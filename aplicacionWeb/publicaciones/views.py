from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
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