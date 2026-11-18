from django.db import models

SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', "Outro"),
    ('N', "Não Informar"),
]

SITUACAO_CHOICES = [
    ('D', 'Disponível'),
    ('I', 'Indisponível'),
    ('A', 'Alugado'),
]
TIPO_CHOICES = [
    ('A', 'Apartamento'),
    ('C', 'Casa'),
    ('S', 'Sala Comercial'),
]
STATUS_LOCACAO_CHOICES = [
    ('P', 'Pendente'),
    ('A', 'Ativa'),
    ('F', 'Finalizada'),
    ('C', 'Cancelada'),
]


class Imovel(models.Model):
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    numero_quartos = models.IntegerField(
        null=True, verbose_name="Número de quartos")
    metragem = models.IntegerField(null=True, verbose_name="Metragem (m²)")
    valor_aluguel = models.FloatField(
        default=0.0, verbose_name="Valor do aluguel")
    obs = models.CharField(max_length=200, blank=True,
                           verbose_name="Observações")
    situacao = models.CharField(
        max_length=1, choices=SITUACAO_CHOICES, default='D', verbose_name="Situação")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.endereco

# noov model para inserção de imagens


class FotoImovel(models.Model):
    imovel = models.ForeignKey(
        Imovel, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='imoveis/')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Foto de {self.imovel}'


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=18, unique=True, verbose_name="CPF/CNPJ")
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, verbose_name="E-mail")
    endereco = models.CharField(
        max_length=200, null=True, verbose_name="Endereço")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome + " " + self.sobrenome

    def save(self, *args, **kwargs):
        self.nome = self.nome.title()
        self.sobrenome = self.sobrenome.title()
        self.email = self.email.lower()

        super().save(*args, **kwargs)


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    observacoes = models.TextField(blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome + " " + self.sobrenome

    def save(self, *args, **kwargs):
        self.nome = self.nome.title()
        self.sobrenome = self.sobrenome.title()
        self.email = self.email.lower()

        super().save(*args, **kwargs)


class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    imovel = models.ForeignKey(
        Imovel, on_delete=models.PROTECT, verbose_name="Imóvel")
    data_inicio = models.DateField(verbose_name="Data de início")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")
    status = models.CharField(
        max_length=1, choices=STATUS_LOCACAO_CHOICES, default='P')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cliente} - {self.imovel}'


class Ocorrencia(models.Model):
    imovel = models.ForeignKey(
        Imovel, on_delete=models.CASCADE, related_name='ocorrencias', verbose_name="Imóvel")
    descricao = models.TextField(verbose_name="Descrição do problema")
    resolvida = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ocorrência em {self.imovel}'
