# Generated by Django 4.2 on 2023-04-16 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0003_filtro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.CharField(max_length=10)),
                ('descricao', models.CharField(blank=True, max_length=100, verbose_name='Descrição')),
                ('categoria', models.CharField(choices=[('Casa', 'Casa'), ('Educação', 'Educação'), ('Eletrônicos', 'Eletrônicos'), ('Lazer', 'Lazer'), ('Saúde', 'Saúde'), ('Supermercado', 'Supermercado'), ('Transporte', 'Transporte'), ('Outros', 'Outros')], max_length=12)),
                ('comprovante', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FiltroDespesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.DecimalField(blank=True, decimal_places=2, help_text='R$', max_digits=10, null=True)),
                ('max', models.DecimalField(blank=True, decimal_places=2, help_text='R$', max_digits=10, null=True)),
                ('data', models.DateField(blank=True, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Educação', 'Educação'), ('Eletrônicos', 'Eletrônicos'), ('Lazer', 'Lazer'), ('Saúde', 'Saúde'), ('Supermercado', 'Supermercado'), ('Transporte', 'Transporte'), ('Outros', 'Outros')], max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FiltroReceita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.DecimalField(blank=True, decimal_places=2, help_text='R$', max_digits=10, null=True)),
                ('max', models.DecimalField(blank=True, decimal_places=2, help_text='R$', max_digits=10, null=True)),
                ('data', models.DateField(blank=True, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('Investimento', 'Investimento'), ('Presente', 'Presente'), ('Prêmio', 'Prêmio'), ('Salário', 'Salário'), ('Outros', 'Outros')], max_length=12, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Filtro',
        ),
    ]
