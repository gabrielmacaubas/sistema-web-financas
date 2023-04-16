import csv
from .models import Receita, Despesa


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
    if type == 'r':
        arquivo_nome = 'receitas.csv'
    
    else:
        arquivo_nome = 'despesas.csv'

    writer = csv.writer(open(arquivo_nome, 'w'))
    writer.writerow(['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'])

    for objeto in objetos:
        writer.writerow([objeto.valor, objeto.data, objeto.descricao, objeto.categoria, objeto.comprovante])
    
    return arquivo_nome


def duplicidade_validation(valor, data, categoria, type):
    if type == 'r':
        
        dados = Receita.objects.filter(valor=valor)

    else:
        dados = Despesa.objects.filter(valor=valor)

    dados = dados.filter(data=data)
    dados = dados.filter(categoria=categoria)

    if len(dados) == 0:
        return True
    
    else:
        return False
