from django.shortcuts import render


def produto(request):
    return render(request, 'produtos/produto_detalhe.html')