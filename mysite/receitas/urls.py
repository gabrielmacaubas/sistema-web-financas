from django.urls import path

from . import views

urlpatterns = [
    path('receitas/', views.receitas_view, name='receitas_view'),
]