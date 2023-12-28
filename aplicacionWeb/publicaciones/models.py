from django.db import models
from usuarios.models import Usuario

# Create your models here.

# Esta clase es para las categorias

class Categorias(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Publicaciones(models.Model):
    titulo = models.CharField(max_length = 255)
    post = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to="publicaciones")
    subtitulo = models.CharField(max_length = 255, null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, related_name='posteos', null=True)
    
    def __str__(self):
        return self.titulo
    

class Comentarios(models.Model):
    texto = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    relacion_post = models.ForeignKey(Publicaciones, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentario_usuario')
    
    def __str__(self):
        return self.relacion_post.titulo + '' + self.autor.first_name + '' + self.autor.last_name
    

