# Generated by Django 5.0.2 on 2024-06-09 18:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0004_turma_aula_data_aula_aula_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='data_inclusao',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
