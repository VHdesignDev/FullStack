from django import forms
from .models import Cliente, Funcionario, Imovel, Locacao, FotoImovel, Ocorrencia


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'sobrenome',
            'email',
            'telefone',
            'observacoes',
            'endereco',
            'sexo',
        ]

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Nome',
            }),
            'sobrenome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Sobrenome',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Email',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Telefone',
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite as Observações',
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Endereço',
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'telefone',
            'email',
            'endereco',
        ]

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Nome',
            }),
            'sobrenome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Sobrenome',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o CPF ou CNPJ',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Telefone',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Email',
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Endereço',
            }),
        }


class ImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = [
            'endereco',
            'tipo',
            'numero_quartos',
            'metragem',
            'valor_aluguel',
            'obs',
        ]

        widgets = {
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Endereço',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'numero_quartos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Número de Quartos',
            }),
            'metragem': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a Metragem',
            }),
            'valor_aluguel': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Valor do Aluguel',
            }),
            'obs': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite as Observações',
            }),
        }


class LocacaoForm(forms.ModelForm):

    class Meta:
        model = Locacao
        fields = [
            'cliente',
            'imovel',
            'data_inicio',
            'duracao_meses',
        ]

        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-select'
            }),
            'imovel': forms.Select(attrs={
                'class': 'form-select'
            }),
            'data_inicio': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'duracao_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a duração em meses',
            }),
        }


class FotoImovelForm(forms.ModelForm):

    class Meta:
        model = FotoImovel
        fields = ['imagem']


class OcorrenciaForm(forms.ModelForm):

    class Meta:
        model = Ocorrencia
        fields = [
            'imovel',
            'descricao',
        ]

        widgets = {
            'imovel': forms.Select(attrs={
                'class': 'form-select'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descreva o problema (ex: vazamento no banheiro)',
            }),
        }
