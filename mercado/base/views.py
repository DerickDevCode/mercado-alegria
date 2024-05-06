from django.shortcuts import render

from mercado.base.forms import UserForm


def home(request):
    return render(request, 'base/home.html')


def cadastro_e_login(request):
    form = UserForm
    return render(request, 'base/cadastro_e_login.html', context={'form': form})
