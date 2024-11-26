# API 문서화 하는 이유
# -> API개발할 때 다른 사용자나 개발자가 API사용법을 알고 있어야한다.(사용자에게 사용법을 전달한다)
#    수동으로 직접 문서를 작성하면 시간이 많이 들고, 문서 업데이트하는데 번거롭고 잊기 쉽다
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
