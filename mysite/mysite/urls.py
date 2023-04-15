"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
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
