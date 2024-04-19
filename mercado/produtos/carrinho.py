from decimal import Decimal

from mercado import settings
from mercado.produtos.models import Produto, CarrinhoItem


class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get(settings.CARRRINHO_SESSION_ID)
        if settings.CARRRINHO_SESSION_ID not in request.session:
            carrinho = self.session[settings.CARRRINHO_SESSION_ID] = {}
        self.carrinho = carrinho

    def add_product_to_cart(self, produto, quantidade=1):
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            self.carrinho[produto_id]['quantidade'] += 1
        else:
            self.carrinho[produto_id] = {'quantidade': quantidade}
        self.session.modified = True

    def remove_product_from_cart(self, produto):
        produto_id = str(produto.id)
        try:
            self.carrinho[produto_id]['quantidade'] -= 1
            if self.carrinho[produto_id]['quantidade'] <= 0:
                del self.carrinho[produto_id]
        except Exception:
            pass
        self.session.modified = True

    def exclude_product_from_cart(self, produto):
        try:
            produto_id = str(produto.id)
            del self.carrinho[produto_id]
            self.session.modified = True
        except Exception:
            pass

    def get_products(self):
        produtos = [(key, p) for key, p in self.carrinho.items()]
        carrinho = []
        for id, p in produtos:
            produto = Produto.objects.get(id=id)
            carrinho.append(CarrinhoItem(produto=produto, quantidade=p['quantidade']))
        return carrinho

    def __len__(self):
        return sum(item['quantidade'] for item in self.carrinho.values())

    def get_sub_total_price(self):
        return sum(Decimal(item['preco']) * item['quantidade'] for item
                   in self.carrinho.values())
