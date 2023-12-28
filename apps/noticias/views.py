from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404, render, redirect
from .models import Noticia, Categoria
from .forms import Formulario_Modificar_Noticia

from apps.comentarios.models import Comentario

from .models import Noticia
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia

class Home_Noticias_clase(ListView):
    model = Noticia
    template_name = 'noticias/home.html'
    context_object_name = 'noticias'
    
class Cargar_noticia(CreateView):
    model = Noticia
    template_name = 'noticias/cargar_noticia.html'
    form_class = Formulario_Noticia
    success_url = reverse_lazy('noticias:home_noticias')

    def form_valid(self, form):
        noticia = form.save(commit=False)
        noticia.usuario = self.request.user
        return super(Cargar_noticia, self).form_valid(form)

def Modificar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        form = Formulario_Modificar_Noticia(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias:home_noticias')
    else:
        form = Formulario_Modificar_Noticia(instance=noticia)

    return render(request, 'noticias/modificar_noticia.html', {'form': form, 'noticia': noticia, 'categorias': categorias})

def Detalle_noticia(request, pk):
    ctx = {}
    n = Noticia.objects.get(pk=pk)
    ctx['noticia'] = n 
    
    com = Comentario.objects.filter(noticia=n)  # Cambia 'noticias' a 'noticia'
    ctx['comentarios'] = com
    return render(request, 'noticias/detalle_noticia.html', ctx)


class Borrar_noticia(DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:home_noticias')

