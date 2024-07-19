from django.db import models
from django.utils import timezone
from datetime import date

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
    ("CNS", "Cartão nacional de saúde"),
    ("CNPJ", "Cadastro Nacional da Pessoa Jurídica")
)

class Contato(models.Model):
    tipo_contato = models.CharField(max_length=10, choices=TIPOS_CONTATO_CHOICES)
    descricao = models.CharField(max_length=255)
    data_inclusao = models.DateTimeField(default=timezone.now)
    data_alteracao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.descricao

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=9)
    data_inclusao = models.DateTimeField(default=timezone.now)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=80, null=True)
    estado = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}"
    
class Documento(models.Model):
    nro_documento = models.CharField(max_length=60)
    data_inclusao = models.DateTimeField(default=timezone.now)
    tipo_documento = models.CharField(max_length=40, choices=TIPOS_DOCUMENTO_CHOICES)

class Tipo_pessoa(models.Model):
    descricao = models.CharField(max_length=40)
    def __str__(self):
        return self.descricao
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField()
    data_inclusao = models.DateTimeField(default=timezone.now)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)
    contato = models.ManyToManyField(Contato, related_name='pessoas', blank=True)
    documento = models.ManyToManyField(Documento,  related_name='pessoas', blank=True)
    
    def __str__(self):
        if self.nome:
            return self.nome
        else:
            return self.nome_social


    def calcular_idade(self):
        hoje = date.today()
        anos = hoje.year - self.data_nascimento.year
        meses = hoje.month - self.data_nascimento.month
        
        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"