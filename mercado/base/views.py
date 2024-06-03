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
        form = UserForm
        return render(request, 'base/editar_perfil.html', context={'form': form, 'user': user})
    elif request.method == 'POST':
        user = request.user
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'base/editar_perfil.html', context={'form': form})
