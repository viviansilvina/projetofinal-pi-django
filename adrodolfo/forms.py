from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Escala, MensagemContato

class EscalaForm(forms.ModelForm):
    class Meta:
        model = Escala
        fields = ['dia', 'programacao', 'horario', 'congregacao']  # Campos a serem exibidos no formulário
        widgets = {
            'dia': forms.Select(attrs={'class': 'form-control'}),  # Altere para Select
            'programacao': forms.TextInput(attrs={'class': 'form-control'}),
            'horario': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'congregacao': forms.Select(attrs={'class': 'form-control'}),
        }


class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': 'required'}),
            'mensagem': forms.Textarea(attrs={'placeholder': 'Escreva uma mensagem...', 'rows': 4, 'required': 'required'}),
        }