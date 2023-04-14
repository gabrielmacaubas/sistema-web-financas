from django.http import HttpResponse
from django.template import loader
from .models import Receita
from .forms import FormularioReceitas
import csv


def receitas_view(request):
    if request.method == 'POST':
        form = FormularioReceitas(request.POST)
        receita = Receita(
            valor=form.data['valor'],
            data=form.data['data'],
            descricao=form.data['descricao'],
            categoria=form.data['categoria'],
            comprovante=form.data['comprovante_opcional']
        )

        salvar_receita(receita)
    
    template = loader.get_template('cadastrar_receitas.html')
    context = {
        'form': FormularioReceitas(),
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


def carregar_receitas():
    f = open('./receitas.csv', 'r')
    reader = csv.DictReader(f)
    receitas = []

    for row in reader:
        receitas.append(row)

    f.close()
    return receitas