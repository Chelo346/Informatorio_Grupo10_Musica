from django.contrib import admin
from django.urls import path, include
#Import views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.indexview, name='index'),
    
    #Include
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls') )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
