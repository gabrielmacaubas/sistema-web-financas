from django.contrib import admin
from django.urls import path
from financas.views import *
from home.views import home_view

urlpatterns = [
    path('', home_view, name="home"),
    path('receitas/', receitas_view, name="receitas"),
    path('despesas/', despesas_view, name="despesas"),
    path('criar_receita/', criar_receita, name='criar_receita'),
    path('criar_despesa/', criar_despesa, name='criar_despesa'),
    path('remover/', remover, name="remover"),
    path('alterar_receita/<int:id>', alterar_receita, name="alterar_receita"),
    path('alterar_despesa/<int:id>', alterar_despesa, name="alterar_despesa"),
    path('exportar_receita/', exportar_receita, name="exportar_receita"),
    path('exportar_despesa/', exportar_despesa, name="exportar_despesa"),
    path('admin/', admin.site.urls, name="aadmin"),
]
