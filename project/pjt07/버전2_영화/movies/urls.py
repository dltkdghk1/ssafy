from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actors_list),
    path('actors/<int:actor_pk>/', views.actors_detail),
    path('movies/', views.movies_list),
    path('movies/<int:movie_pk>/', views.movies_detail),
    path('reviews/<int:review_pk>/', views.reviews_detail),
    path('movies/<int:movie_pk>/reviews/', views.reviews_create),
]
