from mercado.produtos.models import Produto


def buscar_produto(slug):
    """
    Encontra um produto solicitado
    :param slug: recebe o slug do produto
    :return: retorna o produto referente ao slug
    """
    return Produto.objects.get(slug=slug)


def buscar_categoria_do_produto(slug):
    """
    Encontra a categoria de um produto solicitado
    :param slug: recebe o slug do produto
    :return: retorna a categoria do produto referente ao slug
    """
    return Produto.objects.get(slug=slug).categoria.slug


def buscar_departamento_da_categoria(slug):
    """
    Encontra o departamento de uma categoria solicitada
    :param slug: recebe o slug do produto
    :return: retorna o departamento da categoria referente a um produto
    """
    return Produto.objects.get(slug=slug).categoria.departamento.slug
