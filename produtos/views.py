from django.shortcuts import redirect, render

from .forms import EmbalagemForm, LocalForm
from .models import Local


def inicio(request):
    return render(request, 'menu.html')


def listar_locais(request):
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()
    if consulta:
        locais = locais.filter(nome__icontains=consulta)
    if tipo:
        locais = locais.filter(tipo=tipo)
    return render(request, 'produtos/listar_locais.html', {'locais': locais})


def adicionar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listar_locais')
    else:
        form = LocalForm()
    return render(request, 'produtos/adicionar_local.html', {'form': form})  # noqa: E501

def listar_embalagem(request):
    nome = request.GET.get('Nome da Embalagem')
    sigla= request.GET.get('Sigla da Embalagem')
    embalagens = EmbalagemForm.objects.all()
    if nome:
        embalagens = embalagens.filter(nome__icontains=nome)
    if sigla:
        embalagens = embalagens.filter(sigla=sigla)
    return render(request, 'produtos/listar_embalagem.html', {'embalagens': embalagens})

def adicionar_embalagem(request):
    if request.method == 'POST':
        form = EmbalagemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listar_embalagem')
    else:
        form = EmbalagemForm()
    return render(request, 'produtos/adicionar_embalagem.html', {'form': form})