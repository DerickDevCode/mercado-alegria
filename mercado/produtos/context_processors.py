from mercado.produtos import facade
from mercado.produtos.models import Produto, Departamento


def listar_produtos_ordenados(slug):
    return {'PRODUTOS': Produto.objects.select_related('subcategoria__categoria__departamento').order_by('slug').all()}


def listar_departamentos_ordenados(slug):
    return {'DEPARTAMENTOS': Departamento.objects.order_by('slug').all()}


def listar_favoritos(request):
    produtos = []
    if request.user.is_authenticated:
        try:
            favoritos = facade.buscar_favoritos_existente(request)
        except Exception:
            favoritos = facade.criar_favoritos(request)
        for item in facade.listar_itens_dos_favoritos(favoritos):
            produtos.append(item.produto)
    else:
        pass
    return {'PRODUTOS_FAVORITOS': produtos}
