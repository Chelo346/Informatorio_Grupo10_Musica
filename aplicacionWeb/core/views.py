from django.shortcuts import render

'''IMPORTACIONES PARA ENTRAR EN LAS PUBLICACIONES
#import get_objet
from django.shortcuts import get_object_or_404
'''

# Create your views here.

def indexview(request):
    return render(request, 'index.html')


'''FUNCIÓN PARA ENTRAR DENTRO DE LAS PUBLICACIONES
def post_detail(request, post_id):
    # traer el post con el id, si no lo encuentra error 404
    post = get_object_or_404(post, pk=post_id)
    ctx = {"post" :post}
    return render(request, "publicaciones/publicacion_detail", ctx)
    '''
