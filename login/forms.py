from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = '' # Establecer la ayuda de username en vacio
        self.fields['password1'].help_text = ''  # Establece la ayuda para la contraseña en vacío
        self.fields['password2'].help_text = ''  # Establece la ayuda para la confirmación de la contraseña en vacío

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']