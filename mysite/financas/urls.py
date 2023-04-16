from django.urls import path
from . import views

urlpatterns = [
    path('receitas/', views.receitas_view, name='receitas'),
    path('criar/<str:type>', views.criar, name='criar'),
    path('remover/', views.remover, name='remover'),
    path('alterar/<str:type>/<int:id>', views.alterar, name='alterar'),
    path('exportar/<str:type>', views.exportar, name="exportar"),
]
