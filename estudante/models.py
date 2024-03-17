from django.db import models
from django.db.models.functions import Now
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils import timezone
import uuid
from pessoa.models import Pessoa

# Create your models here.
class Matricula (models.Model):
    numero_matricula = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    data_inclusao = models.DateTimeField(db_default=Now())
    ativo = models.BooleanField(default=True)
    data_inativacao = models.DateTimeField(null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)

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