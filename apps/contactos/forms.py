from django import forms
from .models import Contactos

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']
        labels = {
            'nombre_apellido': 'Nombre y Apellido',
            'email': 'Correo electrónico',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
        }
        help_texts = {
            'nombre_apellido': 'Ingrese su nombre y apellido para que podamos conocerlo.',
            'email': 'Ingrese un correo electrónico válido con el cuál podremos contactarnos.',
            'asunto': 'Ingrese el asunto del mensaje.',
            'mensaje': 'Ingrese su mensaje aquí.',
        }



