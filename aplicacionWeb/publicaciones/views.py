from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Publicaciones
from .forms import CrearPublicacionForm
from django.urls import reverse
# Create your views here.

class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'
    
    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        consulta_ordenada = consulta_anterior.order_by('fecha')
        return consulta_ordenada


class Postear(CreateView):
    model = Publicaciones
    template_name = 'publicaciones/postear.html'
    form_class = CrearPublicacionForm
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
class EditarPost(UpdateView):
    model = Publicaciones
    template_name = 'publicaciones/editar-post.html'
    form_class = CrearPublicacionForm
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
class EliminarPost(DeleteView):
    model = Publicaciones
    template_name = 'publicaciones/eliminar-post.html'
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    

''' Agregar línea de comentarios
class PostRealizado(UpdateView):
    template_name = 'publicaciones/publicaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_categoria = self.request.GET.get("id", None)
        antiguedad = self.request.GET.get("orden", None)
        alfabetico = self.request.GET.get("orden", None)

        if id_categoria:
            posteos = Post.objects.filter(categoria_post=id_categoria)
        else:
            if antiguedad == "asc":
                posteos = Post.objects.all().order_by("fecha_creacion")
            elif alfabetico == "a":
                posteos = Post.objects.all().order_by("titulo")
            elif alfabetico == "z":
                posteos = Post.objects.all().order_by("-titulo")
            else:
                posteos = Post.objects.all().order_by("-fecha_creacion")

        categorias = Categoria.objects.all()
        context["posteos"] = posteos
        context["categorias"] = categorias
        return context
'''