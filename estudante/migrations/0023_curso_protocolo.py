# Generated by Django 5.0.2 on 2024-09-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0022_remove_matricula_dias_da_semana_curso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='protocolo',
            field=models.CharField(blank=True, null=True),
        ),
    ]