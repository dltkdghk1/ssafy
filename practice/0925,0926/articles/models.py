from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  # 이미지를 넣지 않아도 게시글이 생성이 되게
  image = models.ImageField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)