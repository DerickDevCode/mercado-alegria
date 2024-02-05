from mercado.produtos.models import Produto


def listar_produtos_ordenados(slug):
    return {'PRODUTOS': Produto.objects.order_by('slug').all()}
