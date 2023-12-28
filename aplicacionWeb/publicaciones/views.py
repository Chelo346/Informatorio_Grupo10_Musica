from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Publicaciones
from .forms import CrearPublicacionForm
from django.urls import reverse
# Create your views here.

'''Para función post_detail'''
#Import get_objet (sirve para saber si no se encuentra un objeto en nuestro directorio)
from django.shortcuts import get_object_or_404


'''FUNCION COMENTAR (REVISAR)
from .models import Publicacion, Comentario
from django.shortcuts import redirect
'''

class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'
    
    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        consulta_ordenada = consulta_anterior.order_by('fecha')
        return consulta_ordenada
    
    '''FUNCIÓN CREAR COMENTARIO AGREGADA (REVISAR)
    def comentario_create(request, publicacion_id):
        if request.method == 'POST':
            texto = request.POST['texto']
            publicacion = Publicacion.objects.get(id=publicacion_id)
            comentario = Comentario(publicacion=publicacion, texto=texto)
            comentario.save()
            return redirect('publicaciones:post_realizado', publicacion_id=publicacion_id)
            '''


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
    

class Post_detail(DetailView):
    model = Publicaciones
    template_name = 'publicaciones/post-detail.html'
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    

''' (Agregar línea de comentarios en este código)'''
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


''' FUNCIÓN COMENTAR (REVISAR)
class Publicaciones(ListView):
    model = Publicacion
    template_name = 'publicaciones/post_realizado.html'
'''
'''FUNCIÓN POST_DETAIL'''
def post_detail(request, post_id):
    # traer el post con id y si no lo encuentra error 404
    post = get_object_or_404(Publicaciones, pk=post_id)
    ctx = {"publicaciones": publicaciones}
    return render(request, "publicaciones/post-detail.html", ctx)