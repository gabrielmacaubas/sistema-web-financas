# Generated by Django 4.2 on 2023-04-16 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_alter_receita_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='descricao',
            field=models.CharField(blank=True, max_length=100, verbose_name='Descrição'),
        ),
    ]
