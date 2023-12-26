from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistroForm
from django.urls import reverse
from django.contrib.auth import login, logout

# Create your views here.

class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistroForm
    
    def get_success_url(self):
        return reverse('index')
    
    def form_valid(self, form):
        respuesta = super().form_valid(form)
        usuario = form.save()
        login(self.request, usuario)
        return respuesta
          