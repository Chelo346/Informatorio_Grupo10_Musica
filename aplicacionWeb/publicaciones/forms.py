from django.forms import ModelForm
from .models import Publicaciones

class CrearPublicacionForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria','titulo', 'subtitulo','post', 'imagen']
        
        labels = {
            'categoria': 'Selecciona una Categoria',
            'titulo':'Titulo',
            'subtitulo':'Subtitulo',
            'post':'Posteo',
            'imagen':'Selecciona una Imagen',
        }
