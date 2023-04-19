from django import forms
from .models import *

# constrói as classes de formulário para cada modelo

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"
        # adiciona funcionalidade de calendário e placeholder ao formulário
        widgets = {
            'data': 
            forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)'}),
            'valor': forms.NumberInput(attrs={'placeholder': '0.00'}),
        }


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = "__all__"
        widgets = {
            'data': 
            forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)'}),
            'valor': forms.NumberInput(attrs={'placeholder': '0.00'}),
        }

# constrói as classes de formulário para cada modelo de filtro

class FiltroReceitaForm(forms.ModelForm):
    class Meta:
        model = FiltroReceita
        fields = '__all__'
        # adiciona funcionalidade de calendário e placeholder ao formulário
        widgets = {
            'data': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)'}
                ),
            'min': forms.NumberInput(attrs={'placeholder': '0.00'}),
            'max': forms.NumberInput(attrs={'placeholder': '0.00'}),
        }


class FiltroDespesaForm(forms.ModelForm):
    class Meta:
        model = FiltroReceita
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)'}
                ),
            'min': forms.NumberInput(attrs={'placeholder': '0.00'}),
            'max': forms.NumberInput(attrs={'placeholder': '0.00'}),
        }
