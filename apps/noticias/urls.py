from django.urls import path
from . import views

app_name = 'noticias' # nombre app:nombre path

urlpatterns = [
    path('', views.home_noticias, name='home_noticias'),
]