from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

# Create your views here.
class registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'registro.html'
	# template_name = 'usuarios/registro.html' #dsp move el registro a la carpeta usuarios en template