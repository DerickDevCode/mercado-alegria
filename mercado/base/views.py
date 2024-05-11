from django.contrib.auth.hashers import make_password
from django.shortcuts import render

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
            return render(request, 'base/home.html')
        else:
            return render(request, 'base/cadastro.html', context={'form': form})
