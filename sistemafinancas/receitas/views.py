from django.http import HttpResponse
from django.template import loader
from .models import Receita
from .forms import ReceitaForm
import csv
import datetime


def receitas_view(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)

        receita = Receita(
            valor=form.data['valor'],
            data=form.data['data'],
            descricao=form.data['descricao'],
            categoria=form.data['categoria'],
            comprovante=form.data['comprovante']
        )

        salvar_receita(receita)
    
    template = loader.get_template('cadastrar_receitas.html')
    context = {
        'form': ReceitaForm(),
        'header': ['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'],
        'receitas': carregar_receitas()
    }


    return HttpResponse(template.render(context, request))


def salvar_receita(receita: Receita):
    dados = [
        receita.valor,
        receita.data,
        receita.descricao,
        receita.categoria,
        receita.comprovante
    ]

    f = open('./receitas.csv', 'a')
    writer = csv.writer(f)

    writer.writerow(dados)
    f.close()


def carregar_receitas(filtro=None):
    if (filtro == None):

        f = open('./receitas.csv', 'r')
        reader = csv.DictReader(f)
        receitas = []

        for row in reader:
            receitas.append(row)

        f.close()

        
        return reversed(merge_sort(receitas))


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
