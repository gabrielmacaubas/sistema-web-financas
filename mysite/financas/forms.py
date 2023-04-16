from django import forms
from .models import Receita, Filtro


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


class FiltroForm(forms.ModelForm):
    class Meta:
        model = Filtro
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)'}
                ),
            'min': forms.NumberInput(attrs={'placeholder': '0.00'}),
            'max': forms.NumberInput(attrs={'placeholder': '0.00'}),
        }
