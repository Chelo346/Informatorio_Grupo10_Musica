from django.forms import ModelForm
from .models import Publicaciones

class CrearPublicacionForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria','titulo', 'subtitulo','post']
        
        labels = {
            'categoria': 'Selecciona una Categoria',
            'titulo':'',
            'subtitulo':'',
            'post':''
        }