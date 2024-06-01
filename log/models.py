from django.db import models
from django.contrib.auth.models import User

TIPOS_EVENTO_ACESSO_CHOICES = (
    ("F", "Falha ao acessar"),
    ("S", "Sucesso ao acessar")
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