from django import forms

from .models import Categoria, Embalagem, Fornecedor, Local, Produto


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'tipo']

class EmbalagemForm(forms.ModelForm):
    class Meta:
        model = Embalagem
        fields = ['nome', 'sigla']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_social', 'nome_fantasia', 'produtos']

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'embalagens', 'estoque_minimo', 'estoque_maximo']  # noqa: E501