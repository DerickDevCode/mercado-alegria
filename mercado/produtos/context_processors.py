from mercado.produtos import facade
from mercado.produtos.models import Produto, Departamento


def listar_produtos_ordenados(slug):
    return {'PRODUTOS': Produto.objects.order_by('slug').all()}


def listar_departamentos_ordenados(slug):
    return {'DEPARTAMENTOS': Departamento.objects.order_by('slug').all()}


def listar_favoritos(request):
    produtos = []
    try:
        favoritos = facade.buscar_favoritos_existente(request)
    except Exception:
        favoritos = facade.criar_favoritos(request)
    for item in facade.listar_itens_dos_favoritos(favoritos):
        produtos.append(item.produto)
    return {'PRODUTOS_FAVORITOS': produtos}
