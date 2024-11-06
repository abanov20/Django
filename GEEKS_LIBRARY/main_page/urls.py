from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list_view, name='books_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='detail'),
]