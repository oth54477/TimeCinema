from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_pk>/", views.detail, name="detail"),
    path("<int:movie_pk>/comment", views.comment_create, name="comment_create"),
    path("recommended/", views.recommended, name="recommended"),
    path("movie_list/", views.movie_list, name="movie_list"),
    path("movie/<int:movie_pk>/", views.movie_detail),
]
