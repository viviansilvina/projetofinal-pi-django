from django.urls import path
from adrodolfo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    path('escala/', views.escala_list, name='escala_list'),  # Listar escalas
    path('escala/novo/', views.escala_create, name='escala_create'),  # Criar escala
    path('escala/editar/<int:id>/', views.escala_update, name='escala_update'),  # Editar escala
    path('escala/deletar/<int:id>/', views.escala_delete, name='escala_delete'),  # Deletar escala
    
    path('historia/', views.historia, name='historia'),
    path('obra_missionaria/', views.obra_missionaria, name='obra_missionaria'),
    path('contate_nos/', views.contate_nos, name='contate_nos'),
    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    
    path('mensagens/', views.mensagens_view, name='mensagens'),

]