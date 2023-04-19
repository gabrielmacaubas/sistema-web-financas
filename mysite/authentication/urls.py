from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.entrar, name="entrar"),
    path('registrar', views.registrar, name="registrar"),
    path('sair', views.sair, name="sair"),
]