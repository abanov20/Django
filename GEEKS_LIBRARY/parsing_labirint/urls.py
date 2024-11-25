from django.urls import path
from . import views


urlpatterns = [
    path('/labirint_list/', views.LabirintListView.as_view(), name='labirint_list'),
    path('labirint_parser/', views.LabirintFormView.as_view(), name='labirint_parser'),
]