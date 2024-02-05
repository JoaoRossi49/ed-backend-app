from django.db import models

# Create your models here.
class Contato (models.Model):
    tipo_contato = models.CharField(max_length=1)
    descricao = models.CharField(max_length=255)
    pass

class Pessoa (models.Model):
    nome =  models.CharField(max_length=255)
    data_nascimento = models.DateField()
    data_inclusao = models.DateField()
    endereco = models.ForeignKey("pessoa.Endereco", verbose_name=("Endereco"), on_delete=models.CASCADE, null=True, blank=True)
    contato = models.ManyToManyField(Contato)
    
class Endereco (models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    
