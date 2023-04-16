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