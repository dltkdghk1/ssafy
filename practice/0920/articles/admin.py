from django.contrib import admin

# Register your models here.
# .(현재디렉토리)의 models.py에서 Article 모델을 가져오겠다.
from .models import Board

# Board 모델을 django 관리자 사이트에 등록
admin.site.register(Board)