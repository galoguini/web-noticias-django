from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.
def login(request):
    return render(request, 'usuarios/login.html')

class registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('usuarios:login')
    template_name = 'usuarios/registro.html'

def perfil(request):
	return render(request, 'usuarios/perfil.html')