from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'adrodolfo/index.html')

def escala(request):
    return render(request, 'adrodolfo/escala.html')

def novo_templo(request):
    return render(request, 'adrodolfo/novo_templo.html')

def historia(request):
    return render(request, 'adrodolfo/historia.html')

def obra_missionaria(request):
    return render(request, 'adrodolfo/obra_missionaria.html')

def contate_nos(request):
    return render(request, 'adrodolfo/contate_nos.html')