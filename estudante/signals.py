from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Atividade_teorica, Matricula, Psa
from datetime import timedelta, date

@receiver(post_save, sender=Matricula)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        data_inicio = instance.data_inicio_contrato
        quantidade_de_encontros = 12
        data_fim = data_inicio

        psas = Psa.objects.all()

        while quantidade_de_encontros > 0:
            data_fim += timedelta(days=1)
            is_feriado = any(psa.data_inicio <= data_fim <= psa.data_fim for psa in psas)
            if data_fim.weekday() >= 5 or is_feriado:
                continue
            quantidade_de_encontros -= 1

        Atividade_teorica.objects.create(
            matricula=instance,
            data_inicio=data_inicio,
            data_fim=data_fim,
            quantidade_de_encontros=12,
            hora_inicio=instance.turma.hora_inicio_encontro,
            hora_termino=instance.turma.hora_fim_encontro
        )