from django.db import models


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


class Categoria(models.Model):
    nome = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    departamento = models.ForeignKey('Departamento', on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
