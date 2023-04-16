from django import forms
from .models import Receita


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"
        widgets = {
            'data': 
            forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)', 'class': 'h5'})
        }


class FiltroForm(forms.Form):
    min = forms.DecimalField(
        max_digits=10,
        decimal_places=2, 
        help_text='R$', 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': '0.00'}
    ))
    max = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text='R$', 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': '0.00'}
    ))
    data = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)', 'class': 'h5'})
    )
    categoria = forms.CharField(
        max_length=12, 
        required=False
    )




