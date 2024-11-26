from django.contrib import admin
from django.urls import path
# .은 현재 디렉토리
from . import views

# URL 네임스페이스 다른 앱과 혼동하지 않기 위해 사용
# {% url 'articles:index' %}
app_name = "articles"

# name='index' -> naming url 패턴
# 직접 href = "/index/"와 같이 직접 url주소를 쓰는 번거로움을 덜어줌
# 이렇게 하드코딩하지 않고 name으로 참조
urlpatterns = [
  path('index/', views.index, name='index'),
  path('dinner/', views.dinner, name='dinner'),
  path('search/', views.search, name='search'),
  path('throw/', views.throw, name='throw'),
  path('catch/', views.catch, name='catch'),

  # <데이터타입:변수명> : variable routing 왜 쓸까?
  # 여러개의 url을 하나의 뷰로 처리하기 위해
  path('<int:number>', views.detail, name="detail")
]