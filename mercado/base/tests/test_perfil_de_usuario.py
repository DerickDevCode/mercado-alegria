import pytest
from django.urls import reverse

from mercado.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('base:perfil'))


def test_status_code_usuario_deslogado(resp):
    assert resp.status_code == 302
    assert resp.url.startswith(reverse('login'))


@pytest.fixture
def resp_usuario_logado(client_com_usuario_logado):
    return client_com_usuario_logado.get(reverse('base:perfil'))


def test_status_code_usuario_logado(resp_usuario_logado):
    assert resp_usuario_logado.status_code == 200


# ------------------------ Testes do Front-end ------------------------ #


def test_botao_editar_perfil_esta_presente_na_pagina(resp_usuario_logado):
    assert_contains(resp_usuario_logado, '''<img src="/static/img/icone-editar-usuario.png" width="40"
                             height="35"
                             style="margin-right: 4px">Editar Perfil</a>''')


def test_botao_senha_esta_presente_na_pagina(resp_usuario_logado):
    assert_contains(resp_usuario_logado, '''<img src="/static/img/icone-cadeado.png" width="40"
                             height="35"
                             style="margin-right: 4px">Senha</a>''')


def test_botao_meus_favoritos_esta_presente_na_pagina(resp_usuario_logado):
    assert_contains(resp_usuario_logado, '''<img src="/static/img/icone-coracao.png" width="40"
                             height="35"
                             style="margin-right: 4px">Meus Favoritos</a>''')


def test_botao_pagamentos_esta_presente_na_pagina(resp_usuario_logado):
    assert_contains(resp_usuario_logado, '''<img src="/static/img/icone-cartao-pagamento.png" width="40"
                             height="35"
                             style="margin-right: 4px">Pagamentos</a>''')


def test_botao_de_logout_esta_presente_na_pagina(resp_usuario_logado):
    assert_contains(resp_usuario_logado, f'<form method="post" action="{reverse("logout")}"')
