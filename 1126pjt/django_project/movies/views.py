from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.conf import settings
from ml.dqn_model import model
import requests
import torch
from .models import Movie, Comment
from accounts.models import WatchHistory
import logging
import random
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .serializer import MovieDetailSerializer, CommentListSerializer, MyCommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

# 로깅 설정
logger = logging.getLogger(__name__)

# TMDB에서 상위 10개 영화 리스트 가져오기 및 유튜브 예고편 정보 추가 (무작위로 10개 선택)
@api_view(['GET'])
def movie_list(request):
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "ko-KR",
        "page": 1
    }
    try:
        # 영화 장르 리스트 가져오기 (장르 ID와 이름 매핑을 위해)
        genre_url = "https://api.themoviedb.org/3/genre/movie/list"
        genre_params = {
            "api_key": settings.TMDB_API_KEY,
            "language": "ko-KR"
        }
        genre_response = requests.get(genre_url, params=genre_params)
        if genre_response.status_code != 200:
            logger.error(f"Failed to fetch genres from TMDB. Status code: {genre_response.status_code}")
            return JsonResponse({"error": "Failed to fetch genres from TMDB."}, status=500)
        
        genre_data = genre_response.json()
        genre_mapping = {genre['id']: genre['name'] for genre in genre_data.get('genres', [])}

        response = requests.get(url, params=params)
        if response.status_code != 200:
            logger.error(f"Failed to fetch popular movies from TMDB. Status code: {response.status_code}")
            return JsonResponse({"error": "Failed to fetch popular movies from TMDB."}, status=500)
        
        results = response.json().get('results', [])
        
        # 영화 데이터를 무작위로 10개 선택
        if len(results) > 10:
            results = random.sample(results, 10)

        for movie_data in results:
            title = movie_data.get('title', '')
            genre_ids = movie_data.get('genre_ids', [])
            content = movie_data.get('overview', '')

            if not title or not content:
                continue

            # 장르 ID를 장르 이름으로 변환
            genre_names = [genre_mapping.get(genre_id, "Unknown") for genre_id in genre_ids]
            genre_names_str = ', '.join(genre_names)

            release_date = movie_data.get('release_date') or None
            poster_path = movie_data.get('poster_path') or ''
            vote_average = movie_data.get('vote_average', 0.0)

            # 중복된 영화가 있는지 확인 후, 없으면 추가
            movie, created = Movie.objects.get_or_create(
                title=title,
                defaults={
                    'genre_ids': genre_ids,
                    'genre_names': genre_names_str,
                    'content': content,
                    'release_date': release_date,
                    'poster_path': poster_path,
                    'vote_average': vote_average
                }
            )
            if created:
                logger.info(f"Created new movie entry: {title}")
            else:
                # 중복된 영화가 있을 경우 데이터 업데이트
                movie.genre_names = genre_names_str
                movie.save()
                logger.info(f"Updated movie entry with new genre names: {title}")

        # 모든 영화 데이터를 반환 (무작위로 10개 선택)
        movies = Movie.objects.all()
        if len(movies) > 10:
            movies = random.sample(list(movies), 10)

        movie_list_with_trailers = []

        for movie in movies:
            # 유튜브 예고편 검색하기
            youtube_url = "https://www.googleapis.com/youtube/v3/search"
            params = {
                "key": settings.YOUTUBE_API_KEY,
                "q": f"{movie.title} official trailer",
                "type": "video",
                "part": "snippet",
                "maxResults": 1,
            }
            youtube_response = requests.get(youtube_url, params=params)
            if youtube_response.status_code != 200:
                logger.error(f"Failed to fetch YouTube trailer for {movie.title}. Status code: {youtube_response.status_code}")
                video_id = None
            else:
                response_data = youtube_response.json()
                items = response_data.get('items', [])
                video_id = items[0].get('id', {}).get('videoId') if items else None

            # 유튜브 API의 응답 확인을 위한 로깅 추가
            if video_id:
                logger.info(f"Fetched video ID: {video_id} for movie: {movie.title}")
            else:
                logger.warning(f"No trailer found for movie: {movie.title}")

            # movie 데이터에 video_id 업데이트
            movie.video_id = video_id
            movie.save()

            movie_data = {
                "id": movie.id,
                "title": movie.title,
                "release_date": movie.release_date,
                "poster_path": movie.poster_path,
                "content": movie.content,
                "vote_average": movie.vote_average,
                "genre_names": movie.genre_names,
                "video_id": video_id
            }

            movie_list_with_trailers.append(movie_data)

        return JsonResponse(movie_list_with_trailers, safe=False)

    except requests.exceptions.RequestException as e:
        # 외부 API 호출 실패 시의 오류 처리
        logger.error(f"External API request failed: {e}")
        return JsonResponse({"error": "Failed to fetch data from external API.", "details": str(e)}, status=500)

# 특정 영화 정보 가져오기
@api_view(['GET'])
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieDetailSerializer(movie)  # Movie 객체를 직렬화
        return Response(serializer.data)  # 직렬화된 데이터를 반환
    except Movie.DoesNotExist:
        logger.warning(f"Movie with ID {movie_id} not found.")
        return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

# 추천 API
@api_view(['GET'])
def recommend_movie(request):
    user_id = request.user.id

    # 사용자의 최신 시청 기록을 가져와 상태를 정의
    watch_history = WatchHistory.objects.filter(user=user_id).order_by('-watched_at')[:5]
    if not watch_history:
        logger.warning(f"No watch history found for user ID {user_id}.")
        return JsonResponse({"error": "No watch history found."}, status=404)

    # 상태 정의 (예: 시청 비율)
    state = [history.watched_percentage for history in watch_history]
    while len(state) < 5:
        state.append(0)

    state_tensor = torch.FloatTensor(state).unsqueeze(0)

    try:
        action_values = model(state_tensor)
        recommended_movie_idx = torch.argmax(action_values).item()

        # 추천된 영화 반환
        recommended_movie = Movie.objects.all()[recommended_movie_idx]
        movie_data = {
            "movie_id": recommended_movie.id,
            "title": recommended_movie.title,
            "genre_names": recommended_movie.genre_names,
            "video_id": recommended_movie.video_id
        }
        return JsonResponse(movie_data)
    except (Movie.DoesNotExist, IndexError, RuntimeError) as e:
        logger.error(f"Recommendation failed: {e}")
        return JsonResponse({"error": "Movie not found or recommendation failed.", "details": str(e)}, status=500)

# 유튜브 예고편 가져오기
@api_view(['GET'])
def movies_shorts(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        logger.warning(f"Movie with ID {movie_id} not found for trailer request.")
        return JsonResponse({"error": "Movie not found."}, status=404)

    youtube_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": settings.YOUTUBE_API_KEY,
        "q": f"{movie.title} official trailer",
        "type": "video",
        "part": "snippet",
        "maxResults": 1,
    }

    try:
        response = requests.get(youtube_url, params=params)
        if response.status_code != 200:
            return JsonResponse({"error": "Failed to fetch trailer from YouTube."}, status=500)

        response_data = response.json()
        items = response_data.get('items', [])
        video_id = items[0].get('id', {}).get('videoId') if items else None

        if not video_id:
            return JsonResponse({"error": "No trailer found for this movie."}, status=404)

        return JsonResponse({"video_id": video_id})

    except requests.exceptions.RequestException as e:
        logger.error(f"YouTube API request failed: {e}")
        return JsonResponse({"error": "YouTube API request failed.", "details": str(e)}, status=500)


@api_view(['GET'])
@permission_classes([])
def comment_list(request):
    # 댓글 전체 조회
    comment = Comment.objects.all()
    # 댓글 목록 쿼리셋을 직렬화 진행
    serializer = CommentListSerializer(comment, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([])
def comment_detail(request, comment_pk):
    # 단일 댓글 조회
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        # 단일 댓글 직렬화
        serializer = CommentListSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentListSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([])
def comment_create(request, movie_id):
    # 게시글 조회 (어떤 게시글에 작성되는 댓글인지)
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = CommentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 외래 키 데이터 입력 후 저장
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
@permission_classes([])
def mycomment(request):
    user = request.user
    comment = user.movie_comment.all()
    serializer = MyCommentSerializer(comment, many=True)
    return Response(serializer.data)