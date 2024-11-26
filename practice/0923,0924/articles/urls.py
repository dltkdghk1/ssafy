from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 전체 게시글 조회
    path('', views.index, name='index'),
    # 단일 게시글 조회
    # variable routing 사용 -> 단순히 조회 목적
    # 1. views.py 함수에서 pk를 매개변수
    # 2. url naming pattern article.pk
    path('<int:pk>/', views.detail, name='detail'),
    # 페이지를 렌더링
    path('new/', views.new, name='new'),
    # 페이지를 리다이렉트
    path('create/', views.create, name='create'),
    # variable routing -> 조회 후 삭제, 조회 후 수정
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 페이지 랜더링
    path('<int:pk>edit/', views.edit, name='edit'),
    # 페이지 리다이렉트
    path('<int:pk>/update/', views.update, name='update'),
]
