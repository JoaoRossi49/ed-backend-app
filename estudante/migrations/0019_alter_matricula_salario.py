# Generated by Django 5.0.2 on 2024-07-31 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0018_remove_empresa_endereco_empresa_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='salario',
            field=models.CharField(blank=True, null=True),
        ),
    ]
