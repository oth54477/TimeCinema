from django import forms
from .models import MovieComment


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         # fields = ('title', 'content', 'image',)
#         # exclude = ('title',)
#         exclude = ("user",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        exclude = ("user", "movie")
