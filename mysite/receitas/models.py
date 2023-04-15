from django.db import models


class Receita(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=12)
    comprovante = models.FileField(null=False)
