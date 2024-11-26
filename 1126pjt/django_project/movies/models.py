from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre_ids = models.JSONField()
    genre_names = models.TextField(blank=True)
    content = models.TextField(blank=True)
    release_date = models.DateField()
    poster_path = models.TextField()
    vote_average = models.FloatField(default=0.0)
    video_id = models.CharField(max_length=200, null=True)



class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_comment'
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
