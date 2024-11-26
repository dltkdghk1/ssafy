from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import WatchHistory
from .serializers import WatchHistorySerializer
from movies.models import Movie
import logging

# 로깅 설정
logger = logging.getLogger(__name__)

# 보상 계산 함수 정의
def reward_function(watched_percentage):
    """시청 비율에 따른 보상을 계산하는 함수"""
    if watched_percentage > 90:
        return 1.0  # 높은 비율 시청 시 높은 보상
    elif watched_percentage > 70:
        return 0.7
    elif watched_percentage > 50:
        return 0.5  # 중간 비율 시청 시 중간 보상
    elif watched_percentage > 25:
        return 0.2
    else:
        return 0.1  # 낮은 비율 시청 시 낮은 보상

# CustomLoginView 클래스 정의
class CustomLoginView(LoginView):
    """사용자 로그인을 위한 뷰"""
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            if response.status_code == 200 and 'key' in response.data:
                return Response({'token': response.data['key']}, status=status.HTTP_200_OK)
            return response
        except Exception as e:
            logger.error(f"CustomLoginView Error: {e}")
            return Response({'error': 'Login failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 시청 기록 뷰 정의
@method_decorator(csrf_exempt, name='dispatch')  # CSRF 예외 처리 추가
class WatchHistoryView(APIView):
    """사용자의 시청 기록을 조회하고 저장하는 API 뷰"""
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request, *args, **kwargs):
        try:
            watch_history = WatchHistory.objects.filter(user=request.user)
            if not watch_history.exists():
                logger.warning(f"No watch history found for user: {request.user.id}")
                return Response({'message': 'No watch history found.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = WatchHistorySerializer(watch_history, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching watch history: {e}")
            return Response({'error': 'Failed to fetch watch history.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        user = request.user
        movie_id = request.data.get('movie_id')
        watched_percentage = request.data.get('watched_percentage')

        if not movie_id or watched_percentage is None:
            logger.warning(f"Invalid data received: movie_id={movie_id}, watched_percentage={watched_percentage}")
            return Response({'error': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            movie = Movie.objects.get(id=movie_id)
            if not (0 <= watched_percentage <= 100):
                logger.warning(f"Invalid watched_percentage value: {watched_percentage}")
                return Response({'error': 'Invalid watched percentage value.'}, status=status.HTTP_400_BAD_REQUEST)

            reward = reward_function(watched_percentage)

            # 시청 기록 저장
            WatchHistory.objects.create(
                user=user,
                movie=movie,
                watched_percentage=watched_percentage,
                genre_names=movie.genre_names,  # 여기서 movie.genre_names를 제대로 가져오는지 확인
                reward=reward
            )
            logger.info(f"Watch history recorded for user: {user.id}, movie: {movie_id}")
            return Response({'message': 'Watch history recorded successfully.'}, status=status.HTTP_201_CREATED)
        except Movie.DoesNotExist:
            logger.error(f"Invalid movie ID: {movie_id}")
            return Response({'error': 'Invalid movie ID.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error saving watch history: {e}")
            return Response({'error': 'Failed to save watch history.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
