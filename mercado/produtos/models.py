from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE, UniqueConstraint
from django.urls import reverse


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    marca = models.CharField(max_length=64)
    codigo = models.CharField(max_length=20, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='imagens_produtos/')
    descricao = models.TextField(null=True)
    subcategoria = models.ForeignKey('Subcategoria', on_delete=models.PROTECT, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos:produto', args=(self.subcategoria.categoria.departamento.slug,
                                                 self.subcategoria.categoria.slug,
                                                 self.subcategoria.slug,
                                                 self.slug,))


class Subcategoria(models.Model):
    nome = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos:pagina_de_subcategorias',
                       args=(self.categoria.departamento.slug, self.categoria.slug, self.slug))


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


class Carrinho(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    produtos = models.ManyToManyField(Produto, through='CarrinhoItem')

    def __str__(self):
        produtos = [item.nome for item in self.produtos.all()]
        return f'{self.user.id}: ({produtos})'


class CarrinhoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=CASCADE)
    quantidade = models.PositiveSmallIntegerField(default=1)

    @property
    def total(self):
        return self.quantidade * self.produto.preco

    def __str__(self):
        return self.produto.nome

    class Meta:
        constraints = [
            UniqueConstraint(fields=['carrinho', 'produto'], name="unique_carrinho__produto")
        ]


class Favoritos(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemFavoritos')

    def __str__(self):
        produtos = [item.nome for item in self.produtos.all()]
        return f'{self.user.id}: ({produtos})'


class ItemFavoritos(models.Model):
    produto = models.ForeignKey(Produto, on_delete=CASCADE)
    favoritos = models.ForeignKey(Favoritos, on_delete=CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['favoritos', 'produto'], name="unique_favorito__produto")
        ]
