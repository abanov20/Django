from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewsSerializer, MovieDetailSerializer, \
    DirectorDetailSerializer, ReviewsDetailSerializer


@api_view(http_method_names=['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
     movies = Movie.objects.all()
     serializer = MovieSerializer(instance=movies, many=True)
     return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        #step1
        title = request.data.get('title')
        description = request.data.get('description', "no description")
        duration = request.data.get('duration')
        director = request.data.get('director')

        director, created = Director.objects.get_or_create(name=director)

        #step2
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director=director
        )
        print(movie)

        return Response(status=status.HTTP_201_CREATED,
                        data=MovieSerializer(movie).data)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def movies_detail_list_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
      data = MovieDetailSerializer(movie).data
      return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director = request.data.get('director')
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=MovieDetailSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
     directors = Director.objects.all()
     serializer = DirectorSerializer(instance=directors, many=True)
     return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(name=name)
        print(director)

        return Response(status=status.HTTP_201_CREATED,
                        data=DirectorSerializer(director).data)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def director_detail_list_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
      data = DirectorDetailSerializer(director).data
      return Response(data=data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=DirectorDetailSerializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
      reviews = Review.objects.all()
      serializer = ReviewsSerializer(instance=reviews, many=True)
      return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')

        movie = get_object_or_404(Movie, id=movie)

        review = Review.objects.create(text=text, movie=movie, stars=stars)
        print(review)

        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewsSerializer(review).data)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def reviews_detail_list_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Reviews not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
      data = ReviewsDetailSerializer(reviews).data
      return Response(data=data)
    elif request.method == 'PUT':
        movie_id = request.data.get('movie')
        movie = get_object_or_404(Movie, id=movie_id)

        reviews.text = request.data.get('text')
        reviews.movie = movie
        reviews.stars = request.data.get('stars')

        reviews.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewsDetailSerializer(reviews).data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET'])
def movies_reviews_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)