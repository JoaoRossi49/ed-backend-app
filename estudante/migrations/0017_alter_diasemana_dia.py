# Generated by Django 5.0.2 on 2024-07-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0016_rename_desligamentos_matriculas_desligamento_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diasemana',
            name='dia',
            field=models.CharField(choices=[('Segunda-feira', 'Segunda-feira'), ('Terça-feira', 'Terça-feira'), ('Quarta-feira', 'Quarta-feira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=20, unique=True),
        ),
    ]
