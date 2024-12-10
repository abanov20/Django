from rest_framework import serializers
from .models import Movie, Director, Review

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['movie', 'text']

class ReviewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['movie', 'text']
