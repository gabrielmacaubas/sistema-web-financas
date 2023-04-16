from django import forms
from .models import *


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"
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


class FiltroReceitaForm(forms.ModelForm):
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
