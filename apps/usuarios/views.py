from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from .forms import FotoPerfilForm, EditarNombreForm

# Create your views here.
def login(request):
    return render(request, 'usuarios/login.html')

class registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('usuarios:login')
    template_name = 'usuarios/registro.html'

def perfil(request):
	return render(request, 'usuarios/perfil.html')

def editar_perfil(request):
    return render(request, 'usuarios/editar_perfil.html')

@login_required
def update_foto_perfil(request):
    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil')
        else:
            print(form.errors)
    else:
        form = FotoPerfilForm(instance=request.user.userprofile)
    return render(request, 'usuarios/perfil.html', {'form': form})

@login_required
def editar_nombre(request):
    if request.method == 'POST':
        form = EditarNombreForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('usuarios:perfil')
    else:
        form = EditarNombreForm(instance=request.user)
    return render(request, 'usuarios/editar_nombre.html', {'form': form})

