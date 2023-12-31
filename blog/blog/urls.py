from django.contrib import admin
from django.urls import path, include

# import staticos/media (importamos para poder visualizar las imagenes en nuestra plantilla)
from django.conf.urls.static import static
from django.conf import settings

# import loginview y logoutview
from django.contrib.auth.views import LoginView, LogoutView

# Import views
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contacto/", views.contacto),
    path("acerca_de/", views.acerca_de, name="acerca_de"),
    
    # 
    # Urls de la aplicacion posts
    path("", include("apps.posts.urls")),
    # urls de otra app
    # urls para el login y logout
    path(
        "login/", LoginView.as_view(template_name="usuarios/login.html"), name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="usuarios/logout.html"),
        name="logout",
    ),
    # urls para el registro de usuarios
    path("usuarios/", include("apps.usuarios.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

