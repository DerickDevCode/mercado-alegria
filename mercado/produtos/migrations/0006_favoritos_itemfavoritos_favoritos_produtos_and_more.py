# Generated by Django 5.0.2 on 2024-06-20 01:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_adicionado_meta_unique_constraint_aos_campos_carrinho_e_produto_do_modelo_carrinhoitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemFavoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favoritos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.favoritos')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
        migrations.AddField(
            model_name='favoritos',
            name='produtos',
            field=models.ManyToManyField(through='produtos.ItemFavoritos', to='produtos.produto'),
        ),
        migrations.AddConstraint(
            model_name='itemfavoritos',
            constraint=models.UniqueConstraint(fields=('favoritos', 'produto'), name='unique_favorito__produto'),
        ),
    ]