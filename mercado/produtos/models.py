from django.db import models
from django.urls import reverse


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    marca = models.CharField(max_length=64)
    codigo = models.CharField(max_length=20, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='imagens_produtos/')
    descricao = models.TextField(null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos:produto', args=(self.categoria.departamento.slug,
                                                 self.categoria.slug,
                                                 self.slug,))


class Categoria(models.Model):
    nome = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    departamento = models.ForeignKey('Departamento', on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos:pagina_de_categorias', args=(self.departamento.slug, self.slug))


class Departamento(models.Model):
    nome = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos:pagina_de_departamentos', args=(self.slug,))
