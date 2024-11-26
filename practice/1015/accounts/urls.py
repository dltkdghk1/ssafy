from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
   path('login/', views.login, name = 'login'),
   path('logout/', views.logout, name = 'logout'),
   path('signup/', views.signup, name = 'signup'), # 회원가입
   # request에 이미 로그인 되어있는 유저의 데이터
   path('delete/', views.delete, name = 'delete'), # 회원탈퇴
   path('update/', views.update, name = 'update'), # 회원정보변경
   path('profile/<username>/', views.profile, name='profile'), # 개인 프로필
   path('<int:user_pk>/follow/', views.follow, name='follow'), # 팔로잉 하기
]
