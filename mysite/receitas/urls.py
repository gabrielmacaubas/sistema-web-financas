from django.urls import path

from . import views

urlpatterns = [
    path('receitas/', views.receitas_view, name='receitas_view'),
    path('criar_receita/', views.criar_receita, name='criar_receita'),
    path('remover/', views.remover, name='remover'),
    path('alterar/<int:id>', views.alterar, name='alterar'),
]