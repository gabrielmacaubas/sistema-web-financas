from django.contrib import admin
from django.urls import path
from financas.views import receitas_view, alterar, criar_receita, remover, exportar
from home.views import home_view

urlpatterns = [
    path('', home_view, name="home"),
    path('receitas/', receitas_view, name="receitas"),
    path('criar_receita/', criar_receita, name="criar_receita"),
    path('remover/', remover, name="remover"),
    path('alterar/<int:id>', alterar, name="alterar"),
    path('exportar/', exportar, name="exportar"),
    path('admin/', admin.site.urls, name="aadmin"),
]
