from django.shortcuts import render
from apps.noticias.models import Noticia
from django.views.generic import ListView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

