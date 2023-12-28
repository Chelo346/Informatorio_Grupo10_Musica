from django.contrib import admin
from .models import Publicaciones, Categorias, Comentarios

# Register your models here.

admin.site.register(Publicaciones)
admin.site.register(Categorias)
admin.site.register(Comentarios)