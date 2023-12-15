from django.shortcuts import render
from django.views.generic import ListView

from .models import Noticia

class Home_Noticias_clase(ListView):
    model = Noticia
    template_name = 'noticias/home.html'
    context_object_name = 'noticias'
    
