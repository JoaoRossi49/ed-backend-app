# Generated by Django 5.0.2 on 2024-09-19 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0025_remove_atividade_teorica_dias_da_semana_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividade_teorica',
            old_name='qtd_encontros',
            new_name='quantidade_de_encontros',
        ),
    ]
