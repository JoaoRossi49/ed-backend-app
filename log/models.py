from django.db import models
from django.contrib.auth.models import User

TIPOS_EVENTO_ACESSO_CHOICES = (
    ("F", "Falha ao acessar"),
    ("S", "Sucesso ao acessar")
)

TIPOS_EVENTO_CADASTRO_CHOICES = (
    ("N", "Criação de registro"),
    ("A", "Alteração de registro"),
    ("R", "Remoção de registro")
)

class Acesso(models.Model):
    data_inclusao = models.DateTimeField(auto_now_add=True)
    tipo_evento = models.CharField(max_length=10, choices=TIPOS_EVENTO_ACESSO_CHOICES)
    user = models.CharField()
    ip = models.CharField(max_length=15)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tentativas = models.IntegerField(default=0)
    bloqueado = models.BooleanField(default=False)

class Cadastro(models.Model):
    data_inclusao = models.DateTimeField(auto_now_add=True)
    tipo_evento = models.CharField(max_length=10, choices=TIPOS_EVENTO_CADASTRO_CHOICES)
    model_afetada = models.CharField(max_length=50)
    detalhes = models.TextField(null=True)