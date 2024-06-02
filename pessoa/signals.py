from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Pessoa

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