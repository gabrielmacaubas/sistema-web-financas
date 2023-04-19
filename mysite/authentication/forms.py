from django import forms
from django.contrib.auth.models import User


class UserEntrarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None
        }
        labels = {
            'username': 'Usuário',
            'password': 'Senha'
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'label': 'Senha'}),
        }


class UserCadastrarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {
            'username': None
        }
        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha'
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'label': 'Senha'}),
        }
