from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from apps.noticias.models import Noticia
from django.contrib.auth.decorators import login_required
from .forms import FotoPerfilForm, EditarNombreForm, EditarEmailForm, EditarUsuarioForm, EditarContraseñaForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

def terminos_condiciones(request):
    return render(request, 'usuarios/term_cond.html')

class ResetContraseñaView(PasswordResetView):
    template_name = 'usuarios/reset_contraseña.html'
    email_template_name = 'usuarios/reset_envio_email.html'
    success_url = reverse_lazy('usuarios:reset_contraseña_enviado')

class ResetContraseñaEnviadoView(PasswordResetDoneView):
    template_name = 'usuarios/reset_contraseña_enviado.html'

class ResetContraseñaConfirmacionView(PasswordResetConfirmView):
    template_name = 'usuarios/reset_contraseña_confirmacion.html'
    success_url = reverse_lazy('usuarios:reset_contraseña_completo')

class ResetContraseñaCompletoView(PasswordResetCompleteView):
    template_name = 'usuarios/reset_contraseña_completo.html'

def login(request):
    return render(request, 'usuarios/login.html')

class registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('usuarios:login')
    template_name = 'usuarios/registro.html'

def perfil(request, username):
    try:
        user = User.objects.get(username=username)
        noticias = Noticia.objects.filter(usuario=user)
    except User.DoesNotExist:
        raise Http404("Usuario no existe")
    
    if request.user.username == username:
        return render(request, 'usuarios/perfil.html', {'user': user, 'noticias': noticias})
    elif request.user.username != username:
        return render(request, 'usuarios/perfil.html', {'user': user, 'noticias': noticias})

@login_required
def update_foto_perfil(request):
    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil', request.user.username)
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
            return redirect('usuarios:perfil', request.user.username)
    else:
        form = EditarNombreForm(instance=request.user)
    return render(request, 'usuarios/editar_nombre.html', {'form': form})

@login_required
def editar_email(request):    
    if request.method == 'POST':
        form = EditarEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu email ha sido actualizado.')
            return redirect('usuarios:perfil', request.user.username)
    else:
        form = EditarEmailForm(instance=request.user)
    return render(request, 'usuarios/editar_email.html', {'form': form})

@login_required
def editar_usuario(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu nombre de usuario ha sido actualizado.')
            return redirect('usuarios:perfil', request.user.username)
    else:
        form = EditarUsuarioForm(instance=request.user)
    return render(request, 'usuarios/editar_usuario.html', {'form': form})

@login_required
def editar_contraseña(request):
    if request.method == 'POST':
        form = EditarContraseñaForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu contraseña ha sido actualizada.')
            return redirect('usuarios:perfil', request.user.username)
    else:
        form = EditarContraseñaForm(instance=request.user)
    return render(request, 'usuarios/editar_contraseña.html', {'form': form})

