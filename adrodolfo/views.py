import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Escala, MensagemContato
from .forms import EscalaForm, ContatoForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .models import MensagemContato


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True  
            user.is_superuser = False  
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)  
    return redirect('login')  

def index(request):
    versiculos = {
        "João 3:16": "Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo aquele que nele crê não pereça, mas tenha a vida eterna.",
        "Salmos 23:1": "O Senhor é o meu pastor; nada me faltará.",
        "Filipenses 4:13": "Tudo posso naquele que me fortalece.",
        "Jeremias 29:11": "Porque eu sei os pensamentos que penso de vós, diz o Senhor; pensamentos de paz, e não de mal, para vos dar o fim que desejais.",
        "Provérbios 3:5-6": "Confia no Senhor de todo o teu coração e não te estribes no teu próprio entendimento. Reconhece-o em todos os teus caminhos, e ele endireitará as tuas veredas.",
    }
    #chave esta que é acessada lá na linha posterior, que é chamada e pega o versiculo específico
    referencia_versiculo = random.choice(list(versiculos.keys())) #para cada versiculo, que por sua vez possui sua referencia, é criada uma chavezinha que é randomizada
    versiculo = versiculos[referencia_versiculo] #essa chavezinha é usada aqui para acessar o dicionario e pegar o versiculo especifico

    contexto = {
        "referencia_versiculo": referencia_versiculo,
        "versiculo": versiculo,
    }
    return render(request, 'adrodolfo/index.html', contexto)

def escala_list(request):
    escalas_templo = Escala.objects.filter(congregacao='Templo Sede').order_by(
        'dia', 'horario')
    escalas_sitio = Escala.objects.filter(congregacao='Sítio Espinheiro').order_by('dia', 'horario')

    return render(request, 'adrodolfo/escala_list.html', {
        'escalas_templo': escalas_templo,
        'escalas_sitio': escalas_sitio,
    })



def contate_nos(request):
    form = ContatoForm(request.POST or None)
    mensagem_sucesso = False

    if request.method == 'POST' and form.is_valid():
        # Salvar os dados no banco
        MensagemContato.objects.create(
            nome=form.cleaned_data['nome'],
            email=form.cleaned_data['email'],
            mensagem=form.cleaned_data['mensagem']
        )
        mensagem_sucesso = True
        form = ContatoForm()  # Recria o formulário vazio após o envio bem-sucedido

    contexto = {
        'form': form,
        'mensagem_sucesso': mensagem_sucesso,
    }

    return render(request, 'adrodolfo/contate_nos.html', contexto)


def historia(request):
    return render(request, 'adrodolfo/historia.html')

def obra_missionaria(request):
    return render(request, 'adrodolfo/obra_missionaria.html')


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


def mensagens_view(request):
    # Filtro de busca
    search_query = request.GET.get('search', '')
    if search_query:
        mensagens = MensagemContato.objects.filter(nome__icontains=search_query) | MensagemContato.objects.filter(email__icontains=search_query)
    else:
        mensagens = MensagemContato.objects.all()

    # Paginação
    paginator = Paginator(mensagens, 5)  # 5 mensagens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto = {
        'mensagens': page_obj,
        'search_query': search_query,
    }
    return render(request, 'adrodolfo/mensagens.html', contexto)