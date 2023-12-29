from django.urls import path
from . import views
from django.contrib.auth import views as auth
from .views import update_foto_perfil, ResetContraseñaView, ResetContraseñaEnviadoView, ResetContraseñaConfirmacionView, ResetContraseñaCompletoView
from django.urls import reverse_lazy

app_name = 'usuarios' # nombre app:nombre path

urlpatterns = [
    path('terminos_condiciones/', views.terminos_condiciones, name="term_cond"),
    path('registro/', views.registro.as_view(), name="registro_usuario"),
    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),
    path('perfil/<str:username>/', views.perfil, name="perfil"),
    path('editarFoto/', update_foto_perfil, name='update_foto_perfil'),
    path('editarNombre/', views.editar_nombre, name="editar_nombre"),
    path('editarContraseña/', views.editar_contraseña, name="editar_contraseña"),
    path('editarUsuario/', views.editar_usuario, name="editar_usuario"),
    path('editarEmail/', views.editar_email, name="editar_email"),
    path('reset_contraseña/', ResetContraseñaView.as_view(), name='reset_contraseña'),
    path('reset_contraseña_enviado/', ResetContraseñaEnviadoView.as_view(), name='reset_contraseña_enviado'),
    path('reset/<uidb64>/<token>/', ResetContraseñaConfirmacionView.as_view(), name='reset_contraseña_confirmacion'),
    path('reset_contraseña_completo/', ResetContraseñaCompletoView.as_view(), name='reset_contraseña_completo'),
]
