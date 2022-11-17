
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# # from rest_framework import generics

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer, MovieDetailSerializer


from django.http.response import JsonResponse

@api_view(['GET'])
def main(request) :
    if request.method == 'GET':
        # 가장 최근에 개봉한 영화
        latest_movies = Movie.objects.order_by('-release_date').prefetch_related('genres')[:20]
        latest_serializer = MovieSerializer(data=latest_movies, many=True)
        # print(latest_movies[0].genres.all())
        latest_serializer.is_valid()

        # 영화 평점 순
        highscore_movies = Movie.objects.order_by('-vote_average').prefetch_related('genres')[:20]
        highscore_serializer = MovieSerializer(data=highscore_movies, many=True)
        highscore_serializer.is_valid()

        # 많은 사람들이 투표한 영화
        like_movies = Movie.objects.order_by('-vote_count').prefetch_related('genres')[:20]
        like_serializer = MovieSerializer(data=like_movies, many=True)
        like_serializer.is_valid()
        
        context={
            'latest_movies' : latest_serializer.data,
            'highscore_movies' : highscore_serializer.data,
            'like_movies' : like_serializer.data,
        }
        return Response(context)


@api_view(['GET'])
def movie_detail(request, movie_pk) :
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieDetailSerializer(movie)
        
        # 영화 genre의 id list
        genres = movie.genres.all().values_list('id', flat=True)
        movies_same_genre = Movie.objects.filter(genres__id__in=genres).prefetch_related('genres').distinct().order_by('-vote_count')[:20]

        same_genre_serializer = MovieSerializer(data = movies_same_genre, many=True)
        same_genre_serializer.is_valid()

        context = {
            "movie" : serializer.data, 
            "same_genres" : same_genre_serializer.data,
        }

        return Response(context)

