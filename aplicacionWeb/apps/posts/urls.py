from django.urls import path
#Import views
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.home_post, name="home-post"),
]
