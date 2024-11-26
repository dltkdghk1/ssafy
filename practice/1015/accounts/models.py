from django.db import models
# Create your models here.
# AbstractUser : 로그인, 권한 관리 등에 필요한 기본적인 필드 제공
from django.contrib.auth.models import AbstractUser

# self : 재귀적으로 다대다 관계
# AbstrackUser : 로그리인, 권한 관리 등에 필요한 기본적인 필드 제공
class User(AbstractUser):
  followings = models.ManyToManyField(
    'self', symmetrical=False, related_name='followers'
  )