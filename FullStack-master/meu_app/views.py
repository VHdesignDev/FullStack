from django.shortcuts import render, redirect
from .models import Funcionario, Imovel, Cliente, Locacao, FotoImovel, Ocorrencia
from .forms import FuncionarioForm, ImovelForm, ClienteForm, LocacaoForm, FotoImovelForm, OcorrenciaForm
from django.contrib import messages
from django.db.models.functions import Lower
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

# Create your views here.


@login_required
def index(request):

    ocorrencias_pendentes = Ocorrencia.objects.filter(
        resolvida=False).order_by('-data_cadastro')[:5]
    locacoes_pendentes = Locacao.objects.filter(
        status='P').order_by('data_inicio')[:5]

    dados = {
        'ocorrencias_pendentes': ocorrencias_pendentes,
        'locacoes_pendentes': locacoes_pendentes,
    }

    return render(request, "index.html", dados)


# ==================== GERIR FUNCIONÁRIOS ====================

@login_required
def cadastrar_funcionario(request):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem acessar esta página')
        return redirect('index')

    form = FuncionarioForm()

    dados = {
        'formulario': form
    }

    if request.method == 'POST':

        form = FuncionarioForm(request.POST)

        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']

            mensagem_confirmacao = f'Funcionário {nome} cadastrado com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_funcionarios')

    return render(request, "cadastrar_funcionario.html", dados)


@login_required
def listar_funcionarios(request):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem acessar esta página')
        return redirect('index')

    ordem = request.GET.get('ordem')
    nome_da_pesquisa = request.GET.get('nome_da_pesquisa', '')

    funcionarios = Funcionario.objects.filter(
        nome__icontains=nome_da_pesquisa,
        ativo=True
    ).order_by(Lower('nome'))

    if ordem == 'decrescente':
        funcionarios = Funcionario.objects.filter(
            nome__icontains=nome_da_pesquisa,
            ativo=True
        ).order_by(Lower('nome').desc())

    dados = {
        'funcionarios': funcionarios,
        'nome_da_pesquisa': nome_da_pesquisa,
    }

    return render(request, 'listar_funcionarios.html', dados)


@login_required
def editar_funcionario(request, id):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem acessar esta página')
        return redirect('index')

    funcionario = Funcionario.objects.get(id=id)

    form = FuncionarioForm(instance=funcionario)

    if request.method == 'POST':

        form = FuncionarioForm(request.POST, instance=funcionario)

        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']

            mensagem_confirmacao = f'Funcionário {nome} alterado com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_funcionarios')

    dados = {
        'formulario': form
    }

    return render(request, 'editar_funcionario.html', dados)


@login_required
def excluir_funcionario(request, id):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem acessar esta página')
        return redirect('index')

    funcionario = Funcionario.objects.get(id=id)

    nome = funcionario.nome
    sobrenome = funcionario.sobrenome

    funcionario.delete()

    mensagem = f'Funcionário {nome} {sobrenome} Excluído com sucesso'
    messages.success(request, mensagem)

    return redirect('listar_funcionarios')


@login_required
def desativar_funcionario(request, id):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem acessar esta página')
        return redirect('index')

    funcionario = Funcionario.objects.get(id=id)

    nome = funcionario.nome
    sobrenome = funcionario.sobrenome

    funcionario.ativo = False
    funcionario.save()

    mensagem = f'Funcionário {nome} {sobrenome} Desativado com sucesso'
    messages.success(request, mensagem)

    return redirect('listar_funcionarios')


@login_required
def funcionarios_inativos(request):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem acessar esta página')
        return redirect('index')

    funcionarios = Funcionario.objects.filter(
        ativo=False
    )

    dados = {
        'funcionarios': funcionarios
    }

    return render(request, 'funcionarios_inativos.html', dados)


@login_required
def ativar_funcionario(request, id):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem acessar esta página')
        return redirect('index')

    funcionario = Funcionario.objects.get(id=id)

    nome = funcionario.nome
    sobrenome = funcionario.sobrenome

    funcionario.ativo = True
    funcionario.save()

    mensagem = f'Funcionario {nome} {sobrenome} Ativado com Sucesso'
    messages.success(request, mensagem)

    return redirect('funcionarios_inativos')


# ==================== CADASTRAR IMÓVEL ====================

@login_required
def cadastrar_imovel(request):

    if request.method == 'POST':
        form = ImovelForm(request.POST)

        if form.is_valid():
            imovel = form.save()

            for arquivo in request.FILES.getlist('fotos'):
                FotoImovel.objects.create(imovel=imovel, imagem=arquivo)

            endereco = form.cleaned_data['endereco']

            mensagem_confirmacao = f'Imóvel {endereco} cadastrado com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('cadastrar_imovel')

    else:
        form = ImovelForm()

    dados = {
        'form': form,
    }

    return render(request, 'cadastrar_imovel.html', dados)


# ==================== GERENCIAR IMÓVEIS ====================

@login_required
def listar_imoveis(request):

    endereco_da_pesquisa = request.GET.get('endereco_da_pesquisa', '')

    imoveis = Imovel.objects.filter(
        endereco__icontains=endereco_da_pesquisa
    ).order_by(Lower('endereco'))

    dados = {
        'imoveis': imoveis,
        'endereco_da_pesquisa': endereco_da_pesquisa,
    }

    return render(request, 'listar_imoveis.html', dados)


@login_required
def editar_imovel(request, id):

    imovel = Imovel.objects.get(id=id)

    form = ImovelForm(instance=imovel)

    if request.method == 'POST':

        form = ImovelForm(request.POST, instance=imovel)

        if form.is_valid():
            form.save()
            endereco = form.cleaned_data['endereco']

            mensagem_confirmacao = f'Imóvel {endereco} alterado com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_imoveis')

    dados = {
        'form': form
    }

    return render(request, 'editar_imovel.html', dados)


@login_required
def excluir_imovel(request, id):

    imovel = Imovel.objects.get(id=id)

    endereco = imovel.endereco

    if Locacao.objects.filter(imovel=imovel, status__in=['P', 'A']).exists():
        mensagem = f'O imóvel {endereco} possui locação ativa e não pode ser excluído'
        messages.error(request, mensagem)

        return redirect('listar_imoveis')

    imovel.delete()

    mensagem = f'Imóvel {endereco} excluído com sucesso'
    messages.success(request, mensagem)

    return redirect('listar_imoveis')


@login_required
def fotos_imovel(request, id):

    imovel = Imovel.objects.get(id=id)

    if request.method == 'POST':
        form = FotoImovelForm(request.POST, request.FILES)

        if form.is_valid():
            foto = form.save(commit=False)
            foto.imovel = imovel
            foto.save()

            messages.success(request, 'Foto adicionada com sucesso!')

            return redirect('fotos_imovel', id=imovel.id)

    else:
        form = FotoImovelForm()

    dados = {
        'form': form,
        'imovel': imovel,
    }

    return render(request, 'fotos_imovel.html', dados)


@login_required
def bloquear_imovel(request, id):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem bloquear imóveis')
        return redirect('listar_imoveis')

    imovel = Imovel.objects.get(id=id)

    if imovel.situacao == 'A':
        mensagem = f'O imóvel {imovel.endereco} está alugado e não pode ser bloqueado'
        messages.error(request, mensagem)
        return redirect('listar_imoveis')

    imovel.situacao = 'I'
    imovel.save()

    mensagem = f'Imóvel {imovel.endereco} bloqueado com sucesso'
    messages.success(request, mensagem)

    return redirect('listar_imoveis')


@login_required
def desbloquear_imovel(request, id):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem desbloquear imóveis')
        return redirect('listar_imoveis')

    imovel = Imovel.objects.get(id=id)

    imovel.situacao = 'D'
    imovel.save()

    mensagem = f'Imóvel {imovel.endereco} desbloqueado com sucesso'
    messages.success(request, mensagem)

    return redirect('listar_imoveis')


@login_required
def pesquisar_imoveis(request):

    localizacao = request.GET.get('localizacao', '')
    tipo = request.GET.get('tipo', '')
    quartos = request.GET.get('quartos', '')
    valor_maximo = request.GET.get('valor_maximo', '')

    imoveis = Imovel.objects.filter(
        situacao='D',
        endereco__icontains=localizacao
    ).order_by(Lower('endereco'))

    if tipo:
        imoveis = imoveis.filter(tipo=tipo)

    if quartos:
        imoveis = imoveis.filter(numero_quartos=quartos)

    if valor_maximo:
        imoveis = imoveis.filter(valor_aluguel__lte=valor_maximo)

    dados = {
        'imoveis': imoveis,
        'localizacao': localizacao,
        'tipo': tipo,
        'quartos': quartos,
        'valor_maximo': valor_maximo,
    }

    return render(request, 'pesquisar_imoveis.html', dados)


@login_required
def detalhes_imovel(request, id):

    imovel = Imovel.objects.get(id=id)

    dados = {
        'imovel': imovel,
    }

    return render(request, 'detalhes_imovel.html', dados)

# ==================== GERENCIAR CLIENTES ====================


@login_required
def cadastrar_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']

            mensagem_confirmacao = f'Cliente {nome} cadastrado com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_clientes')

    else:
        form = ClienteForm()

    dados = {
        'form': form,
    }

    return render(request, 'cadastrar_cliente.html', dados)


@login_required
def listar_clientes(request):

    nome_da_pesquisa = request.GET.get('nome_da_pesquisa', '')

    clientes = Cliente.objects.filter(
        nome__icontains=nome_da_pesquisa
    ).order_by(Lower('nome'))

    dados = {
        'clientes': clientes,
        'nome_da_pesquisa': nome_da_pesquisa,
    }

    return render(request, 'listar_clientes.html', dados)


@login_required
def editar_cliente(request, id):

    cliente = Cliente.objects.get(id=id)

    form = ClienteForm(instance=cliente)

    if request.method == 'POST':

        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']

            mensagem_confirmacao = f'Cliente {nome} alterado com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_clientes')

    dados = {
        'form': form
    }

    return render(request, 'editar_cliente.html', dados)

# ==================== LOCAÇÕES ====================


@login_required
def criar_locacao(request):

    if request.method == 'POST':
        form = LocacaoForm(request.POST)

        if form.is_valid():
            locacao = form.save()

            imovel = locacao.imovel
            imovel.situacao = 'A'
            imovel.save()

            mensagem_confirmacao = f'Locação do imóvel {imovel.endereco} criada com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_locacoes')

    else:
        form = LocacaoForm()

    form.fields['imovel'].queryset = Imovel.objects.filter(situacao='D')

    dados = {
        'form': form,
    }

    return render(request, 'criar_locacao.html', dados)


@login_required
def listar_locacoes(request):

    pesquisa = request.GET.get('pesquisa', '')
    status = request.GET.get('status', '')

    locacoes = Locacao.objects.filter(
        imovel__endereco__icontains=pesquisa
    ).order_by('-data_cadastro')

    if status:
        locacoes = locacoes.filter(status=status)

    dados = {
        'locacoes': locacoes,
        'pesquisa': pesquisa,
        'status': status,
    }

    return render(request, 'listar_locacoes.html', dados)


@login_required
def ativar_locacao(request, id):

    locacao = Locacao.objects.get(id=id)

    locacao.status = 'A'
    locacao.save()

    mensagem = f'Entrada no imóvel {locacao.imovel.endereco} confirmada'
    messages.success(request, mensagem)

    return redirect('listar_locacoes')


@login_required
def finalizar_locacao(request, id):

    locacao = Locacao.objects.get(id=id)

    locacao.status = 'F'
    locacao.save()

    imovel = locacao.imovel
    imovel.situacao = 'D'
    imovel.save()

    mensagem = f'Locação do imóvel {imovel.endereco} finalizada com sucesso'
    messages.success(request, mensagem)

    return redirect('listar_locacoes')


@login_required
def cancelar_locacao(request, id):

    locacao = Locacao.objects.get(id=id)

    if locacao.status != 'P':
        messages.error(request, 'Só é possível cancelar locações pendentes')
        return redirect('listar_locacoes')

    locacao.status = 'C'
    locacao.save()

    imovel = locacao.imovel
    imovel.situacao = 'D'
    imovel.save()

    mensagem = f'Locação do imóvel {imovel.endereco} cancelada com sucesso'
    messages.success(request, mensagem)

    return redirect('listar_locacoes')

# ==================== OCORRÊNCIAS ====================


@login_required
def registrar_ocorrencia(request):

    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)

        if form.is_valid():
            form.save()
            imovel = form.cleaned_data['imovel']

            mensagem_confirmacao = f'Ocorrência no imóvel {imovel} registrada! A equipe foi notificada.'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_ocorrencias')

    else:
        form = OcorrenciaForm()

    dados = {
        'form': form,
    }

    return render(request, 'registrar_ocorrencia.html', dados)


@login_required
def listar_ocorrencias(request):

    pendentes = Ocorrencia.objects.filter(
        resolvida=False).order_by('-data_cadastro')
    resolvidas = Ocorrencia.objects.filter(
        resolvida=True).order_by('-data_cadastro')

    dados = {
        'pendentes': pendentes,
        'resolvidas': resolvidas,
    }

    return render(request, 'listar_ocorrencias.html', dados)


@login_required
def resolver_ocorrencia(request, id):

    ocorrencia = Ocorrencia.objects.get(id=id)

    ocorrencia.resolvida = True
    ocorrencia.save()

    mensagem = f'Ocorrência no imóvel {ocorrencia.imovel} marcada como resolvida'
    messages.success(request, mensagem)

    return redirect('listar_ocorrencias')

# ==================== RELATÓRIOS ====================


@login_required
def gerar_relatorio(request):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem gerar relatórios')
        return redirect('index')

    tipo = request.GET.get('tipo', '')
    status = request.GET.get('status', '')

    locacoes = Locacao.objects.all().order_by('data_inicio')

    if tipo:
        locacoes = locacoes.filter(imovel__tipo=tipo)

    if status:
        locacoes = locacoes.filter(status=status)

    dados = {
        'locacoes': locacoes,
        'tipo': tipo,
        'status': status,
    }

    return render(request, 'relatorio_locacoes.html', dados)

# ==================== USUÁRIOS E LOGIN ====================


@login_required
def cadastrar_usuario(request):

    if not request.user.is_superuser:
        messages.error(
            request, 'Apenas administradores podem acessar esta página')
        return redirect('index')

    if request.method == 'POST':
        formulario_de_usuario = UserCreationForm(request.POST)

        if formulario_de_usuario.is_valid():
            formulario_de_usuario.save()
            usuario = formulario_de_usuario.cleaned_data['username']
            mensagem_confirmacao = f'Usuário {usuario} cadastrado com sucesso!'
            messages.success(request, mensagem_confirmacao)
            return redirect('cadastrar_usuario')
    else:
        formulario_de_usuario = UserCreationForm()

    dados = {
        'formulario': formulario_de_usuario
    }

    return render(request, 'cadastrar_usuario.html', dados)


def sair(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('index')


class AlterarSenhaView(PasswordChangeView):
    template_name = 'alterar_senha.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Senha alterada com sucesso!')
        return super().form_valid(form)
