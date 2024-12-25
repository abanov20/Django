from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.RegisterSerializer, name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('confirm/', views.SMSCodeConfirm.as_view(), name="logout"),
]