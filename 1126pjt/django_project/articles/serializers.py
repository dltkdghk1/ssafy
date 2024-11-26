from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)

class MyArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at']

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
            'user'
        )
        # read_only = ('user',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)
        class Meta:
            model = Comment
            fields = ('id', 'content', 'user')
    comment_set = CommentDetailSerializer(read_only=True, many=True)
    number_of_comments = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    article = ArticleTitleSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)
