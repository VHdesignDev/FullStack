from django.contrib import admin
from .models import Funcionario, Imovel, Cliente, Locacao, FotoImovel, Ocorrencia

# Register your models here.


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email", "telefone", "sexo")


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ("endereco", "tipo", "numero_quartos",
                    "metragem", "valor_aluguel", "situacao")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "cpf", "telefone", "endereco")


@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "imovel", "data_inicio",
                    "duracao_meses", "status")


@admin.register(FotoImovel)
class FotoImovelAdmin(admin.ModelAdmin):
    list_display = ("imovel", "imagem", "data_cadastro")


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ("imovel", "descricao", "resolvida", "data_cadastro")
