from mercado.produtos.models import Produto


def buscar_produto(slug):
    """
    Encontra um produto solicitado
    :param slug: recebe o slug do produto
    :return: retorna o produto referente ao slug
    """
    return Produto.objects.get(slug=slug)


def buscar_subcategoria_do_produto(slug):
    """
    Encontra a subcategoria de um produto solicitado
    :param slug: recebe o slug do produto
    :return: retorna a subcategoria do produto referente ao slug
    """
    return Produto.objects.get(slug=slug).subcategoria.slug


def buscar_categoria_do_produto(slug):
    """
    Encontra a categoria de um produto solicitado
    :param slug: recebe o slug do produto
    :return: retorna a categoria do produto referente ao slug
    """
    return Produto.objects.get(slug=slug).subcategoria.categoria.slug


def buscar_departamento_do_produto(slug):
    """
    Encontra o departamento de um produto solicitado
    :param slug: recebe o slug do produto
    :return: retorna o departamento do produto
    """
    return Produto.objects.get(slug=slug).subcategoria.categoria.departamento.slug


def listar_produtos_por_marca(marca):
    """
    Lista todos os produtos de uma determinada marca
    :return: retorna uma lista com os produtos de uma determinada marca ordenados pelo slug
    """
    return list(Produto.objects.filter(marca=marca).order_by('slug'))


def listar_produtos_por_departamento(departamento):
    """
    Lista todos os produtos de um determinado departamento
    :return: retorna uma lista com os produtos de um determinado departamento ordenados pelo slug
    """
    return list(
        Produto.objects.filter(subcategoria__categoria__departamento__slug__iexact=departamento).order_by('slug'))


def listar_produtos_por_categoria(categoria):
    """
    Lista todos os produtos de uma determinada categoria
    :return: retorna uma lista com os produtos de uma determinada categoria ordenados pelo slug
    """
    return list(Produto.objects.filter(subcategoria__categoria__slug__iexact=categoria).order_by('slug'))


def listar_produtos_por_subcategoria(subcategoria):
    """
    Lista todos os produtos de uma determinada subcategoria
    :return: retorna uma lista com os produtos de uma determinada subcategoria ordenados pelo slug
    """
    return list(Produto.objects.filter(subcategoria__slug__iexact=subcategoria).order_by('slug'))
