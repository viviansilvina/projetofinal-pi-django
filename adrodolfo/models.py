from django.db import models

# Create your models here.
class Contatos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome

class Segunda(models.Model):
    programacao = models.TextField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.programacao

class Terca(models.Model):
    programacao = models.TextField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.programacao

class Quarta(models.Model):
    programacao = models.TextField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.programacao

class Quinta(models.Model):
    programacao = models.TextField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.programacao

class Sexta(models.Model):  
    programacao = models.TextField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.programacao

class Sabado(models.Model):
    programacao = models.TextField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.programacao

class Domingo(models.Model):
    programacao = models.TextField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.programacao