from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias')
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=False, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Noticia.objects.get(pk=self.pk)
            if (orig.titulo != self.titulo or orig.contenido != self.contenido or 
                orig.imagen != self.imagen or orig.categoria != self.categoria):
                self.modificado = timezone.now()
        super(Noticia, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'
        ordering = ['-creado']