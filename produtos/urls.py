from django.urls import path

from .views import (
    adicionar_categorias,
    adicionar_embalagem,
    adicionar_fornecedores,
    adicionar_local,
    adicionar_produtos,
    editar_categorias,
    editar_embalagem,
    editar_fornecedores,
    editar_local,
    editar_produtos,
    excluir_categorias,
    excluir_embalagem,
    excluir_fornecedores,
    excluir_local,
    excluir_produtos,
    inicio,
    listar_categorias,
    listar_embalagem,
    listar_fornecedores,
    listar_locais,
    listar_produtos,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagem/', listar_embalagem, name='listar_embalagem'),
    path('embalagem/adicionar/', adicionar_embalagem, name='adicionar_embalagem'),  # noqa: E501
    path('editar_local/<pk>/', editar_local, name='editar_local'),
    path('excluir_local/<pk>/', excluir_local, name='excluir_local'),
    path('editar_embalagem/<pk>/', editar_embalagem, name='editar_embalagem'),
    path('excluir_embalagem/<pk>/', excluir_embalagem, name='excluir_embalagem'),  # noqa: E501
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', adicionar_categorias, name='adicionar_categorias'),  # noqa: E501
    path('editar_categorias/<pk>/', editar_categorias, name='editar_categorias'),  # noqa: E501
    path('excluir_categorias/<pk>/', excluir_categorias, name='excluir_categorias'),  # noqa: E501
    path('fornecedores/', listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/adicionar/', adicionar_fornecedores, name='adicionar_fornecedores'),  # noqa: E501
    path('editar_fornecedores/<pk>/', editar_fornecedores, name='editar_fornecedores'),  # noqa: E501
    path('excluir_fornecedores/<pk>/', excluir_fornecedores, name='excluir_fornecedores'),  # noqa: E501
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', adicionar_produtos, name='adicionar_produtos'),  # noqa: E501
    path('editar_produtos/<pk>/', editar_produtos, name='editar_produtos'),  # noqa: E501
    path('excluir_produtos/<pk>/', excluir_produtos, name='excluir_produtos'),  # noqa: E501

]
