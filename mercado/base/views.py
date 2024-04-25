from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def cadastro_e_login(request):
    return render(request, 'base/cadastro_e_login.html')
