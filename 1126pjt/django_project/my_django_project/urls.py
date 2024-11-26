from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# 간단한 홈 뷰 함수 추가
def home_view(request):
    return HttpResponse("<h1>Welcome to Movie Shorts API!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', include('movies.urls')),  # 영화 관련 URL 연결
    path('api/v1/', include('articles.urls')),  # articles 앱 관련 URL 포함
    path('api/v1/accounts/', include('accounts.urls')),  # accounts 앱의 URL 포함
    path('auth/', include('dj_rest_auth.urls')),  # dj-rest-auth 관련 기본 인증 URL 경로
    path('signup/', include('dj_rest_auth.registration.urls')),  # 회원가입 관련 URL 경로
    path('', home_view, name='home'),  # 루트 URL을 처리하는 뷰 추가
]
