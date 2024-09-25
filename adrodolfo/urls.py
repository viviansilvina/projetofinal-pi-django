from django.urls import path
from adrodolfo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('escala/', views.escala, name='escala'),
    path('novo_templo/', views.novo_templo, name='novo_templo'),
    path('historia/', views.historia, name='historia'),
    path('obra_missionaria/', views.obra_missionaria, name='obra_missionaria'),
    path('contate_nos/', views.contate_nos, name='contate_nos'),
]