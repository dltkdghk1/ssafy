from django.urls import path
from . import views

app_name = 'weathers'

urlpatterns = [
    # 원래 서비스라면 index를 없애도 무관하다.
    # 강의를 위해 save-data url을 따로 구성
    path('', views.index, name='index'),
    path('save_data/', views.save_data, name='save_data'),
]
