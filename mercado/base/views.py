from django.shortcuts import render, redirect

from mercado.base.forms import UserForm


def home(request):
    return render(request, 'base/home.html')


def cadastro_e_login(request):
    if request.method == 'GET':
        form = UserForm
        return render(request, 'base/cadastro_e_login.html', context={'form': form})
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base/home.html')
        else:
            return render(request, 'base/cadastro_e_login.html', context={'form': form})
