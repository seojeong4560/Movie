
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# from rest_framework import status
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# # from rest_framework import generics

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Comment, Mbti, Detail
from .serializers import MovieSerializer, GenreSerializer, MovieDetailSerializer, CommentSerializer, MbtiSerializer, DetailSerializer, MovieBackdropSerializer

from django.http.response import JsonResponse
from datetime import datetime
import ast
import random


@api_view(['GET'])
def main(request) :
    if request.method == 'GET':
        now = datetime.now()
        temp = Movie.objects.order_by('-release_date').prefetch_related('genres')[:50]

        i = 0
        while True:
            if str(now)[:10] < str(temp[i].release_date):
                i += 1
            else:
                break
        
        # 상영 예정작
        upcomming_movies = temp[:i]
        upcomming_serializer = MovieSerializer(data=upcomming_movies, many=True)
        upcomming_serializer.is_valid()


        # 가장 최근에 개봉한 영화
        latest_movies = temp[i:i+20]
        latest_serializer = MovieSerializer(data=latest_movies, many=True)
        latest_serializer.is_valid()

        # print(latest_movies[0].genres.all())
        # print(temp[0].release_date)
        # print(str(now)[:10]>"2023-10-30")
        

        # 영화 평점 순
        highscore_movies = Movie.objects.order_by('-vote_average').prefetch_related('genres')[:20]
        highscore_serializer = MovieSerializer(data=highscore_movies, many=True)
        highscore_serializer.is_valid()

        # 많은 사람들이 투표한 영화
        like_movies = Movie.objects.order_by('-vote_count').prefetch_related('genres')[:20]
        like_serializer = MovieSerializer(data=like_movies, many=True)
        like_serializer.is_valid()
        
        context={
            'upcomming_movies' : upcomming_serializer.data,
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


# @api_view(['GET'])
# def random_backdrop(request) :
#     if request.method == 'GET':
#         backdrop = Movie.objects.get()
#         serializer = MovieBackdropSerializer(movie)

#         return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        # comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)




@api_view(['GET'])
def mbti_detail(request, mbti_pk):
    if request.method == 'GET':
        mbti = Mbti.objects.get(pk=mbti_pk)
        serializer = MbtiSerializer(mbti)
        return Response(serializer.data)

@api_view(['GET'])
def mbti_recommend(request, type):
    if request.method == 'GET':
        recommend = Detail.objects.get(type=type)
        # recommend = Mbti.objects.all()
        serializer = DetailSerializer(recommend)
        return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def recommend(request):
    if request.method == 'POST':
        selected = request.data.get("genres")
        selected_genre = Movie.objects.filter(genres__id__in=selected).prefetch_related('genres').distinct().order_by('-vote_count')[:20]
        recommend_serializer = MovieSerializer(data=selected_genre, many=True)
        recommend_serializer.is_valid()

        context = {
            'selected_genre' : recommend_serializer.data,
        }
        return Response(context)

    else:
        genres = Genre.objects.all()        
        genres_serializer = GenreSerializer(data=genres, many=True)
        genres_serializer.is_valid()
        context = {
            'genres': genres_serializer.data,
        }
        return Response(context)