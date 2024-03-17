# Generated by Django 5.0.2 on 2024-03-17 22:57

import django.db.models.deletion
import django.db.models.functions.datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0005_contato_data_alteracao_alter_pessoa_contato_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_matricula', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('data_inclusao', models.DateTimeField(db_default=django.db.models.functions.datetime.Now())),
                ('ativo', models.BooleanField(default=True)),
                ('data_inativacao', models.DateTimeField(blank=True, null=True)),
                ('pessoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa')),
            ],
        ),
    ]
