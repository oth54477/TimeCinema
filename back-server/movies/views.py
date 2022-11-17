from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.decorators.http import require_safe
from .models import Movie

from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from django.core import serializers
from .serializers import MovieListSerializer, MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@require_safe
def index(request):
    # movies = get_list_or_404(Movie)
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)



@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)



@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



@require_safe
def recommended(request):
    if request.user.is_authenticated:
        best_movie = Movie.objects.all().order_by("-popularity")[0]
        recommended_movies = Movie.objects.all().order_by("-popularity")[1:10]
        context = {
            'best_movie' : best_movie,
            'movies' : recommended_movies
        }
        return render(request, 'movies/recommended.html', context)
    return redirect('accounts:login')