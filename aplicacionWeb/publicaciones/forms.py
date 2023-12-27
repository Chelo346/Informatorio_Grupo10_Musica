from django.forms import ModelForm
from .models import Publicaciones

class CrearPublicacionForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria','titulo', 'subtitulo','post', 'imagen']
        
        labels = {
            'categoria': 'Selecciona una Categoria',
            'titulo':'',
            'subtitulo':'',
            'post':'',
            'imagen':'',
        }

'''CLASE CREAR COMENTARIO (REVISAR)

class CrearComentarioForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['comentario']
        
        labels = {
            'comentario': 'Realiza un comentario',
        }
'''