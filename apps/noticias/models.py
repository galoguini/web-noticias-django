from django.db import models

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
    modificado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'
        ordering = ['-creado']

    def __str__(self):
        return self.titulo
