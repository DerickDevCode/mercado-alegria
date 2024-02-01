from django.urls import path

from mercado.produtos.views import produto

app_name = 'produtos'
urlpatterns = [
    path('', produto, name='produto'),
]

# formato da url para implementar <slug:departamento>/<slug:categoria>/<slug:produto>
