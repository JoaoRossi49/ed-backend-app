from django.db import models
from django.db.models.functions import Now

#Alimentação de listas para choices
TIPOS_CONTATO_CHOICES = (
    ("CELULAR", "Celular"),
    ("TELEFONE", "Telefone"),
    ("EMAIL", "E-mail")
)

TIPOS_DOCUMENTO_CHOICES = (
    ("RG", "Documento de identidade"),
    ("CPF", "Cadastro de pessoa física"),
    ("CTPS", "Carteira nascional de trabalho"),
    ("PASS", "Passaporte"),
    ("CNH", "Carteira de motorista"),
    ("EL", "Título de eleitor"),
    ("CNS", "Cartão nascional de saúde")
)

RELACOES_FAMILIARES_CHOICES = (
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
    ("SOGRa", "Sogra"),
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


# Criação de models
class Contato (models.Model):
    id = models.AutoField
    tipo_contato = models.CharField(max_length=10, choices=TIPOS_CONTATO_CHOICES)
    descricao = models.CharField(max_length=255)
    data_inclusao = models.DateTimeField(db_default=Now())
    pass

class Pessoa (models.Model):
    nome =  models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, null=True)
    data_nascimento = models.DateField()
    data_inclusao = models.DateTimeField(db_default=Now())
    endereco = models.ForeignKey("pessoa.Endereco", verbose_name=("Endereco"), on_delete=models.CASCADE, null=True, blank=True)
    contato = models.ManyToManyField("pessoa.Contato")

class Relacao_familiar(models.Model):
    pessoa_pai = models.ForeignKey("pessoa.pessoa", related_name='relacoes_pai', on_delete=models.CASCADE)
    pessoa_filho = models.ForeignKey("pessoa.pessoa", related_name='relacoes_filho', on_delete=models.CASCADE)
    tipo_relacao = models.CharField(max_length=40, choices=RELACOES_FAMILIARES_CHOICES)
    
class Endereco (models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=9)
    data_inclusao = models.DateTimeField(db_default=Now())
    complemento = models.CharField(max_length=255, null=True)
    cidade= models.CharField(max_length=80, null=True)
    estado= models.CharField(max_length=50, null=True)
    pais= models.CharField(max_length=50, null=True)

class Documento (models.Model):
    nro_documento = models.CharField(max_length=60)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inclusao = models.DateTimeField(db_default=Now())
    tipo_documento = models.CharField(max_length=40, choices=TIPOS_DOCUMENTO_CHOICES)
