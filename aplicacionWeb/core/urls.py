from django.contrib import admin
from django.urls import path, include
#Import views
from . import views

urlpatterns = [
    path('index/', views.indexview, name='index'),
    path('publicaciones/', views.publicacionesview, name='publicaciones'),
]