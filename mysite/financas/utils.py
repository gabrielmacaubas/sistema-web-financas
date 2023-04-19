import csv
from .forms import FiltroDespesaForm, FiltroReceitaForm
from .models import Receita, Despesa


def filtrar(objetos, form, type):
    if type == Receita:
        form_type = FiltroReceitaForm

    else:
        form_type = FiltroDespesaForm

    if len(form) != 0:
        if form['min'] != '' or form['max'] != '':
            min = form['min']
            max = form['max']    
            objetos = filtrar_valor(min, max, objetos)

        if form['categoria'] != '':
            categoria = form['categoria']
            objetos = filtrar_categoria(categoria, objetos)
        
        if form['data'] != '':
            data = form['data']
            objetos = filtrar_data(data, objetos)
        
        form.pop('csrfmiddlewaretoken')

        form = form_type(initial=form)

    else:
        form = form_type()
    
    return (form, objetos)


def criar(form, type):
    valido = duplicidade_validation(
        form['valor'], 
        form['data'],
        form['categoria'],
        type
        )

    if valido:
        type.objects.create(
            valor = form['valor'],
            data = form['data'],
            descricao = form['descricao'],
            categoria = form['categoria'],
            comprovante = form['comprovante']
            )


def alterar(object, form, type):
    object.valor = form['valor']
    object.data = form['data']
    object.descricao = form['descricao']
    object.categoria = form['categoria']
    object.comprovante = form['comprovante']
    valido = duplicidade_validation(
        form['valor'], 
        form['data'], 
        form['categoria'],
        type
        )

    if valido:
        object.save()


def filtrar_valor(min, max, objetos): 
    
    if min == '':
        min = "0.00"

    min = float(min.replace(',', '.'))

    if max == '':
        objetos = objetos.filter(valor__gte=min)

    else:
        max = float(max.replace(',', '.'))
        objetos = objetos.filter(valor__gte=min)
        objetos = objetos.filter(valor__lte=max)

    return objetos


def filtrar_categoria(categoria, objetos):
    objetos = objetos.filter(categoria=categoria)

    return objetos


def filtrar_data(data, objetos):
    objetos = objetos.filter(data=data)
    return objetos


def gerar_arquivo(objetos, type):
    if type == 'receita':
        arquivo_nome = 'receitas.csv'
    
    else:
        arquivo_nome = 'despesas.csv'

    writer = csv.writer(open(arquivo_nome, 'w'))
    writer.writerow(['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'])

    for objeto in objetos:
        writer.writerow([objeto.valor, objeto.data, objeto.descricao, objeto.categoria, objeto.comprovante])
    
    return arquivo_nome


def duplicidade_validation(valor, data, categoria, type):
    if type == Receita:
        dados = type.objects.filter(valor=valor)

    else:
        dados = type.objects.filter(valor=valor)

    dados = dados.filter(data=data)
    dados = dados.filter(categoria=categoria)

    if len(dados) == 0:
        return True
    
    else:
        return False
