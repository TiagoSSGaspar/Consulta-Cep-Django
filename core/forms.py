from django import forms
from .models import Endereco


class EnderecoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs.update({'class': 'form-control'}) #, 'onblur':'pesquisacep(this.value);'
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control'})
        self.fields['complemento'].widget.attrs.update({'class': 'form-control'})
        self.fields['bairro'].widget.attrs.update({'class': 'form-control'})
        self.fields['cidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['uf'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Endereco
        fields = [
            'cep',
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'uf',
            'descricao'
        ]
