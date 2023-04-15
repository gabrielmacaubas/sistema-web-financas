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
    receitas = []

    if request.method == 'POST':
        form = ReceitaForm(request.POST)

        receita = Receita(
            valor=form.data['valor'],
            data=form.data['data'],
            descricao=form.data['descricao'],
            categoria=form.data['categoria'],
            comprovante=form.data['comprovante']
        )

        criar_receita(receita)
        receitas = ler_receitas()

    else:
        filtro_form = FiltroForm(request.GET)
        receitas = ler_receitas()

        if len(filtro_form.data) != 0:
            if filtro_form.data['min'] != '' or filtro_form.data['max'] != '':
                min = filtro_form.data['min']
                max = filtro_form.data['max']

                receitas = filtrar_valor(min, max, receitas)


    template = loader.get_template('cadastrar_receitas.html')
    context = {
        'form': ReceitaForm(),
        'filtroForm': FiltroForm(),
        'header': ['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante', ''],
        'receitas': receitas
    }

    return HttpResponse(template.render(context, request))


def criar_receita(receita: Receita):
    file = pd.read_csv('./receitas.csv', encoding='UTF-8', sep=',', usecols=["id"])
    id = file.iloc[-1][0] + 1
    dados = [
        id,
        receita.valor,
        receita.data,
        receita.descricao,
        receita.categoria,
        receita.comprovante
    ]
    file = open('./receitas.csv', 'a')
    writer = csv.writer(file)

    writer.writerow(dados)
    file.close()
    

def ler_receitas():
    f = open('./receitas.csv', 'r')
    reader = csv.DictReader(f)
    receitas = []

    for row in reader:
        receitas.append(row)

    f.close()

    return reversed(merge_sort(receitas))


def alterar(request, id):
    receita_antigo = buscar_receita(id)
    template = loader.get_template('alterar_receita.html')

    context = {
        'form': ReceitaForm(initial=receita_antigo),
        'id': id
    }

    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        receita = Receita(
            valor=form.data['valor'],
            data=form.data['data'],
            descricao=form.data['descricao'],
            categoria=form.data['categoria'],
            comprovante=form.data['comprovante']
        )
        fields = ['id', 'valor', 'data', 'descricao', 'categoria', 'comprovante']
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open('./receitas.csv', 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['id'] == str(id):
                    print('updating row', row['id'])
                    row['valor'] = receita.valor
                    row['data'] = receita.data
                    row['descricao'] = receita.descricao
                    row['categoria'] = receita.categoria
                    row['comprovante'] = receita.comprovante
                    
                row = {'id': row['id'], 'valor': row['valor'], 'data': row['data'], 'descricao': row['descricao'], 
                        'categoria': row['categoria'], 'comprovante': row['comprovante']}
                writer.writerow(row)

        shutil.move(tempfile.name, './receitas.csv')

        df = pd.read_csv('./receitas.csv', encoding='UTF-8')
        df.loc[df['id'] == int(id), 'valor'] = receita.valor
        return redirect('/receitas')

    return HttpResponse(template.render(context, request))


def merge_sort(receitas):
    if len(receitas) > 1:
        mid = len(receitas)//2
        L = receitas[:mid]
        R = receitas[mid:]
 
        merge_sort(L)
        merge_sort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            dataA = L[i]["data"]  
            dataB = R[j]["data"]
            dataA = datetime.datetime(int(dataA[0:4]), int(dataA[5:7]), int(dataA[8:10]))
            dataB = datetime.datetime(int(dataB[0:4]), int(dataB[5:7]), int(dataB[8:10]))

            if dataA <= dataB:
                receitas[k] = L[i]
                i += 1
            else:
                receitas[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            receitas[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            receitas[k] = R[j]
            j += 1
            k += 1
    return receitas


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
         

def buscar_receita(id):
    receitas = ler_receitas()

    for receita in receitas:
        if int(receita['id']) == id:
            return receita

    return None
