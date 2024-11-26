from django.shortcuts import render
from .serializers import (
    ActorListSerializer,
    ActorDetailSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    ReviewDetailSerializer
)
from rest_framework.decorators import api_view
from .models import Actor, Movie, Review
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def actors_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def actors_detail(request, actor_pk):
    if request.method == 'GET':
        actor = Actor.objects.get(pk=actor_pk)
        serializer = ActorDetailSerializer(actor)
        return Response(serializer.data)

@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def movies_detail(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE',])
def reviews_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST',])
def reviews_create(request, movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        serializer = ReviewDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)

