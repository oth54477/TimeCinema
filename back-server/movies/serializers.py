from rest_framework import serializers
from .models import Movie, Genre, MovieComment, MovieCommentReply
from accounts.models import User
from community.models import Article


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "profile_image")


class UserAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class MovieLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("like_users",)


class MovieWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("watch_users",)


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


class MovieLikeListSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        # fields = ('movie_id', 'title','poster_path', 'genre_ids', 'release_date')
        fields = "__all__"


class MovieCommentReplySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=True)

    class Meta:
        model = MovieCommentReply
        fields = "__all__"
        read_only_fields = ("movie", "user", "comment")



class MovieCommentSerializer(serializers.ModelSerializer):
    reply_set = MovieCommentReplySerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)
    # , many=True

    class Meta:
        model = MovieComment
        fields = "__all__"
        read_only_fields = ("movie", "user")


class MovieCommentUserSerializer(serializers.ModelSerializer):
    reply_set = MovieCommentReplySerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = MovieComment
        fields = "__all__"
        read_only_fields = ("movie", "user")



class MovieCommentCreateSerializer(serializers.ModelSerializer):
    reply_set = MovieCommentReplySerializer(read_only=True, many=True)

    class Meta:
        model = MovieComment
        fields = "__all__"
        read_only_fields = ("movie", "user")



class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)
    comment_set = MovieCommentSerializer(read_only=True, many=True)
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_count = serializers.IntegerField(source="comment_set.count", read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    watch_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ("comment_set", "comment_count", "genre_ids")

# movie_id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=50)
#     adult = models.BooleanField()
#     popularity = models.FloatField()
#     poster_path = models.TextField()
#     release_date = models.DateField()
#     genre_ids = models.ManyToManyField(Genre, related_name="genre_movies")
#     overview = models.TextField(null=True)
#     runtime = models.IntegerField(null=True)
#     vote_average = models.FloatField()
#     original_title = models.CharField(max_length=50)
#     original_language = models.CharField(max_length=50)
#     vote_count = models.IntegerField(null=True)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likeuser_movie")
#     watch_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="watchuser_movie")