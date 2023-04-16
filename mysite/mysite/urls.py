from django.contrib import admin
from django.urls import path
from receitas.views import receitas_view, alterar, criar_receita, remover
from home.views import home_view

urlpatterns = [
    path('', home_view, name="home"),
    path('receitas/', receitas_view, name="receitas"),
    path('criar_receita/', criar_receita, name="criar_receita"),
    path('remover/', remover, name="remover"),
    path('alterar/<int:id>', alterar, name="alterar"),
    path('admin/', admin.site.urls),
]
