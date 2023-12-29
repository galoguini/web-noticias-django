from django.shortcuts import render
from django.views.generic import ListView
from apps.noticias.models import Noticia, Categoria

class HomeView(ListView):
    model = Noticia
    template_name = 'home.html'
    context_object_name = 'home_principal_n'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = Categoria.objects.all()
        noticias_por_categoria = {categoria: Noticia.objects.filter(categoria=categoria)[:2] for categoria in categorias}
        context['noticias_por_categoria'] = noticias_por_categoria
        return context

def about(request):
    return render(request, 'about.html')
