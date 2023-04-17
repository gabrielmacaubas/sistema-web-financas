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
        'type': 'receita'
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
        'type': 'despesa'
    }

    return HttpResponse(template.render(context, request))


def criar_receita(request):
    form_data = request.POST
    valido = duplicidade_validation(
        form_data['valor'], 
        form_data['data'],
        form_data['categoria'],
        'receita'
        )

    if valido:
        Receita.objects.create(
            valor = form_data['valor'],
            data = form_data['data'],
            descricao = form_data['descricao'],
            categoria = form_data['categoria'],
            comprovante = form_data['comprovante']
            )
    
    return redirect('receitas')


def criar_despesa(request):
    form_data = request.POST
    valido = duplicidade_validation(
        form_data['valor'], 
        form_data['data'],
        form_data['categoria'],
        'despesa'
        )

    if valido:
        Despesa.objects.create(
            valor = form_data['valor'],
            data = form_data['data'],
            descricao = form_data['descricao'],
            categoria = form_data['categoria'],
            comprovante = form_data['comprovante']
            )
    
    return redirect('despesas')
        

def alterar_receita(request, id):      
    if request.method == 'POST':
        form_data = request.POST
        receita = Receita.objects.get(pk=id)
        print(receita)
        receita.valor = form_data['valor']
        receita.data = form_data['data']
        receita.descricao = form_data['descricao']
        receita.categoria = form_data['categoria']
        receita.comprovante = form_data['comprovante']
        valido = duplicidade_validation(
            form_data['valor'], 
            form_data['data'], 
            form_data['categoria'],
            'receita'
            )

        if valido:
            receita.save()

        return redirect('receitas')
    
    receita_antigo = Receita.objects.get(pk=id).__dict__
    receita_antigo.pop('_state')
    receita_antigo.pop('comprovante')
    template = loader.get_template('alterar_receita.html')
    context = {
        'form': ReceitaForm(initial=receita_antigo),
        'id': id
    }

    return HttpResponse(template.render(context, request))


def alterar_despesa(request, id):      
    if request.method == 'POST':
        form_data = request.POST
        despesa = Despesa.objects.get(pk=id)
        despesa.valor = form_data['valor']
        despesa.data = form_data['data']
        despesa.descricao = form_data['descricao']
        despesa.categoria = form_data['categoria']
        despesa.comprovante = form_data['comprovante']
        valido = duplicidade_validation(
            form_data['valor'], 
            form_data['data'], 
            form_data['categoria'],
            'despesa'
            )

        if valido:
            despesa.save()

        return redirect('despesas')
    
    despesa_antigo = Despesa.objects.get(pk=id).__dict__
    despesa_antigo.pop('_state')
    despesa_antigo.pop('comprovante')
    template = loader.get_template('alterar_despesa.html')
    context = {
        'form': DespesaForm(initial=despesa_antigo),
        'id': id
    }

    return HttpResponse(template.render(context, request))


def remover(request):
    args = list(request.POST.keys())[1].split(' ')
    id = args[0]
    type = args[1]
    
    if type == 'receita':
        destino = 'receitas'
        objeto = Receita

    else:
        destino = 'despesas'
        objeto = Despesa

    objeto = objeto.objects.get(pk=id)
    objeto.delete()

    return redirect(destino)
  

def exportar_receita(request):  
    receitas = Receita.objects.all()
    arquivo_nome = gerar_arquivo(receitas, 'receita')

    with open(arquivo_nome, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(arquivo_nome)
        
        return response


def exportar_despesa(request):

    despesas = Despesa.objects.all()
    arquivo_nome = gerar_arquivo(despesas, 'despesa')

    with open(arquivo_nome, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(arquivo_nome)
        
        return response
