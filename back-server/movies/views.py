from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.decorators.http import require_safe
from .models import Movie

from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from django.core import serializers
from .serializers import MovieListSerializer, MovieSerializer, MovieCommentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import CommentForm

import datetime

# Create your views here.
@require_safe
def index(request):
    # movies = get_list_or_404(Movie)
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, "movies/index.html", context)


@api_view(["GET"])
def movie_list(request):
    movies_list = []
    start_date = datetime.date(2022, 7, 1)
    end_date = datetime.date(2022, 7, 31)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    serializer = MovieListSerializer(movies, many=True)
    movies_list.append(serializer.data)
    start_date = datetime.date(2022, 8, 1)
    end_date = datetime.date(2022, 8, 31)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    serializer = MovieListSerializer(movies, many=True)
    movies_list.append(serializer.data)
    start_date = datetime.date(2022, 9, 1)
    end_date = datetime.date(2022, 9, 30)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    serializer = MovieListSerializer(movies, many=True)
    movies_list.append(serializer.data)
    start_date = datetime.date(2022, 10, 1)
    end_date = datetime.date(2022, 10, 31)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    serializer = MovieListSerializer(movies, many=True)
    movies_list.append(serializer.data)
    return Response(movies_list)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm()
    context = {"movie": movie, "comment_form": comment_form}
    return render(request, "movies/detail.html", context)


@api_view(["GET"])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(["POST"])
def comment_create(request, movie_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        best_movie = Movie.objects.all().order_by("-popularity")[0]
        recommended_movies = Movie.objects.all().order_by("-popularity")[1:10]
        context = {"best_movie": best_movie, "movies": recommended_movies}
        return render(request, "movies/recommended.html", context)
    return redirect("accounts:login")
