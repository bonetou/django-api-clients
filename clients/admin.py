from django.contrib import admin
from clients.models import Client

class Clients(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email','cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 25

admin.site.register(Client, Clients)

