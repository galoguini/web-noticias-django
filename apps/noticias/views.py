from django.shortcuts import render

# Create your views here.

def home_noticias(request):
    return render(request, 'noticias/home.html')
