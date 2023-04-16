from django.contrib import admin
from django.urls import path
from financas.views import *
from home.views import home_view

urlpatterns = [
    path('', home_view, name="home"),
    path('receitas/', receitas_view, name="receitas"),
    path('despesas/', despesas_view, name="despesas"),
    path('criar/<str:type>', criar, name="criar"),
    path('remover/', remover, name="remover"),
    path('alterar/<str:type>/<int:id>', alterar, name="alterar"),
    path('exportar/<str:type>', exportar, name="exportar"),
    path('admin/', admin.site.urls, name="aadmin"),
]
