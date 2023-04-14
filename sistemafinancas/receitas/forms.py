from django import forms


class FormularioReceitas(forms.Form):
    valor = forms.DecimalField(max_digits=10, decimal_places=2)
    data = forms.CharField(max_length=10)
    descricao = forms.CharField(max_length=100, required=False)
    categoria = forms.CharField(max_length=12)
    comprovante_opcional = forms.FileField()
