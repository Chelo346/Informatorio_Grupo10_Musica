from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2',
                  'email', 'telefono', 'domicilio']
        
        labels = {
            'first_name': 'Ingresa tu nombre',
            'last_name':'Ingresa tu apellido',
            'username': 'Ingresa tu Nick'
        }