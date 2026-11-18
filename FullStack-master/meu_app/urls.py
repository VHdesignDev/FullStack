from django.urls import path
from meu_app import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),

    # Gerir Funcionários
    path('cadastrar_funcionario/', views.cadastrar_funcionario,
         name="cadastrar_funcionario"),
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('editar_funcionario/<int:id>/',
         views.editar_funcionario, name='editar_funcionario'),
    path('excluir_funcionario/<int:id>/',
         views.excluir_funcionario, name='excluir_funcionario'),
    path('desativar_funcionario/<int:id>/',
         views.desativar_funcionario, name='desativar_funcionario'),
    path('funcionarios_inativos/', views.funcionarios_inativos,
         name='funcionarios_inativos'),
    path('ativar_funcionario/<int:id>/',
         views.ativar_funcionario, name='ativar_funcionario'),

    # Imóveis
    path('cadastrar_imovel/', views.cadastrar_imovel, name='cadastrar_imovel'),
    path('imoveis/', views.listar_imoveis, name='listar_imoveis'),
    path('editar_imovel/<int:id>/', views.editar_imovel, name='editar_imovel'),
    path('excluir_imovel/<int:id>/', views.excluir_imovel, name='excluir_imovel'),
    path('fotos_imovel/<int:id>/', views.fotos_imovel, name='fotos_imovel'),
    path('bloquear_imovel/<int:id>/',
         views.bloquear_imovel, name='bloquear_imovel'),
    path('desbloquear_imovel/<int:id>/',
         views.desbloquear_imovel, name='desbloquear_imovel'),
    path('pesquisar_imoveis/', views.pesquisar_imoveis, name='pesquisar_imoveis'),
    path('detalhes_imovel/<int:id>/',
         views.detalhes_imovel, name='detalhes_imovel'),

    # Clientes
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),

    # Locações
    path('criar_locacao/', views.criar_locacao, name='criar_locacao'),
    path('locacoes/', views.listar_locacoes, name='listar_locacoes'),
    path('ativar_locacao/<int:id>/', views.ativar_locacao, name='ativar_locacao'),
    path('finalizar_locacao/<int:id>/',
         views.finalizar_locacao, name='finalizar_locacao'),
    path('cancelar_locacao/<int:id>/',
         views.cancelar_locacao, name='cancelar_locacao'),

    # Usuários e Login
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.sair, name='logout'),
    path('alterar_senha/', views.AlterarSenhaView.as_view(), name='alterar_senha'),

    # Ocorrências
    path('registrar_ocorrencia/', views.registrar_ocorrencia,
         name='registrar_ocorrencia'),
    path('ocorrencias/', views.listar_ocorrencias, name='listar_ocorrencias'),
    path('resolver_ocorrencia/<int:id>/',
         views.resolver_ocorrencia, name='resolver_ocorrencia'),

    # Relatórios
    path('relatorio/', views.gerar_relatorio, name='gerar_relatorio'),
]
