# Generated by Django 5.0.2 on 2024-03-17 23:40

import estudante.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='numero_matricula',
            field=models.CharField(default=estudante.models.generar_matricula, max_length=6, unique=True),
        ),
    ]