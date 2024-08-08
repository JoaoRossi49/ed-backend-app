from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Pessoa, Perfil
from django.db.models.signals import post_save
from django.contrib.auth.models import User

@receiver(post_delete, sender=Pessoa)
def delete_related_objects(sender, instance, **kwargs):
    print('entrou em delete_related')
    print(instance.contato.all().count())
    print(instance.documento.all().count())
    for contato in instance.contato.all():
        print(contato)
        contato.delete()
    
    for documento in instance.documento.all():
        documento.delete()
    
    if instance.endereco:
        instance.endereco.delete()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()