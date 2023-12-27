from django.urls import reverse
from .models import Noticia

def noticia_aleatoria(request):
    noticia = Noticia.objects.order_by('?').first()
    noticia_url = reverse('noticias:detalle_noticia', args=[str(noticia.id)]) if noticia else ''
    return {'noticia_aleatoria': noticia, 'noticia_url': noticia_url}