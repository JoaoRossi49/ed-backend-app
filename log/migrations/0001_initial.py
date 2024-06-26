# Generated by Django 5.0.2 on 2024-06-01 18:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inclusao', models.DateTimeField(auto_now_add=True)),
                ('tipo_evento', models.CharField(choices=[('F', 'Falha ao acessar'), ('S', 'Sucesso ao acessar')], max_length=10)),
                ('user', models.CharField(verbose_name=60)),
                ('ip', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tentativas', models.IntegerField(default=0)),
                ('bloqueado', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
