from rest_framework import serializers
from .models import Movie, Genre



class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title','poster_path')


class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'