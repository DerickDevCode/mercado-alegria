from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from mercado.base.forms import UserForm
from mercado.base.models import User


def home(request):
    return render(request, 'base/home.html')


def cadastro(request):
    if request.method == 'GET':
        form = UserForm
        return render(request, 'base/cadastro.html', context={'form': form})
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=form.cleaned_data['email'])
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user=user)
            return redirect('/')
        else:
            return render(request, 'base/cadastro.html', context={'form': form})


@login_required
def perfil(request):
    return render(request, 'base/perfil.html', context={})


@login_required
def editar_perfil(request):
    if request.method == 'GET':
        user = request.user
        form = UserForm(instance=user)
        return render(request, 'base/editar_perfil.html', context={'form': form, 'user': user})
    elif request.method == 'POST':
        user = request.user
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'base/editar_perfil.html', context={'form': form})


def quem_somos_nos(request):
    return render(request, 'base/quem_somos_nos.html')


def politica_de_privacidade(request):
    return render(request, 'base/politica_de_privacidade.html')


def politica_de_entrega(request):
    return render(request, 'base/politica_de_entrega.html')


def trocas_e_devolucoes(request):
    return render(request, 'base/trocas_e_devolucoes.html')


def politicas_de_cancelamentos_e_ressarcimentos(request):
    return render(request, 'base/políticas_de_cancelamentos_e_ressarcimentos.html')


def politica_de_venda_precos_ofertas_e_promocoes(request):
    return render(request, 'base/política_de_venda_preços_ofertas_e_promoções.html')


def central_de_atendimento(request):
    return render(request, 'base/central_de_atendimento.html')


def pagamento_sucesso(request):
    return render(request, 'base/pagamento_sucesso.html')


def pagamento_falha(request):
    return render(request, 'base/pagamento_falha.html')
