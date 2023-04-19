from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


def entrar(request):
    if request.method == 'POST':
        form = request.POST
        nome = form['username']
        senha = form['password']
        user = authenticate(username=nome, password=senha)

        if user is not None:
            login(request, user)

            return redirect('home')

        else:
            messages.error(request, 'Usuário ou senha inválidos!')

            return redirect('entrar')

    if request.user.is_authenticated:
        return redirect('home')
    
    template = loader.get_template('entrar.html')
    context = {
        'form': UserEntrarForm()
    }

    return HttpResponse(template.render(context, request))


def registrar(request):
    
        if request.method == 'POST':
            form = request.POST
            nome = form['username']
            email = form['email']
            senha = form['password']
            
            try:
                usuario = User.objects.create_user(nome, email, senha)
            except Exception:
                messages.error(request, 'Este usuário já existe!')

                return redirect('registrar')
            
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            
            return redirect('entrar')

        template = loader.get_template('registrar.html')
        context = {
            'form': UserCadastrarForm()
        }

        return HttpResponse(template.render(context, request))


def sair(request):
    logout(request)
    messages.success(request, 'Usuário deslogado com sucesso!')

    return redirect('entrar')
