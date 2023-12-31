from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Publicaciones
from .forms import CrearPublicacionForm, ComentarioForm
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
    
class PostDetalle(DetailView):
    model = Publicaciones
    template_name = 'publicaciones/detalle-post.html'
    context_object_name = 'detalle'
    
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario_comentario'] = ComentarioForm
        return contexto
    
    def post(self, request, *args, **kwargs):
        publicaciones = self.get_object()
        formulario = ComentarioForm(request.POST)
        
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.autor_id = self.request.user.id
            comentario.relacion_post = publicaciones
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)