from typing import Any
from django.shortcuts import render
from .forms import ContactoForm
from django.contrib import messages 
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class ContactoUsuario(CreateView):
    template_name = 'contactos/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Consulta enviada.')
        return super().form_valid(form)
    
    def contacto(request):
    # Lógica de la vista de la página de contacto
        return render(request, 'contacto.html')
