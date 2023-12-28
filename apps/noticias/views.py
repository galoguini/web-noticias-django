from django.http import HttpResponseForbidden
from typing import Any

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Noticia, Categoria
from apps.comentarios.models import Comentario
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia

#Controla si el usuario está logeado
from django.contrib.auth.mixins import LoginRequiredMixin #en clases
from django.contrib.auth.decorators import login_required #en funciones
from django.contrib.auth.decorators import user_passes_test

#Controla si el usuario es staff
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required

def Home_Noticias(request):
    contexto = {}
    cat = Categoria.objects.all()
    contexto['categorias'] = cat

    filtro_categoria = request.GET.get('categoria', None)
    orden_fecha = request.GET.get('orden')
    orden_titulo = request.GET.get('titulo')
    filtro_titulo = request.GET.get('search', None)

    todas = Noticia.objects.all()

    if filtro_categoria and filtro_categoria != '0':
        todas = todas.filter(categoria__id=filtro_categoria)

        if orden_fecha == 'asc':
            todas = todas.order_by('creado')
        elif orden_fecha == 'desc':
            todas = todas.order_by('-creado')

        if orden_titulo == 'asc':
            todas = todas.order_by('titulo')
        elif orden_titulo == 'desc':
            todas = todas.order_by('-titulo')

        if filtro_titulo:
            todas = todas.filter(
                Q(titulo__icontains=filtro_titulo)
            )

    else:
        if orden_fecha == 'asc':
            todas = todas.order_by('creado')
        elif orden_fecha == 'desc':
            todas = todas.order_by('-creado')

        if orden_titulo == 'asc':
            todas = todas.order_by('titulo')
        elif orden_titulo == 'desc':
            todas = todas.order_by('-titulo')

        if filtro_titulo:
            todas = todas.filter(
                Q(titulo__icontains=filtro_titulo)
            )

    contexto['noticias'] = todas
    return render(request, 'noticias/home_noticias.html', contexto)

class Home_Noticias_clase(ListView):
    model = Noticia
    template_name = 'noticias/home.html'
    context_object_name = 'noticias'

class Cargar_noticia(LoginRequiredMixin, CreateView):
    model = Noticia
    template_name = 'noticias/cargar_noticia.html'
    form_class = Formulario_Noticia
    success_url = reverse_lazy('noticias:home_noticias')

    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user 
        return super().form_valid(form)

@login_required
def Modificar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    if noticia.usuario != request.user and not request.user.is_staff:
        return HttpResponseForbidden("No tienes permiso para modificar esta noticia.")

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

class Borrar_noticia(LoginRequiredMixin, DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:home_noticias')

    def dispatch(self, request, *args, **kwargs):
        noticia = self.get_object()

        if noticia.usuario == self.request.user or self.request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("No tienes permiso para eliminar esta noticia.")

