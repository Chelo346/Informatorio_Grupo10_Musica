from django.shortcuts import render

# Create your views here.
def home_post(request):
    return render(request, "home.html")

def categorias_post(request):
    return render(request, "categorias.html")

def post(request):
    return render(request, "post.html")