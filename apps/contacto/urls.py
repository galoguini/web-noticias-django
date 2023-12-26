from django.urls import path
from . import views

app_name = 'contactos'

urlpatterns = [
    path('', views.ContactoUsuario.as_view(), name= 'contacto'),
]
