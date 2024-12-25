from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Movie, Director, Review
from .serializers import (
    MovieValidateSerializer,
    MovieCreateSerializer,
    MovieDetailSerializer,
    MovieUpdateSerializer,
    DirectorValidateSerializer,
    DirectorCreateSerializer,
    DirectorDetailSerializer,
    DirectorUpdateSerializer,
    ReviewUpdateSerializer,
    ReviewCreateSerializer,
    ReviewsDetailSerializer,
    MovieSerializer,
    ReviewsSerializer
)

class MoviesListAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieValidateSerializer(instance=movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description', "no description")
        duration = serializer.validated_data.get('duration')
        director_name = serializer.validated_data.get('director')

        director, created = Director.objects.get_or_create(name=director_name)

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director=director
        )
        return Response(status=status.HTTP_201_CREATED, data=MovieSerializer(movie).data)


class MoviesDetailAPIView(APIView):
    def get(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        data = MovieDetailSerializer(movie).data
        return Response(data=data)

    def put(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        serializer = MovieUpdateSerializer(data=request.data, context={'movie': movie})
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director = serializer.validated_data.get('director')
        movie.save()
        return Response(status=status.HTTP_201_CREATED, data=MovieDetailSerializer(movie).data)

    def delete(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DirectorsListAPIView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorValidateSerializer(instance=directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DirectorCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        name = serializer.validated_data.get('name')
        director = Director.objects.create(name=name)
        return Response(status=status.HTTP_201_CREATED, data=DirectorDetailSerializer(director).data)


class DirectorsDetailAPIView(APIView):
    def get(self, request, id):
        director = get_object_or_404(Director, id=id)
        data = DirectorDetailSerializer(director).data
        return Response(data=data)

    def put(self, request, id):
        director = get_object_or_404(Director, id=id)
        serializer = DirectorUpdateSerializer(data=request.data, context={'director': director})
        serializer.is_valid(raise_exception=True)

        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(status=status.HTTP_201_CREATED, data=DirectorDetailSerializer(director).data)

    def delete(self, request, id):
        director = get_object_or_404(Director, id=id)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewsListAPIView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewUpdateSerializer(instance=reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie')
        stars = serializer.validated_data.get('stars')

        movie = get_object_or_404(Movie, id=movie_id)

        review = Review.objects.create(text=text, movie=movie, stars=stars)
        return Response(status=status.HTTP_201_CREATED, data=ReviewsSerializer(review).data)


class ReviewsDetailAPIView(APIView):
    def get(self, request, id):
        review = get_object_or_404(Review, id=id)
        data = ReviewsDetailSerializer(review).data
        return Response(data=data)

    def put(self, request, id):
        review = get_object_or_404(Review, id=id)
        serializer = ReviewUpdateSerializer(data=request.data, context={'review': review})
        serializer.is_valid(raise_exception=True)

        movie_id = serializer.validated_data.get('movie')
        movie = get_object_or_404(Movie, id=movie_id)

        review.text = serializer.validated_data.get('text')
        review.movie = movie
        review.stars = serializer.validated_data.get('stars')
        review.save()
        return Response(status=status.HTTP_201_CREATED, data=ReviewsDetailSerializer(review).data)

    def delete(self, request, id):
        review = get_object_or_404(Review, id=id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesReviewsListAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
