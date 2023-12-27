from django.contrib import admin
from .models import Contactos

# Register your models here.

@admin.register(Contactos)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_apellido', 'email', 'asunto', 'fecha')
    