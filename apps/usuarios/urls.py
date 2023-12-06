from django.urls import path
from . import views
from django.contrib.auth import views as auth

app_name = 'usuarios' # nombre app:nombre path

urlpatterns = [
    # path('login/',auth.LoginView.as_view(template_name='login.html'),name='login'),
    # path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    # path('logout/',auth.LogoutView.as_view(),name="logout"),

    path('registro/', views.registro.as_view(), name="registro_usuario"),
]