import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Receita
from .forms import *
from .utils import *


def receitas_view(request):
    receitas = Receita.objects.all().order_by('data').reverse()
    filtro_form = request.GET.dict()

    if len(filtro_form) != 0:
        if filtro_form['min'] != '' or filtro_form['max'] != '':
            min = filtro_form['min']
            max = filtro_form['max']    
            receitas = filtrar_valor(min, max, receitas)

        if filtro_form['categoria'] != '':
            categoria = filtro_form['categoria']
            receitas = filtrar_categoria(categoria, receitas)
        
        if filtro_form['data'] != '':
            data = filtro_form['data']
            receitas = filtrar_data(data, receitas)
        
        filtro_form.pop('csrfmiddlewaretoken')
        filtro_form = FiltroReceitaForm(initial=filtro_form)

    else:
        filtro_form = FiltroReceitaForm()

    template = loader.get_template('cadastrar_receitas.html')
    context = {
        'form': ReceitaForm(),
        'filtroForm': filtro_form,
        'header': ['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'],
        'receitas': receitas,
        'type': 'r'
    }

    return HttpResponse(template.render(context, request))


def despesas_view(request):
    despesas = Despesa.objects.all().order_by('data').reverse()
    filtro_form = request.GET.dict()

    if len(filtro_form) != 0:
        if filtro_form['min'] != '' or filtro_form['max'] != '':
            min = filtro_form['min']
            max = filtro_form['max']    
            despesas = filtrar_valor(min, max, despesas)

        if filtro_form['categoria'] != '':
            categoria = filtro_form['categoria']
            despesas = filtrar_categoria(categoria, despesas)
        
        if filtro_form['data'] != '':
            data = filtro_form['data']
            despesas = filtrar_data(data, despesas)
        
        filtro_form.pop('csrfmiddlewaretoken')
        filtro_form = FiltroDespesaForm(initial=filtro_form)

    else:
        filtro_form = FiltroDespesaForm()

    filtro_form = FiltroDespesaForm()
    template = loader.get_template('cadastrar_despesas.html')
    context = {
        'form': DespesaForm(),
        'filtroForm': filtro_form,
        'header': ['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'],
        'despesas': despesas,
        'type': 'd'
    }

    return HttpResponse(template.render(context, request))


def criar(request, type):
    form_data = request.POST
    valido = duplicidade_validation(
        form_data['valor'], 
        form_data['data'],
        form_data['categoria'],
        type
        )
    
    if type == 'r':
        objeto = Receita
        destino = 'receitas'
    
    else:
        objeto = Despesa
        destino = 'despesas'


    if valido:
        objeto.objects.create(
            valor = form_data['valor'],
            data = form_data['data'],
            descricao = form_data['descricao'],
            categoria = form_data['categoria'],
            comprovante = form_data['comprovante']
            )
    
    return redirect(destino)


def alterar(request, type, id):
    if type == 'r':
        destino = 'receitas'
        objeto = Receita
        template = loader.get_template('alterar_receita.html')

    else:
        destino = 'despesas'
        objeto = Despesa
        template = loader.get_template('alterar_despesa.html')
        
    if request.method == 'POST':
        form_data = request.POST
        objeto = objeto.objects.get(pk=id)
        objeto.valor = form_data['valor']
        objeto.data = form_data['data']
        objeto.descricao = form_data['descricao']
        objeto.categoria = form_data['categoria']
        objeto.comprovante = form_data['comprovante']
        valido = duplicidade_validation(
            form_data['valor'], 
            form_data['data'], 
            form_data['categoria'],
            type
            )

        if valido:
            objeto.save()

        return redirect(destino)
    
    objeto_antigo = objeto.objects.get(pk=id).__dict__
    objeto_antigo.pop('_state')
    objeto_antigo.pop('comprovante')
    context = {
        'form': ReceitaForm(initial=objeto_antigo),
        'id': id
    }

    return HttpResponse(template.render(context, request))


def remover(request):
    args = list(request.POST.keys())[1].split(' ')
    id = args[0]
    type = args[1]
    
    if type == 'r':
        destino = 'receitas'
        objeto = Receita

    else:
        destino = 'despesas'
        objeto = Despesa

    objeto = objeto.objects.get(pk=id)
    objeto.delete()

    return redirect(destino)
  

def exportar(request, type):
    if type == 'r':
        objeto = Receita

    else:
        objeto = Despesa
        
    objetos = objeto.objects.all()
    arquivo_nome = gerar_arquivo(objetos, type)

    with open(arquivo_nome, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(arquivo_nome)
        
        return response
