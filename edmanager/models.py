from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dashboard = models.BooleanField(null=True, blank=True, help_text="O usuário pode acessar o dashboard?")
    aprendizes = models.BooleanField(null=True, blank=True, help_text="O usuário pode acessar a tela de listagem de aprendizes?")
    matricular = models.BooleanField(null=True, blank=True, help_text="O usuário pode matricular novos aprendizes?")
    turmas = models.BooleanField(null=True, blank=True, help_text="O usuário pode acessar a tela de listagem de turmas?")
    diario_de_aula = models.BooleanField(null=True, blank=True, help_text="O usuário pode acessar o diário de aulas?")

    def __str__(self):
        return self.user.username
