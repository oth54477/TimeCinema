from django.urls import path
from . import views


app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/<int:movie_pk>", views.detail, name="detail"),
    path("<int:movie_pk>/comment", views.comment_list, name="comment_list"),
    path("<int:movie_pk>/comment/create", views.comment_create, name="comment_create"),
    path("<int:movie_pk>/comment/<int:comment_pk>/reply/create", views.reply_create, name="reply_create"),
    path("<int:movie_pk>/comment/<int:comment_pk>/reply", views.reply_list, name="reply_list"),
    path("recommended", views.recommended, name="recommended"),
    path("movie_list", views.movie_list, name="movie_list"),
    path("<int:movie_pk>", views.movie_detail, name="movie_detail"),
    path("<int:movie_pk>/like", views.movie_like, name="movie_like"),
    path("<int:movie_pk>/watch", views.movie_watch, name="movie_watch"),
    path("user_list", views.user_list, name="user_list"),
    path("comment/<int:user_pk>", views.user_comment, name="user_comment"),
    path("like/<int:user_pk>", views.user_like, name="user_like"),
]


