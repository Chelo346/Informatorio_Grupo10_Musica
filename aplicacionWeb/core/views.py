from django.shortcuts import render
from core.models import Publicaciones

# Create your views here.

def indexview(request):
    return render(request, 'index.html', {})


def publicacionesView(request):
    ctx = {
        'posteos': Publicaciones.objects.all()
    }
    return render(request, 'publicaciones.html', ctx)
