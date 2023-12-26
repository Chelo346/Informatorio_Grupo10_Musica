from django.forms import ModelForm
from .models import Publicaciones

class CrearPublicacionForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria','imagen','titulo', 'subtitulo','post']
        
        labels = {
            'categoria': 'Selecciona una Categoria',
            'imagen':'',
            'titulo':'',
            'subtitulo':'',
            'post':''
        }