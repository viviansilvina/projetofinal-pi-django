from django.contrib import admin
from .models import Contatos, Escala
# Register your models here.
@admin.register(Contatos)
class ContatosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'mensagem')

@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ('dia', 'programacao', 'horario', 'congregacao')
    list_filter = ('congregacao', 'dia')
    search_fields = ('dia', 'programacao', 'congregacao')
    ordering = ('dia', 'horario')