from rest_framework import serializers
from .models import Movie, Genre



class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)


class MovieListSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        # fields = ('movie_id', 'title','poster_path', 'genre_ids', 'release_date')
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'