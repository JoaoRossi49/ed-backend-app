from django.db import models
from django.db.models.functions import Now

# Choices
TIPOS_CONTATO_CHOICES = (
    ("CELULAR", "Celular"),
    ("TELEFONE", "Telefone"),
    ("EMAIL", "E-mail")
)

TIPOS_DOCUMENTO_CHOICES = (
    ("RG", "Documento de identidade"),
    ("CPF", "Cadastro de pessoa física"),
    ("CTPS", "Carteira nacional de trabalho"),
    ("PASS", "Passaporte"),
    ("CNH", "Carteira de motorista"),
    ("EL", "Título de eleitor"),
    ("CNS", "Cartão nacional de saúde")
)

RELACOES_CHOICES = (
    ("PAI", "Pai"),
    ("MÃE", "Mãe"),
    ("FILHO", "Filho"),
    ("FILHA", "Filha"),
    ("IRMÃO", "Irmão"),
    ("IRMÃ", "Irmã"),
    ("AVÔ", "Avô"),
    ("AVÓ", "Avó"),
    ("TIO", "Tio"),
    ("TIA", "Tia"),
    ("PRIMO", "Primo"),
    ("PRIMA", "Prima"),
    ("SOGRO", "Sogro"),
    ("SOGRA", "Sogra"),
    ("GENRO", "Genro"),
    ("NORA", "Nora"),
    ("MARIDO", "Marido"),
    ("ESPOSA", "Esposa"),
    ("SOBRINHO", "Sobrinho"),
    ("SOBRINHA", "Sobrinha"),
    ("NETO", "Neto"),
    ("NETA", "Neta"),
    ("PAI_ADOTIVO", "Pai Adotivo"),
    ("MÃE_ADOTIVA", "Mãe Adotiva"),
    ("FILHO_ADOTIVO", "Filho Adotivo"),
    ("FILHA_ADOTIVA", "Filha Adotiva")
)

class Contato(models.Model):
    tipo_contato = models.CharField(max_length=10, choices=TIPOS_CONTATO_CHOICES)
    descricao = models.CharField(max_length=255)
    data_inclusao = models.DateTimeField(default=Now)
    data_alteracao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.descricao

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=9)
    data_inclusao = models.DateTimeField(default=Now)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=80, null=True)
    estado = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}"

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField()
    data_inclusao = models.DateTimeField(default=Now)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True)
    contato = models.ManyToManyField(Contato, blank=True)

    def __str__(self):
        return self.nome_social if self.nome_social else self.nome

class Relacao(models.Model):
    pessoa_pai = models.ForeignKey(Pessoa, related_name='relacoes_pai', on_delete=models.CASCADE)
    pessoa_filho = models.ForeignKey(Pessoa, related_name='relacoes_filho', on_delete=models.CASCADE)
    tipo_relacao = models.CharField(max_length=40, choices=RELACOES_CHOICES)

class Documento(models.Model):
    nro_documento = models.CharField(max_length=60)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inclusao = models.DateTimeField(default=Now)
    tipo_documento = models.CharField(max_length=40, choices=TIPOS_DOCUMENTO_CHOICES)
