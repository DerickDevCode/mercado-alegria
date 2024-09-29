from django.urls import path

from mercado.base.views import home, cadastro, perfil, editar_perfil, quem_somos_nos, politica_de_privacidade, \
    politica_de_entrega, trocas_e_devolucoes, politicas_de_cancelamentos_e_ressarcimentos, \
    politica_de_venda_precos_ofertas_e_promocoes, central_de_atendimento, pagamento_sucesso, pagamento_falha

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar_perfil', editar_perfil, name='editar_perfil'),
    path('quem_somos_nos', quem_somos_nos, name='quem_somos_nos'),
    path('politica_de_privacidade', politica_de_privacidade, name='politica_de_privacidade'),
    path('politica_de_entrega', politica_de_entrega, name='politica_de_entrega'),
    path('trocas_e_devolucoes', trocas_e_devolucoes, name='trocas_e_devolucoes'),
    path('politicas_de_cancelamentos_e_ressarcimentos', politicas_de_cancelamentos_e_ressarcimentos,
         name='politicas_de_cancelamentos_e_ressarcimentos'),
    path('politica_de_venda_precos_ofertas_e_promocoes', politica_de_venda_precos_ofertas_e_promocoes,
         name='politica_de_venda_precos_ofertas_e_promocoes'),
    path('central_de_atendimento', central_de_atendimento, name='central_de_atendimento'),
    path('pagamento_sucesso', pagamento_sucesso, name='pagamento_sucesso'),
    path('pagamento_falha', pagamento_falha, name='pagamento_falha'),
]
