from django.urls import path
from .views import post_list, post_create, post_detail, post_update, post_delete, like

app_name = "blog"
urlpatterns = [
    path("", post_list, name='list'	),
    path("create/", post_create, name='create'),
    path("<str:slug>/", post_detail, name='detail'),
    path("update/<str:slug>/", post_update, name='update'),
    path("delete/<str:slug>/", post_delete, name='delete'),
    path("like/<str:slug>/", like, name='like'),
]
