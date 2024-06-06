import pytest

from mercado.base.models import User


@pytest.fixture
def usuario_logado(db):
    usuario_modelo = User.objects.create_user(first_name='teste', last_name='testando', date_of_birth='2000-01-01',
                                              email='usuario@exemplo.com',
                                              cpf='000.000.000-00', phone_number='00 00000-0000', password='teste123')
    return usuario_modelo


@pytest.fixture
def client_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client
