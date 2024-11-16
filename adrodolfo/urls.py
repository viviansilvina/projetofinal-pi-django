from django.urls import path
from adrodolfo import views

urlpatterns = [
    path('', views.index, name='index'),

    path('escala/', views.escala_list, name='escala_list'),  # Listar escalas
    path('escala/novo/', views.escala_create, name='escala_create'),  # Criar escala
    path('escala/editar/<int:id>/', views.escala_update, name='escala_update'),  # Editar escala
    path('escala/deletar/<int:id>/', views.escala_delete, name='escala_delete'),  # Deletar escala
    
    path('novo_templo/', views.novo_templo, name='novo_templo'),
    path('historia/', views.historia, name='historia'),
    path('obra_missionaria/', views.obra_missionaria, name='obra_missionaria'),
    path('contate_nos/', views.contate_nos, name='contate_nos'),
]