from rest_framework import serializers
from .models import Weather

# django가 사용하는 데이터 형식 -> python
# 우리 서비스 = 웹 서비스 -> 다른 언어, 환경에서 요청이 올 수도 있다.
# -> 모든 요청에 부합할 수 있도록 데이터 형식을 정해야한다.
# -> Json형식으로 바꿔야한다.
# -> DRF는 Json형식으로 변환을 serializers를 통해서 쉽게 할 수 있도록 해준다.
# DB에 지정된 필드로만 포장에 관여 : ModelSerializer
#   -> 여러 테이블의 데이터를 한번에 포장 : Nested Serializer
# DB필드 외의 데이터들도 포장에 관여 : serializer
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'