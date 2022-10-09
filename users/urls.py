from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = "users"
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path('register/', register, name="register"),
]