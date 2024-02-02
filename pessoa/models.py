from django.db import models

# Create your models here.

class Pessoa (models.Model):
    nome =  models.CharField(max_length=255)
    data_nascimento = models.DateField()
    data_inclusao = models.DateField()
    