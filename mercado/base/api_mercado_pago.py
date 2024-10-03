# SDK do Mercado Pago
import django
import mercadopago
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mercado.settings'
django.setup()

from mercado.produtos import facade
from mercado.settings import TOKEN_MERCADO_PAGO, BASE_URL_COMERCIAL_ALEGRIA


def obter_info_itens_para_pagamento(request):
    carrinho = facade.buscar_carrinho_existente(request)
    itens_carrinho = facade.listar_itens_do_carrinho(carrinho)
    items_detail = []
    for item in itens_carrinho:
        items_detail.append({'id': item.produto.id, 'title': item.produto.nome, 'picture_url': item.produto.imagem.url,
                             'quantity': item.quantidade, 'currency_id': 'BRL', 'unit_price': item.produto.preco})
    return items_detail


def gerar_link_de_pagamento(request):
    # Adicione as credenciais
    sdk = mercadopago.SDK(TOKEN_MERCADO_PAGO)

    # Cria um item na preferência
    preference_data = {
        "items": obter_info_itens_para_pagamento(request),
        "back_urls": {
            "success": f"http://{BASE_URL_COMERCIAL_ALEGRIA}/pagamento_falha",
            "failure": f"http://{BASE_URL_COMERCIAL_ALEGRIA}/pagamento_falha",
        },
        "auto_return": "all"
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    return preference['init_point']
