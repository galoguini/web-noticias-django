from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

# Create your views here.
def login(request):
    return render(request, 'usuarios/login.html')

class registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('usuarios:login')
	template_name = 'usuarios/registro.html'

def perfil(request):
	return render(request, 'usuarios/perfil.html')