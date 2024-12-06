from django.core.serializers import serialize
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewsSerializer, MovieDetailSerializer, \
    DirectorDetailSerializer, ReviewsDetailSerializer


@api_view(http_method_names=['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def movies_detail_list_api_view(request, id):
    movie = Movie.objects.get(id=id)
    data = MovieDetailSerializer(movie).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(instance=directors, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def director_detail_list_api_view(request, id):
    directors = Director.objects.get(id=id)
    data = DirectorDetailSerializer(directors).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewsSerializer(instance=reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def reviews_detail_list_api_view(request, id):
    reviews = Review.objects.get(id=id)
    data = ReviewsDetailSerializer(reviews).data
    return Response(data=data)


