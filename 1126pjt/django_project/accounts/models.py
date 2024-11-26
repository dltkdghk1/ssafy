from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from movies.models import Movie

# 사용자 모델
class User(AbstractUser):
    pass

# 시청 기록 모델
class WatchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched_percentage = models.FloatField(default=0.0)  # 사용자가 시청한 비율
    watched_at = models.DateTimeField(default=timezone.now)  # 시청 시간
    genre_names = models.TextField(blank=True)  # 장르 이름 (콤마로 구분된 문자열)
    reward = models.FloatField(default=0.0)  # 보상 값을 추가합니다.
