from django.urls import path
from .views import CustomLoginView, WatchHistoryView

urlpatterns = [
    path('custom/login/', CustomLoginView.as_view(), name='custom_login'),  # 사용자 정의 로그인 URL
    path('watch-history/', WatchHistoryView.as_view(), name='watch_history'),  # 시청 기록 URL
]
