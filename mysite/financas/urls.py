from django.urls import path
from . import views

# paths para o CRUD

urlpatterns = [
    path('receitas/', views.receitas_view, name='receitas'),
    path('despesas/', views.despesas_view, name='despesas'),
    path('criar_receita/', views.criar_receita_view, name='criar_receita'),
    path('criar_despesa/', views.criar_despesa_view, name='criar_despesa'),
    path('remover/', views.remover_view, name='remover'),
    path('alterar_receita/<int:id>', views.alterar_receita_view, name="alterar_receita"),
    path('alterar_despesa/<int:id>', views.alterar_despesa_view, name="alterar_despesa"),
    path('exportar_receita/', views.exportar_receita_view, name="exportar_receita"),
    path('exportar_despesa/', views.exportar_despesa_view, name="exportar_despesa"),
]
