# from django.http import HttpResponse
# <<<<<<< HEAD:aplicacionWeb/blog/blog/views.py
# # render
# from django.shortcuts import render 

# def saludo(request):
#     return render(request, 'index.html')

# def despedida(request):
#     return HttpResponse("Buenas Noches!")

# def nombre(request):
#     return HttpResponse(
#         {"Gonzalo" + " " + "Pérez de Eulate",})
# =======
# #  render
# from django.shortcuts import render
# # Cada vez que agrego una funcion nueva tiene que ser llamado desde url.
# def saludo(request):
#     return render(request, "index.html")
# <<<<<<< HEAD
# >>>>>>> main:aplicacionWeb/blog/views.py
# =======
# >>>>>>> bfe200699467f6e62f4021d085228feae5ec20cb

from django.http import HttpResponse
#  render
from django.shortcuts import render
# Cada vez que agrego una funcion nueva tiene que ser llamado desde url.
'''
def saludo(request):
    return render(request, "index.html")
    '''
