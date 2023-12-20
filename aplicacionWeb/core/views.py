from django.shortcuts import render

# Create your views here.

def indexview(request):
    return render(request, 'index.html', {})


def publicacionesview(request):
    return render(request, 'publicaciones.html', {})