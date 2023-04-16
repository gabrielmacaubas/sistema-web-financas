import csv


def filtrar_valor(min, max, receitas):  
    if min == '':
        min = "0.00"

    min = float(min.replace(',', '.'))

    if max == '':
        receitas = receitas.filter(valor__gte=min)

    else:
        max = float(max.replace(',', '.'))
        receitas = receitas.filter(valor__gte=min)
        receitas = receitas.filter(valor__lte=max)

    return receitas


def filtrar_categoria(categoria, receitas):
    receitas = receitas.filter(categoria=categoria)
    return receitas


def filtrar_data(data, receitas):
    receitas = receitas.filter(data=data)
    return receitas


def gerar_arquivo(receitas):
    writer = csv.writer(open('receitas.csv', 'w'))
    writer.writerow(['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'])

    for receita in receitas:
        writer.writerow([receita.valor, receita.data, receita.descricao, receita.categoria, receita.comprovante])
    
    