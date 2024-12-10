from rest_framework import serializers
from .models import Movie, Director, Review

class MovieDetailSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movie_count']

    def get_movie_count(self, obj):
        return obj.movie_set.count()

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['movie', 'text', 'stars']

class ReviewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['movie', 'text', 'stars']

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    reviews = ReviewsSerializer(source='review_set', many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        reviews = obj.review_set.all()
        if reviews.exists():
            return sum(review.stars for review in reviews) / reviews.count()
        return 0