from django.db import models
from django.conf import settings

# Create your models here.


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class Era(models.Model):
    era_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    adult = models.BooleanField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    release_date = models.DateField()
    genre_ids = models.ManyToManyField(Genre, related_name="genre_movies")
    overview = models.TextField(null=True)
    runtime = models.IntegerField(null=True)
    vote_average = models.FloatField()
    original_title = models.CharField(max_length=50)
    original_language = models.CharField(max_length=50)
    vote_count = models.IntegerField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likeuser_movie")
    watch_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="watchuser_movie")
    era = models.ManyToManyField(Era, related_name="era_movie")
    


class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comment_set")
    star_point = models.IntegerField()
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MovieCommentReply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.ForeignKey(MovieComment, on_delete=models.CASCADE, related_name="reply_set")
    reply_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)