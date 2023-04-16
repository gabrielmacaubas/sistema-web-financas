from django.db import models

RECEITA_CHOICES = (
    ('Investimento', 'Investimento'),
    ('Presente', 'Presente'),
    ('Prêmio', 'Prêmio'),
    ('Salário', 'Salário'),
    ('Outros', 'Outros')
)
DESPESA_CHOICES = (
    ('Casa', 'Casa'),
    ('Educação', 'Educação'),
    ('Eletrônicos', 'Eletrônicos'),
    ('Lazer', 'Lazer'),
    ('Saúde', 'Saúde'),
    ('Supermercado', 'Supermercado'),
    ('Transporte', 'Transporte'),
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
        choices=RECEITA_CHOICES
        )
    comprovante = models.FileField(
        null=False, 
        blank=False
        )
    

class Despesa(models.Model):
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
        choices=DESPESA_CHOICES
        )
    comprovante = models.FileField(
        null=False, 
        blank=False
        )
    

class FiltroReceita(models.Model):
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
        choices=RECEITA_CHOICES,
        blank=True,
        null=True
        )


class FiltroDespesa(models.Model):
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
        choices=DESPESA_CHOICES,
        blank=True,
        null=True
        )

