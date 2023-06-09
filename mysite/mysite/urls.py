from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from financas.views import *
from home.views import home_view

# paths para o CRUD
urlpatterns = [
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('home/', home_view, name='home'),
    path('receitas/', receitas_view, name="receitas"),
    path('despesas/', despesas_view, name="despesas"),
    path('criar_receita/', criar_receita_view, name='criar_receita'),
    path('criar_despesa/', criar_despesa_view, name='criar_despesa'),
    path('remover/', remover_view, name="remover"),
    path('alterar_receita/<int:id>', alterar_receita_view, name="alterar_receita"),
    path('alterar_despesa/<int:id>', alterar_despesa_view, name="alterar_despesa"),
    path('exportar_receita/', exportar_receita_view, name="exportar_receita"),
    path('exportar_despesa/', exportar_despesa_view, name="exportar_despesa"),
]
