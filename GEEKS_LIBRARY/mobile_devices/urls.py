from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='device_list'),
    path('book_detail/<int:id>/', views.DeviceDetailView.as_view(), name='detail'),
    path('all_products/', views.all_models_lists_view, name='all_products_tags'),
    path('apple_products/', views.Apple_list_view, name='apple_tags'),
    path('xiomi_products/', views.xiomi_list_view, name='xiomi_tags'),
]
