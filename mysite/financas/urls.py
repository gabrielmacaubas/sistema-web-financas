from django.urls import path
from . import views

urlpatterns = [
    path('receitas/', views.receitas_view, name='receitas'),
    path('despesas/', views.despesas_view, name='despesas'),
    path('criar_receita/', views.criar_receita, name='criar_receita'),
    path('criar_despesa/', views.criar_despesa, name='criar_despesa'),
    path('remover/', views.remover, name='remover'),
    path('alterar_receita/<int:id>', views.alterar_receita, name="alterar_receita"),
    path('alterar_despesa/<int:id>', views.alterar_despesa, name="alterar_despesa"),
    path('exportar_receita/', views.exportar_receita, name="exportar_receita"),
    path('exportar_despesa/', views.exportar_despesa, name="exportar_despesa"),
]
