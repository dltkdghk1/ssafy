from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    #  1. 게임화면 출력
    path('start/', views.start, name='start'),
    # 2. 정답을 체크
    path('guess/int:game_session_id>/', views.guess, name='guess'),
]
