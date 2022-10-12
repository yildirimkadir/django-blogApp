from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register, profile


# app_name = "users"
urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login' ),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
]