from django.forms import ModelForm
from .models import Publicaciones

class CrearPublicacionForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria','titulo', 'subtitulo','post', 'imagen']
        
        labels = {
            'categoria': 'Selecciona una Categoria',
            'imagen':'',
            'titulo':'',
            'subtitulo':'',
            'post':'',
            'imagen':'',
        }