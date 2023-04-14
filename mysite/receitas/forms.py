from django import forms
from .models import Receita



class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"
        widgets = {
            'data': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)', 'class': 'form-control'}
            )
        }


class FiltroForm(forms.Form):
    min = forms.DecimalField(max_digits=10, decimal_places=2, help_text='R$', required=False)
    max = forms.DecimalField(max_digits=10, decimal_places=2, help_text='R$', required=False)
    #data
    #categoria

"""
class FormularioReceitas(forms.Form):
    valor = forms.DecimalField(max_digits=10, decimal_places=2)
    data = forms.CharField(max_length=10)
    descricao = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=12)
    comprovante_opcional = forms.FileField(required=False)
"""