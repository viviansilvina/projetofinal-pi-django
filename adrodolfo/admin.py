from django.contrib import admin
from .models import Contatos, Segunda, Terca, Quarta, Quinta, Sexta, Sabado, Domingo
# Register your models here.
@admin.register(Contatos)
class ContatosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'mensagem')

@admin.register(Segunda)
class SegundaAdmin(admin.ModelAdmin):
    list_display = ('programacao', 'horario')

@admin.register(Terca) 
class TercaAdmin(admin.ModelAdmin):
    list_display = ('programacao', 'horario')

@admin.register(Quarta)
class QuartaAdmin(admin.ModelAdmin):
    list_display = ('programacao', 'horario')

@admin.register(Quinta)
class QuintaAdmin(admin.ModelAdmin):
    list_display = ('programacao', 'horario')
    
@admin.register(Sexta)
class SextaAdmin(admin.ModelAdmin):
    list_display = ('programacao', 'horario')

@admin.register(Sabado)
class SabadoAdmin(admin.ModelAdmin):
    list_display = ('programacao', 'horario')

@admin.register(Domingo)
class DomingoAdmin(admin.ModelAdmin):
    list_display = ('programacao', 'horario')