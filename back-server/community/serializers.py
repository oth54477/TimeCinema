from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title",)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user", "content")


# class ReviewListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ('title','content',)


# class Review2Serializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ('title', 'content',)


# class MovieListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = ('title',)


# class MovieList2Serializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = ('title', 'overview',)


# class ActorList2Serializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = ('name',)


# class ActorSerializer(serializers.ModelSerializer):
#     movies = MovieListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Actor
#         fields = '__all__'


# class MovieSerializer(serializers.ModelSerializer):
#     actors = ActorList2Serializer(many=True, read_only=True)
#     review_set = Review2Serializer(many=True, read_only=True)
#     class Meta:
#         model = Movie
#         fields = '__all__'


# class ReviewSerializer(serializers.ModelSerializer):
#     movie = MovieListSerializer(read_only=True)
#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ('movie',)


# class ActorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = ('id', 'name',)
