from django.db import models
from django.conf import settings


class Article(models.Model):
  # settings.py의 사용자 모델을 참조
  # on_delete=models.CASCADE -> 연결된 사용자가 삭제되면 게시글도 함께 삭제
  # 사용자와 게시글의 관계(Many_to_one)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=20)
  content = models.TextField()
  image = models.ImageField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
  # 게시글과 댓글간의 관계(Many_to_one)
  # 작성자와 댓글간의 관계(Many_to_one)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)