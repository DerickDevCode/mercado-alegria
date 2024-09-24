# SDK do Mercado Pago
import mercadopago

from mercado.settings import TOKEN_MERCADO_PAGO


def gerar_link_de_pagamento():
    # Adicione as credenciais
    sdk = mercadopago.SDK(TOKEN_MERCADO_PAGO)

    # Cria um item na preferência
    preference_data = {
        "items": [
            {
                "id": "1",
                "title": "Produto teste",
                # "description": "Dummy description",
                # "picture_url": "http://www.myapp.com/myimage.jpg",
                # "category_id": "car_electronics",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 1,
            }
        ],
        "back_urls": {
            "success": "http://test.com/success",
            "failure": "http://test.com/failure",
            "pending": "http://test.com/pending",
        },
        "auto_return": "all"
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    return preference['init_point']

# print(preference)
# print(preference['init_point'])
