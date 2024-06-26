# Generated by Django 5.0.2 on 2024-06-02 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0012_remove_documento_pessoa_pessoa_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='contato',
            field=models.ManyToManyField(blank=True, related_name='pessoas', to='pessoa.contato'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='documento',
            field=models.ManyToManyField(blank=True, related_name='pessoas', to='pessoa.documento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='endereco',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.endereco'),
        ),
    ]
