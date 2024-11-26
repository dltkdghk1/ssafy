from rest_framework import serializers
from .models import DepositProducts, DespositOptions

class DepositProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class DepositOptionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DespositOptions
        fields = '__all__'
        read_only_fields = ('product',)
