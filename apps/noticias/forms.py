from django import forms
from .models import Noticia

class Formulario_Noticia(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen', 'categoria']
        labels = {
            'titulo':'Título de la noticia.',
            'contenido':'Descripción de la noticia.',
            'imagen':'Imagen ilustrativa.',
            'categoria':'Categoría de la noticia.',
        }
        help_texts = {
            'titulo': 'Ingrese un título para la noticia.',
            'contenido': 'Ingrese una descripción para la noticia.',
            'imagen': 'Ingrese una imagen ilustrativa para la noticia.',
            'categoria': 'Ingrese la categoría de la noticia.',
        }

class Formulario_Modificar_Noticia(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen', 'categoria']
        labels = {
            'titulo':'Título de la noticia.',
            'contenido':'Descripción de la noticia.',
            'imagen':'Imagen ilustrativa.',
            'categoria':'Categoría de la noticia.',
        }
        help_texts = {
            'titulo': 'Ingrese un título para la noticia.',
            'contenido': 'Ingrese una descripción para la noticia.',
            'imagen': 'Ingrese una imagen ilustrativa para la noticia.',
            'categoria': 'Ingrese la categoría de la noticia.',
        }