from django.db import models
from django.db.models.functions import Now
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils import timezone
import random
from pessoa.models import Pessoa

def generar_matricula():
    matricula = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    while Matricula.objects.filter(numero_matricula=matricula).exists():
        matricula = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return matricula


class Matricula (models.Model):
    numero_matricula = models.CharField(max_length=6, unique=True, default=generar_matricula)
    data_inclusao = models.DateTimeField(db_default=Now())
    ativo = models.BooleanField(default=True)
    data_inativacao = models.DateTimeField(null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.numero_matricula

class Aula (models.Model):
    tema = models.CharField(max_length=250)
    descricao = models.CharField()
    #anexos = models.B
    
class Presenca (models.Model):
    estudante_id = models.ForeignKey(Matricula, on_delete=models.CASCADE, null=True)
    data_hora_chegada = models.DateTimeField(db_default=Now())
    aula_id = models.ForeignKey(Aula, on_delete = models.CASCADE)
    
@receiver(pre_save, sender=Matricula)
def update_data_inativacao(sender, instance, **kwargs):
    if instance.pk:
        original_instance = sender.objects.get(pk=instance.pk)
        if original_instance.ativo != instance.ativo:
            if instance.ativo:
                instance.data_inativacao = timezone.now()
            else:
                instance.data_inativacao = None
    elif instance.ativo:
        instance.data_inativacao = timezone.now()
