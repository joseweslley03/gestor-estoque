from tabnanny import verbose
from django.db import models

from utils.base_models import BaseModel


class Categoria(BaseModel):
    nome = models.CharField(
        max_length=100, verbose_name='nome da categoria', unique=True
    )  # noqa: E501

    class Meta:
        db_table = 'categorias'


class Produto(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome do produto')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        verbose_name='categoria do produto',
    )  # noqa: E501
    embalagens = models.ManyToManyField(
        'produtos.Embalagem', verbose_name='Embalagens do produto'
    )  # noqa: E501
    estoque_minimo = models.FloatField(
        verbose_name='estoque minimo do produto',
    )
    estoque_maximo = models.FloatField(
        verbose_name='estoque maximo do produto',
    )

    class Meta:
        db_table = 'produtos'


class Fornecedor(BaseModel):
    nome_social = models.CharField(
        max_length=100, verbose_name='Razao Social do fornecedor', unique=True
    )  # noqa: E501
    nome_fantasia = models.CharField(
        max_length=100, verbose_name='nome Fantasia do fornecedor'
    )  # noqa: E501
    produtos = models.ManyToManyField(
        Produto,
        verbose_name='Produtos do Fornecedor',
    )  # noqa: E501

    class Meta:
        db_table = 'fornecedores'


class Embalagem(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Nome da embalagem')
    sigla = models.CharField(max_length=3, verbose_name='Sigla da embalagem')

    class Meta:
        db_table = 'embalagens'


class Movimentacao(BaseModel):
    TIPOS_MOVIMENTACAO = [
        (1, 'Entrada'),
        (-1, 'Saida'),
    ]
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, verbose_name='produto da movimento'
    )  # noqa: E501
    fornecedor = models.ForeignKey(
        'produtos.Fornecedor',
        on_delete=models.CASCADE,
        verbose_name='Fornecedor do produto movimentado',
    )  # noqa: E501
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=6, verbose_name='Quantidade movimentada'
    )  # noqa: E501
    local = models.ForeignKey(
        'produtos.Local',
        on_delete=models.CASCADE,
        verbose_name='Local da movimentação',
    )  # noqa: E501
    tipo = models.IntegerField(
        choices=TIPOS_MOVIMENTACAO, verbose_name='Tipo de movimentação'
    )  # noqa: E501
    preco = models.DecimalField(
        max_digits = 10,
        decimal_places = 6,
        verbose_name='Preço do produto na movimentação'
    )
    codigo_fabricante = models.CharField(
        max_length=50,
        verbose_name='Código do fabricante'
    )

    class Meta:
        db_table = 'movimentacoes'


class Local(BaseModel):
    TIPOS_DE_LOCAL = [('F', 'Fisico'), ('D', 'Digital')]
    nome = models.CharField(
        max_length=50, verbose_name='Nome do local armazenado'
    )  # noqa: E501
    tipo = models.CharField(max_length=1, choices=TIPOS_DE_LOCAL)

    class Meta:
        db_table = 'locais'
