from django.shortcuts import render
from .models import Movie
from .serializers import MovieListSerializer
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
import requests

# Create your views here.
def movie_list(request):
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "ko-KR",
        "page": 1
    }
    response = requests.get(url, params=params).json()

    # 상위 5개의 영화만 데이터베이스에 저장
    results = response.get('results', [])[:2]

    for movie_data in results:
        title = movie_data.get('title', '')
        genre_ids = movie_data.get('genre_ids', [])
        content = movie_data.get('overview', '')

        if not title or not content:
            continue  # 영화 제목이나 줄거리가 없는 경우 제외

        release_date = movie_data.get('release_date') or None
        poster_path = movie_data.get('poster_path') or ''
        vote_average = movie_data.get('vote_average', 0.0)

        # 중복된 영화가 있는지 확인 후, 없으면 추가
        if not Movie.objects.filter(title=title).exists():
            movie = Movie.objects.create(
                title=title,
                genre_ids=genre_ids,
                content=content,
                release_date=release_date,
                poster_path=poster_path,
                vote_average=vote_average
            )

            # 유튜브 API에서 예고편 검색하기
            youtube_url = "https://www.googleapis.com/youtube/v3/search"
            params = {
                "key": settings.YOUTUBE_API_KEY,
                "q": f"{movie.title} official trailer",
                "type": "video",
                "part": "snippet",
                "maxResults": 1,
            }
            youtube_response = requests.get(youtube_url, params=params).json()
            items = youtube_response.get('items', [])
            video_id = items[0].get('id', {}).get('videoId') if items else None

            if video_id:
                movie.video_id = video_id
                movie.save()

    # 모든 영화 데이터를 반환
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)