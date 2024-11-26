from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    # 전체 게시글 조회
    path('', views.index, name = 'index'),
    # 단일 게시글 조회(detail 페이지)
    # variable routing ---> 단순히 조회 목적
    # 1. views.py 함수에서 pk를 매개변수
    # 2. url naming pattern article.pk
    path('<int:pk>/', views.detail, name = 'detail'),
    # 페이지 랜더링 + 리다이렉트
    path('create/', views.create, name = 'create'),
    # variable routing ---> 조회 후 삭제, 조회 후 수정
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    # 페이지 렌더링 + 리다이렉트
    path('<int:pk>/update/', views.update, name = 'update'),
    # 댓글 생성 url
    path('<int:pk>/comments/', views.comments_create, name = 'comments_create'),
    path(
      '<int:article_pk>/comments/<int:comment_pk>/delete/',
      views.comments_delete,
      name = 'comments_delete'
    ),
    path('<int:article_pk>/likes/', views.likes, name = 'likes'),
]
