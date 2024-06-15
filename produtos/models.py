from pyexpat import model
from django.db import models
from utils.base_models import BaseModel

class Categoria(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome da categoria', unique=True)

    class Meta:
        db_table = 'categorias'

class Produto(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome do produto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='categoria do produto')
    embalagens = models.ManyToManyField('produtos.Embalagem',verbose_name='Embalagens do produto')

    class Meta:
        db_table = 'produtos'

class Fornecedor(BaseModel):
    nome_social = models.CharField(max_length=100, verbose_name='Razao Social do fornecedor', unique=True)
    nome_fantasia = models.CharField(max_length=100, verbose_name='nome Fantasia do fornecedor')
    produtos =models.ManyToManyField(Produto, verbose_name='Produtos do Fornecedor',)
    
    
    class Meta:
        db_table = 'fornecedores'

class Embalagem(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Nome da embalagem')
    sigla = models.CharField(max_length=3,verbose_name='Sigla da embalagem')

    class Meta:
        db_table = 'embalagens'

class Movimentacao(BaseModel):
    TIPOS_MOVIMENTACAO =[(1, 'Entrada'), (-1, 'Saida'),]
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='produto da movimento')
    fornecedor = models.ForeignKey('produtos.Fornecedor', on_delete=models.CASCADE, verbose_name='Fornecedor do produto movimentado',)
    quantidade = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Quantidade movimentada')
    local = models.ForeignKey('produtos.Local', on_delete=models.CASCADE, verbose_name='Local da movimentação')
    tipo = models.IntegerField(choices=TIPOS_MOVIMENTACAO, verbose_name='Tipo de movimentação')

    class Meta:
        db_table = 'movimentacoes'

class Local(BaseModel):
    TIPOS_DE_LOCAL = [('F', 'Fisico'), ('D', 'Digital')]
    nome = models.CharField(max_length=50, verbose_name='Nome do local armazenado')
    tipo = models.CharField(max_length=1, choices=TIPOS_DE_LOCAL)

    class Meta:
        db_table = 'locais'



