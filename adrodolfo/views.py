from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Escala
from .forms import EscalaForm

# Create your views here.
def index(request):
    return render(request, 'adrodolfo/index.html')

def escala_list(request):
    # Ordenando as escalas do Templo Sede e Sítio Espinheiro pelo campo 'dia'
    escalas_templo = Escala.objects.filter(congregacao='Templo Sede').order_by(
        'dia')
    escalas_sitio = Escala.objects.filter(congregacao='Sítio Espinheiro').order_by('dia')

    return render(request, 'adrodolfo/escala_list.html', {
        'escalas_templo': escalas_templo,
        'escalas_sitio': escalas_sitio,
    })

@login_required
# View para criar programação da escala
def escala_create(request):
    if request.method == 'POST':
        form = EscalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('escala_list')
    else:
        form = EscalaForm()
    return render(request, 'adrodolfo/escala_form.html', {'form': form})

# Editar programação escala
def escala_update(request, id):
    escala = get_object_or_404(Escala, id=id)
    if request.method == 'POST':
        form = EscalaForm(request.POST, instance=escala)
        if form.is_valid():
            form.save()
            return redirect('escala_list')
    else:
        form = EscalaForm(instance=escala)
    return render(request, 'adrodolfo/escala_form.html', {'form': form})

# Deletar programação da escala
def escala_delete(request, id):
    escala = get_object_or_404(Escala, id=id)
    if request.method == 'POST':
        escala.delete()
        return redirect('escala_list')
    return render(request, 'adrodolfo/escala_confirm_delete.html', {'escala': escala})


def novo_templo(request):
    return render(request, 'adrodolfo/novo_templo.html')

def historia(request):
    return render(request, 'adrodolfo/historia.html')

def obra_missionaria(request):
    return render(request, 'adrodolfo/obra_missionaria.html')

def contate_nos(request):
    return render(request, 'adrodolfo/contate_nos.html')
