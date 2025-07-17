import django
import mercadopago
import os

from mercado.produtos.carrinho import Carrinho

os.environ['DJANGO_SETTINGS_MODULE'] = 'mercado.settings'
django.setup()

from mercado.produtos import facade  # noqa
from mercado.settings import TOKEN_MERCADO_PAGO, BASE_URL_COMERCIAL_ALEGRIA  # noqa


def obter_info_itens_para_pagamento(carrinho, carrinhoitens):
    items_detail = []
    for item in carrinhoitens:
        items_detail.append({'id': item.produto.id, 'title': item.produto.nome, 'picture_url': item.produto.imagem.url,
                             'quantity': item.quantidade, 'currency_id': 'BRL',
                             'unit_price': float(item.produto.preco)})
    return items_detail


def gerar_link_de_pagamento(carrinho, carrinhoitens):
    # Adicione as credenciais
    sdk = mercadopago.SDK(TOKEN_MERCADO_PAGO)

    # Cria um item na preferência
    preference_data = {
        "items": obter_info_itens_para_pagamento(carrinho, carrinhoitens),
        "back_urls": {
            "success": f"http://{BASE_URL_COMERCIAL_ALEGRIA}/pagamento_falha",
            "failure": f"http://{BASE_URL_COMERCIAL_ALEGRIA}/pagamento_falha",
        },
        "auto_return": "all"
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    try:
        result = preference['init_point']
        return result
    except KeyError:
        pass
