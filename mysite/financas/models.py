from django.db import models

CATEGORIA_CHOICES = (
    ('Investimento', 'Investimento'),
    ('Presente', 'Presente'),
    ('Prêmio', 'Prêmio'),
    ('Salário', 'Salário'),
    ('Outros', 'Outros')
)


class Receita(models.Model):
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    data = models.CharField(max_length=10)
    descricao = models.CharField(
        max_length=100, 
        blank=True, 
        verbose_name='Descrição'
        )
    categoria = models.CharField(
        max_length=12,
        choices=CATEGORIA_CHOICES
        )
    comprovante = models.FileField(
        null=False, 
        blank=False
        )
    

class Filtro(models.Model):
    min = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text='R$', 
        blank=True,
        null=True
        )
    max = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text='R$', 
        blank=True,
        null=True
        )
    data = models.DateField(
        blank=True,
        null=True
        )
    categoria = models.CharField(
        max_length=12, 
        choices=CATEGORIA_CHOICES,
        blank=True,
        null=True
        )
