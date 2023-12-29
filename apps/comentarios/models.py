from django.db import models
from django.contrib.auth.models import User 
from apps.noticias.models import Noticia
# Create your models here. 

class Comentario(models.Model):
    creado = models.DateTimeField(
        'creado',
        auto_now_add=True
    )
    modificado = models.DateTimeField(
        'modificado',
        auto_now_add=True
    )
    texto = models.TextField()
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
    modificado = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.texto

