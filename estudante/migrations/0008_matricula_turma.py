# Generated by Django 5.0.2 on 2024-06-10 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0007_alter_turma_data_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estudante.turma'),
        ),
    ]
