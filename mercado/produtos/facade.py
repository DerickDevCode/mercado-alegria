from mercado.produtos.models import Produto, Carrinho, CarrinhoItem


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


def filtrar_produtos_pela_pesquisa(query):
    """
    Lista todos os produtos resultantes de uma pesquisa na barra de pesquisa
    :return: retorna uma lista com os produtos filtrados pela pesquisa
    """
    return Produto.objects.filter(nome__icontains=query)


def buscar_carrinho_existente(request):
    """
    Encontra o carrinho respectivo ao usuário do site através das informações do request
    :param request: recebe o request
    :return: retorna o carrinho do usuário
    """
    return Carrinho.objects.filter(user=request.user).first()


def criar_carrinho(request):
    """
    Cria um novo carrinho a partir do usuário do site através das informações do request
    :param request: recebe o request
    :return: retorna o carrinho do usuário
    """
    return Carrinho.objects.create(user=request.user)


def buscar_item_do_carrinho(produto):
    """
    Encontra o item do carrinho através do produto
    :param produto: recebe o produto a ser encontrado dentro do carrinho
    :return: retorna o item(produto) do carrinho
    """
    return CarrinhoItem.objects.get(produto=produto)
