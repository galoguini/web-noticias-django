from django.apps import AppConfig


class NoticiasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.noticias' # agregar el "apps." adelante para que funcione
