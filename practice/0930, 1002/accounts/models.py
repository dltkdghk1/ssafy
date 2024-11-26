from django.db import models
# AbstractUser : 로그인, 관한 관리 등에 필용한 기본적인 필드 제공
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass