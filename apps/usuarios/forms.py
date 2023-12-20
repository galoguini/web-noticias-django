from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import UserProfile

class EditarNombreForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        error_messages={
            'required': '⚠️Este campo es requerido.',
            'invalid': '⚠️Introduzca una dirección de email válida.',
        }
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('⚠️El nombre de usuario ya existe.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')    
        if User.objects.filter(email=email).exists():
            raise ValidationError('⚠️Ya existe un usuario con ese correo electrónico.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError('⚠️Las contraseñas no coinciden.')
        return password2