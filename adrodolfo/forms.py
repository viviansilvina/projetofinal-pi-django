from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Escala

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
