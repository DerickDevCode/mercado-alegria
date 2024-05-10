from django.shortcuts import render

from mercado.base.forms import UserForm


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
            return render(request, 'base/home.html')
        else:
            return render(request, 'base/cadastro.html', context={'form': form})
