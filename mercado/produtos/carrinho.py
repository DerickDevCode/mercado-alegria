from decimal import Decimal

from mercado import settings
from mercado.produtos.models import Produto, CarrinhoItem


class Carrinho(object):
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get(settings.CARRRINHO_SESSION_ID)
        if settings.CARRRINHO_SESSION_ID not in request.session:
            carrinho = self.session[settings.CARRRINHO_SESSION_ID] = {}
        self.carrinho = carrinho

    def add(self, produto, quantidade=1):
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            self.carrinho[produto_id]['quantidade'] += 1
        else:
            self.carrinho[produto_id] = {'quantidade': quantidade}
        self.session.modified = True

    def remove(self, produto):
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
        self.session.modified = True

    def get_products(self):
        produtos = [(key, p) for key, p in self.carrinho.items()]
        carrinhoitem = []
        for id, p in produtos:
            produto = Produto.objects.get(id=id)
            carrinhoitem.append(CarrinhoItem(produto=produto, quantidade=p['quantidade']))
        return carrinhoitem

    def __len__(self):
        return sum(item['quantidade'] for item in self.carrinho.values())

    def get_sub_total_price(self):
        return sum(Decimal(item['preco']) * item['quantidade'] for item
                   in self.carrinho.values())

    def clear(self):
        """
        Remove all items from the cart.
        """
        for key in list(self.carrinho.keys()):  # Use list() para criar uma cópia das chaves
            del self.carrinho[key]
        self.session.modified = True

    def save(self):
        self.session[settings.CARRRINHO_SESSION_ID] = self.carrinho
        self.session.modified = True
