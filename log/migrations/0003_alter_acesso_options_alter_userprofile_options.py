# Generated by Django 5.0.2 on 2024-07-20 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_cadastro_alter_acesso_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acesso',
            options={'verbose_name': 'Acesso ao sistema', 'verbose_name_plural': 'Acessos ao sistema'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'um Usuário Bloqueado', 'verbose_name_plural': 'Usuários bloqueados'},
        ),
    ]
