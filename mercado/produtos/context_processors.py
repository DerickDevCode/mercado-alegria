from mercado.produtos.models import Produto, Departamento


def listar_produtos_ordenados(slug):
    return {'PRODUTOS': Produto.objects.order_by('slug').all()}


def listar_departamentos_ordenados(slug):
    return {'DEPARTAMENTOS': Departamento.objects.order_by('slug').all()}
