from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Escala, MensagemContato
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
        

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):  
        username = self.cleaned_data.get('username') 
        if " " in username:
            raise ValidationError("O nome de usuário não pode conter espaços.")
        
        elif User.objects.filter(username=username).exists():
            raise ValidationError("Este nome de usuário já está em uso. Escolha outro.")
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Esse e-mail já está cadastrado.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("As senhas não coincidem.")
        return password2
