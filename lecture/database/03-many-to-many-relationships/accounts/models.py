from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # 상대방을 팔로우 했다고 상대방이 나를 팔로우 한게 아니므로 대칭이 아니다 즉, symmetrical=False
    
