from django.contrib import admin
from django.urls import path, include
#Import views
from . import views

urlpatterns = [
    path('index/', views.indexview, name='index'),
    
    #Include
    path('publicaciones/', include('publicaciones.urls')),
]