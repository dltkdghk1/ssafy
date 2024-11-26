# accounts/serializers.py

from rest_framework import serializers
from .models import WatchHistory
from movies.models import Movie

# 영화 직렬화기
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre_ids', 'release_date', 'vote_average', 'poster_path')

# 시청 기록 직렬화기
class WatchHistorySerializer(serializers.ModelSerializer):
    movie = MovieSerializer()  # 영화 정보를 포함하기 위해 영화 직렬화기를 중첩

    class Meta:
        model = WatchHistory
        fields = ('user', 'movie', 'watched_percentage', 'watched_at',)
