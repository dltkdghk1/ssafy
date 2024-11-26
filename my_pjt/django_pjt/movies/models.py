from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre_ids = models.JSONField()
    content = models.TextField(blank=True)
    release_date = models.DateField()
    poster_path = models.TextField()
    vote_average = models.FloatField(default=0.0)
    video_id = models.CharField(max_length=200, null=True)