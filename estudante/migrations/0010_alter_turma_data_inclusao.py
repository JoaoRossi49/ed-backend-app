# Generated by Django 5.0.2 on 2024-06-14 21:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0009_alter_matricula_data_inclusao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='data_inclusao',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
