from django.contrib import admin
from django.urls import path, include
#Import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include('core.urls')),
]