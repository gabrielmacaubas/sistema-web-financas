from django.contrib import admin
from .models import Receita, Despesa

# registra os modelos no painel de administração
admin.site.register(Receita)
admin.site.register(Despesa)
