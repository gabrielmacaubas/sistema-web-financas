import shutil
from tempfile import NamedTemporaryFile
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Receita
from .forms import ReceitaForm, FiltroForm
import csv
import datetime
import pandas as pd

def receitas_view(request):
    receitas = Receita.objects.all().order_by('data').reverse()

    """
    else:
        filtro_form = FiltroForm(request.GET)
        receitas = ler_receitas()

        if len(filtro_form.data) != 0:
            if filtro_form.data['min'] != '' or filtro_form.data['max'] != '':
                min = filtro_form.data['min']
                max = filtro_form.data['max']

                receitas = filtrar_valor(min, max, receitas)
    """

    template = loader.get_template('cadastrar_receitas.html')
    context = {
        'form': ReceitaForm(),
        'filtroForm': FiltroForm(),
        'header': ['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante', ''],
        'receitas': receitas
    }

    return HttpResponse(template.render(context, request))


def criar_receita(request):
    form_data = ReceitaForm(request.POST)

    Receita.objects.create(
        valor= form_data.data['valor'],
        data= form_data.data['data'],
        descricao= form_data.data['descricao'],
        categoria= form_data.data['categoria'],
        comprovante= form_data.data['comprovante']
    )
    
    return redirect('/receitas')


def alterar(request, id):
    
    if request.method == 'POST':
        form_data = ReceitaForm(request.POST)
        receita = Receita.objects.get(pk=id)
        receita.valor = form_data.data['valor']
        receita.data = form_data.data['data']
        receita.descricao = form_data.data['descricao']
        receita.categoria = form_data.data['categoria']
        receita.comprovante = form_data.data['comprovante']

        receita.save()

        return redirect('/receitas')

    receita_antigo = Receita.objects.get(pk=id).__dict__
    receita_antigo.pop('_state')
    template = loader.get_template('alterar_receita.html')
    context = {
        'form': ReceitaForm(initial=receita_antigo),
        'id': id
    }

    return HttpResponse(template.render(context, request))


def remover(request):
    id = list(request.POST.keys())[1]
    receita = Receita.objects.get(pk=id)
    receita.delete()

    return redirect('/receitas')
"""
def filtrar_valor(min, max, receitas):  
    if min == '':
        min = 0
    
    receitas_novo = []
    min = int(min)

    if max == '':
        for receita in receitas:
            if int(receita["valor"]) >= min:
                receitas_novo.append(receita)

        return receitas_novo

    else:
        max = int(max)

        for receita in receitas:
            if int(receita["valor"]) >= min and int(receita["valor"]) <= max:
                receitas_novo.append(receita)

        return receitas_novo
"""        
