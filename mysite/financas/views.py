import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Receita
from .forms import *
from .utils import *


# view para página de receitas
def receitas_view(request):
    # envia os dados para o template com ou sem filtos
    try:
        if not request.user.is_authenticated:
            template = loader.get_template('acesso_restrito.html')
            context = {}

            return HttpResponse(template.render(context, request))
        
        receitas = Receita.objects.all().order_by('data').reverse()
        filtro_form = request.GET.dict()
        (filtro_form, receitas) = filtrar(receitas, filtro_form, Receita)
        template = loader.get_template('cadastrar_receitas.html')
        context = {
            'form': ReceitaForm(),
            'filtroForm': filtro_form,
            'header': ['Valor', 'Data', 'Descrição', 'Categoria', 'Comprovante'],
            'receitas': receitas,
            'type': 'receita'
        }

        return HttpResponse(template.render(context, request))
    except Exception as e:
        print(e)

# view para página de Despesas
def despesas_view(request):
    # envia os dados para o template com ou sem filtos
    try:
        if not request.user.is_authenticated:
            template = loader.get_template('acesso_restrito.html')
            context = {}
            
            return HttpResponse(template.render(context, request))
        
        despesas = Despesa.objects.all().order_by('data').reverse()
        filtro_form = request.GET.dict()
        (filtro_form, despesas) = filtrar(despesas, filtro_form, Despesa)
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
    except Exception as e:
        print(e)

# view para criação de uma receita
def criar_receita_view(request):
    try:
        form_data = request.POST

        criar(form_data, Receita)

        return redirect('receitas')
    except Exception as e:
        print(e)

# view para criação de uma despesa
def criar_despesa_view(request):
    try:
        form_data = request.POST
        
        criar(form_data, Despesa)
        
        return redirect('despesas')
    except Exception as e:
        print(e)

# view para alteração de uma receita
def alterar_receita_view(request, id): 
    try:
        if not request.user.is_authenticated:
            template = loader.get_template('acesso_restrito.html')
            context = {}
            
            return HttpResponse(template.render(context, request))
        
        # em caso de POST, altera o objeto e redireciona para a página de receitas
        if request.method == 'POST':
            form_data = request.POST
            receita = Receita.objects.get(pk=id)
            alterar(receita, form_data, Receita)
            
            return redirect('receitas')    
        # em caso de GET, envia o objeto a ser alterado para preenchimento do formulário
        receita_antigo = Receita.objects.get(pk=id).__dict__
        receita_antigo.pop('_state')
        receita_antigo.pop('comprovante')
        template = loader.get_template('alterar_receita.html')
        context = {
            'form': ReceitaForm(initial=receita_antigo),
            'id': id
        }

        return HttpResponse(template.render(context, request))
    except Exception as e:
        print(e)

# view para alteração de uma receita
def alterar_despesa_view(request, id):
    try:
        if not request.user.is_authenticated:
            template = loader.get_template('acesso_restrito.html')
            context = {}
            
            return HttpResponse(template.render(context, request))
        
        # em caso de POST, altera o objeto e redireciona para a página de receitas
        if request.method == 'POST':
            form_data = request.POST
            despesa = Despesa.objects.get(pk=id)
            alterar(despesa, form_data, Despesa)
            
            return redirect('despesas')     
        # em caso de GET, envia o objeto a ser alterado para preenchimento do formulário
        despesa_antigo = Despesa.objects.get(pk=id).__dict__
        despesa_antigo.pop('_state')
        despesa_antigo.pop('comprovante')
        template = loader.get_template('alterar_despesa.html')
        context = {
            'form': DespesaForm(initial=despesa_antigo),
            'id': id
        }

        return HttpResponse(template.render(context, request))
    except Exception as e:
        print(e)

# view para alteração de uma receita
def remover_view(request):
    try:
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
    except Exception as e:
        print(e)
  
# view para exportação do arquivo csv de receitas
def exportar_receita_view(request):  
    try:
        receitas = Receita.objects.all()
        arquivo_nome = gerar_arquivo(receitas, 'receita')

        with open(arquivo_nome, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(arquivo_nome)
            
            return response
    except Exception as e:
        print(e)

# view para exportação do arquivo csv de despesas
def exportar_despesa_view(request):
    try:
        despesas = Despesa.objects.all()
        arquivo_nome = gerar_arquivo(despesas, 'despesa')

        with open(arquivo_nome, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(arquivo_nome)
            
            return response
    except Exception as e:
        print(e)
