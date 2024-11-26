# movies/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # 영화 목록 가져오기
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),  # 특정 영화 가져오기
    path('recommend/', views.recommend_movie, name='recommend_movie'),  # 추천 영화 API
    path('<int:movie_id>/shorts/', views.movies_shorts, name='movies_shorts'),  # 영화 예고편 가져오기
    path('<int:movie_id>/comments/', views.comment_create, name='comment_create'),
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('mycomment/', views.mycomment),
]
