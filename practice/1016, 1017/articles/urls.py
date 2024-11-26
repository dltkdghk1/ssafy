from django.urls import path
from . import views

# app_name은 template가 없어서 쓰지 않음

urlpatterns = [
    # 전체 게시글 조회
    path('articles/', views.article_list),
    # 단일 게시글 조회
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments', views.comment_create),
]
