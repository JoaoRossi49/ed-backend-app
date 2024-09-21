from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Atividade_teorica, Matricula
from datetime import timedelta

@receiver(post_save, sender=Matricula)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        data_inicio = instance.data_inicio_contrato
        quantidade_de_encontros = 12
        data_fim = data_inicio + timedelta(days=quantidade_de_encontros)

        Atividade_teorica.objects.create(
            matricula=instance,
            data_inicio=data_inicio,
            data_fim=data_fim,
            quantidade_de_encontros=quantidade_de_encontros,
            hora_inicio=instance.turma.hora_inicio_encontro,
            hora_termino=instance.turma.hora_fim_encontro
        )