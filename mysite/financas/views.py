from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Receita
from .forms import ReceitaForm, FiltroForm
from .utils import *


def receitas_view(request):
    receitas = Receita.objects.all().order_by('data').reverse()
    filtro_form = FiltroForm(request.GET)

    if len(filtro_form.data) != 0:
        filtro_form = filtro_form.data
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
        
        filtro_form = filtro_form.dict()
        filtro_form.pop('csrfmiddlewaretoken')
        filtro_form = FiltroForm(initial=filtro_form)


    template = loader.get_template('cadastrar_receitas.html')
    
    context = {
        'form': ReceitaForm(),
        'filtroForm': filtro_form,
        'header': ['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'],
        'receitas': receitas
    }

    return HttpResponse(template.render(context, request))


def criar_receita(request):
    form_data = ReceitaForm(request.POST)

    Receita.objects.create(
        valor = form_data.data['valor'],
        data = form_data.data['data'],
        descricao = form_data.data['descricao'],
        categoria = form_data.data['categoria'],
        comprovante = form_data.data['comprovante']
    )
    
    return redirect('receitas')


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


def remover(request):
    id = list(request.POST.keys())[1]
    receita = Receita.objects.get(pk=id)
    receita.delete()

    return redirect('receitas')
  