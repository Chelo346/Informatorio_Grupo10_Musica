"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD:aplicacionWeb/blog/blog/urls.py
from django.urls import path
# Import views
=======
from django.urls import path, include
#Import views
>>>>>>> main:aplicacionWeb/blog/urls.py
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD:aplicacionWeb/blog/blog/urls.py
    path("", views.saludo, name='saludo'),
    path("despedir/", views.despedida, name='despedir'),
    path("nombre/", views.nombre, name='nombre'),
=======
    path("", views.saludo, name="saludo"),
>>>>>>> main:aplicacionWeb/blog/urls.py
=======
    
    path("", include('core.urls')),
>>>>>>> bfe200699467f6e62f4021d085228feae5ec20cb
]
