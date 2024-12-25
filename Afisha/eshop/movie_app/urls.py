
from django.urls import path, include
from movie_app import views


urlpatterns = [
    path('api/v1/movies/', views.movies_list_api_view),
    path('api/v1/directors/', views.director_list_api_view),
    path('api/v1/reviews/', views.reviews_list_api_view),
    path('api/v1/movies/<int:id>/', views.movies_detail_list_api_view),
    path('api/v1/directors/<int:id>/', views.director_detail_list_api_view),
    path('api/v1/reviews/<int:id>/', views.reviews_detail_list_api_view),
    path('api/v1/movies/reviews/', views.movies_reviews_list_api_view),
]
