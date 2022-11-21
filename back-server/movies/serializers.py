from rest_framework import serializers
from .models import Movie, Genre, MovieComment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class MovieListSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        # fields = ('movie_id', 'title','poster_path', 'genre_ids', 'release_date')
        fields = "__all__"


class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = "__all__"
        read_only_fields = ("movie", "user")


class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)
    comment_set = MovieCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source="comment_set.count", read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
