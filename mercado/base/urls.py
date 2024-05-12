from django.urls import path

from mercado.base.views import home, cadastro, perfil

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
]
