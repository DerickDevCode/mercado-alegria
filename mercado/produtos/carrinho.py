from mercado import settings
from mercado.produtos import facade
from mercado.produtos.models import Produto, CarrinhoItem


class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        if settings.CARRINHO_SESSION_ID not in request.session:
            carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}
        self.carrinho = carrinho

    def add_product_to_cart(self, produto_id, quantidade=1):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            self.carrinho[produto_id]['quantidade'] += 1
        else:
            self.carrinho[produto_id] = {'quantidade': quantidade}
        self.session.modified = True

    def remove_product_from_cart(self, produto_id):
        produto_id = str(produto_id)
        try:
            self.carrinho[produto_id]['quantidade'] -= 1
            if self.carrinho[produto_id]['quantidade'] <= 0:
                del self.carrinho[produto_id]
        except Exception:
            pass
        self.session.modified = True

    def exclude_product_from_cart(self, produto_id):
        produto_id = str(produto_id)
        try:
            del self.carrinho[produto_id]
            self.session.modified = True
        except Exception:
            pass

    def get_products(self):
        produtos = [(key, p) for key, p in self.carrinho.items()]
        carrinho = []
        for id, p in produtos:
            produto = Produto.objects.get(id=id)
            carrinho.append(ItemCarrinho(produto=produto, carrinho=self.carrinho, quantidade=p['quantidade']))
        return carrinho


class ItemCarrinho:
    def __init__(self, produto, carrinho, quantidade):
        self.produto = produto
        self.carrinho = carrinho
        self.quantidade = quantidade

    @property
    def total(self):
        return self.quantidade * self.produto.preco


# Funções criadas para melhor apresentação de código nas views do carrinho

def calcular_total_itens(itens):
    total = 0
    for item in itens:
        total += item.produto.preco * item.quantidade
    return total


def obter_carrinho_e_itens(request):
    if request.user.is_authenticated:
        try:
            carrinho = facade.buscar_carrinho_existente(request)
        except Exception:
            carrinho = facade.criar_carrinho(request)
        carrinhoitens = facade.listar_itens_do_carrinho(carrinho)
    else:
        carrinho = Carrinho(request)
        carrinhoitens = carrinho.get_products()
    return carrinho, carrinhoitens


def adicionar_produto_ao_carrinho(request, produto_id):
    if request.user.is_authenticated:
        try:
            carrinho = facade.buscar_carrinho_existente(request)
        except Exception:
            carrinho = facade.criar_carrinho(request)

        produto = Produto.objects.get(id=produto_id)

        try:
            item = facade.buscar_item_do_carrinho(produto)
            item.quantidade += 1
            item.save()
        except Exception:
            novo_item = CarrinhoItem(produto=produto, carrinho=carrinho)
            novo_item.save()
        carrinhoitens = facade.listar_itens_do_carrinho(carrinho)
    else:
        carrinho = Carrinho(request)
        carrinho.add_product_to_cart(produto_id)
        carrinhoitens = carrinho.get_products()
    return carrinho, carrinhoitens


def remover_produto_do_carrinho(request, produto_id):
    if request.user.is_authenticated:
        carrinho = facade.buscar_carrinho_existente(request)
        produto = Produto.objects.get(id=produto_id)
        try:
            item = facade.buscar_item_do_carrinho(produto)
            item.quantidade -= 1
            item.save()
            if item.quantidade <= 0:
                item.delete()
        except Exception:
            pass
        carrinhoitens = facade.listar_itens_do_carrinho(carrinho)
    else:
        carrinho = Carrinho(request)
        carrinho.remove_product_from_cart(produto_id)
        carrinhoitens = carrinho.get_products()
    return carrinho, carrinhoitens


def excluir_produto_do_carrinho(request, produto_id):
    if request.user.is_authenticated:
        carrinho = facade.buscar_carrinho_existente(request)
        produto = Produto.objects.get(id=produto_id)
        try:
            item = facade.buscar_item_do_carrinho(produto)
            item.delete()
        except Exception:
            pass
        carrinhoitens = facade.listar_itens_do_carrinho(carrinho)
    else:
        carrinho = Carrinho(request)
        carrinho.exclude_product_from_cart(produto_id)
        carrinhoitens = carrinho.get_products()
    return carrinho, carrinhoitens
