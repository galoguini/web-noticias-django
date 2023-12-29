from django.shortcuts import render, HttpResponseRedirect
from apps.noticias.models import Noticia
from django.views.generic import DeleteView, UpdateView
from .models import Comentario
from django.urls import reverse_lazy
from .forms import Form_Modificacion
from django.http import HttpResponseRedirect, HttpResponseBadRequest 
from django.utils import timezone
# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from apps.noticias.models import Noticia

def Agregar_Comentario(request, pk):
    texto = request.POST.get('comentario', None)

    if not texto or not texto.strip():
        mensaje = "¡Ups! Parece que olvidaste escribir tu comentario. Por favor, asegúrate de ingresar un comentario válido antes de enviarlo."
        return HttpResponse(f'<p>{mensaje}</p><p><a href="{reverse_lazy("noticias:detalle_noticia", kwargs={"pk": pk})}">Volver al detalle de noticias</a></p>')

    noticia = Noticia.objects.get(pk=pk)
    usuario = request.user 
    Comentario.objects.create(texto=texto, usuario=usuario, noticia=noticia)
    return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticia', kwargs={'pk': pk}))

class BorrarComentario(DeleteView):
	model = Comentario
 
	def get_success_url(self):
		return reverse_lazy('noticias:detalle_noticia', kwargs={'pk': self.object.noticia.pk})
    
class ModificaComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'comentarios/modificar.html'
 
	def get_success_url(self):         
		return reverse_lazy('noticias:detalle_noticia', kwargs={'pk': self.object.noticia.pk})

	def form_valid(self, form):
		form.instance.modificado = timezone.now()
		return super().form_valid(form)