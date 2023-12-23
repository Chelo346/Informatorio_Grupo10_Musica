from django.db import models

# Create your models here.

# Esta clase es para las categorias

class Categorias(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Publicaciones(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length = 255)
    post = models.TextField()
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, related_name='posteos', null=True)
    
    def __str__(self):
        return self.titulo
    

