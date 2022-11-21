from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import JsonResponse

from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from django.core import serializers

# from .serializers import ActorSerializer, MovieList2Serializer, MovieSerializer, ReviewSerializer, ActorListSerializer, ReviewListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
@require_GET
def index(request):
    article = Article.objects.all()
    if article:
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    return JsonResponse({})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("community:detail", article.pk)
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "community/create.html", context)


@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "community/detail.html", context)


@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect("community:detail", article.pk)
    context = {
        "comment_form": comment_form,
        "article": article,
        "comments": article.comment_set.all(),
    }
    return render(request, "community/detail.html", context)


@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            is_like = False
        else:
            article.like_users.add(user)
            is_like = True
        context = {
            "is_like": is_like,
            "like_user_count": article.like_users.count(),
        }
    return JsonResponse(context)
