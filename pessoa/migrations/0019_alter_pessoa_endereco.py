# Generated by Django 5.0.2 on 2024-10-02 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0018_alter_contato_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='endereco',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.endereco'),
        ),
    ]
