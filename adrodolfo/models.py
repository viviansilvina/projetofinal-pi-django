from django.db import models

# Create your models here.

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

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome} ({self.email})"
    