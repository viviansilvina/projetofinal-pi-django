from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Contatos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome

class Escala(models.Model):
    DIAS_CHOICES = [
        ("Segunda-feira", "Segunda-feira"),
        ("Terça-feira", "Terça-feira"),
        ("Quarta-feira", "Quarta-feira"),
        ("Quinta-feira", "Quinta-feira"),
        ("Sexta-feira", "Sexta-feira"),
        ("Sábado", "Sábado"),
        ("Domingo", "Domingo"),
    ]

    dia = models.CharField(max_length=15, choices=DIAS_CHOICES)
    programacao = models.TextField()
    horario = models.TimeField()
    congregacao = models.CharField(
        max_length=20,
        choices=[('Templo Sede', 'Templo Sede'), ('Sítio Espinheiro', 'Sítio Espinheiro')]
    )

    def __str__(self):
        return f"{self.programacao} - {self.dia}"
# models.py