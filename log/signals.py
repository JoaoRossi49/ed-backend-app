from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Cadastro
import json
from pessoa.models import Pessoa, Contato, Endereco, Documento
from datetime import date, datetime

def custom_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@receiver(pre_save, sender=Contato)
@receiver(pre_save, sender=Endereco)
@receiver(pre_save, sender=Pessoa)
@receiver(pre_save, sender=Documento)
def capture_previous_state(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            instance._previous_state = old_instance.__dict__.copy()
        except sender.DoesNotExist:
            instance._previous_state = None

@receiver(post_save, sender=Contato)
@receiver(post_save, sender=Endereco)
@receiver(post_save, sender=Pessoa)
@receiver(post_save, sender=Documento)
def create_or_update_log(sender, instance, created, **kwargs):
    if created:
        tipo_evento = "N"
        valor_anterior = None
    else:
        tipo_evento = "A"
        valor_anterior = instance._previous_state

    valor_atual = instance.__dict__.copy()
    valor_atual.pop('_state', None)  # Remove Django internal attribute
    if valor_anterior:
        valor_anterior.pop('_state', None)

    Cadastro.objects.create(
        tipo_evento=tipo_evento,
        model_afetada=sender.__name__,
        detalhes=json.dumps({
            'old': valor_anterior,
            'new': valor_atual
        }, default=custom_serializer)
    )

@receiver(post_delete, sender=Contato)
@receiver(post_delete, sender=Endereco)
@receiver(post_delete, sender=Pessoa)
@receiver(post_delete, sender=Documento)
def delete_log(sender, instance, **kwargs):
    data = instance.__dict__.copy()
    data.pop('_state', None)

    Cadastro.objects.create(
        tipo_evento="R",
        model_afetada=sender.__name__,
        detalhes=json.dumps({
            'old': data,
            'new': None
        }, default=custom_serializer)
    )
