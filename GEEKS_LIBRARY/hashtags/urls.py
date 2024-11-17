from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products_lists_view, name='all_products_tags'),
    path('old_products/', views.old_list_view, name='old_tags'),
    path('young_products/', views.young_list_view, name='young_tags'),
    path('children_products/', views.children_list_view, name='children_tags'),
]