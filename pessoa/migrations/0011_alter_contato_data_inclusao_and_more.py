# Generated by Django 5.0.2 on 2024-05-29 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0010_alter_contato_data_inclusao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_inclusao',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 13, 8, 56, 990384, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='documento',
            name='data_inclusao',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 13, 8, 56, 992402, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='data_inclusao',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 13, 8, 56, 990384, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_inclusao',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 13, 8, 56, 991378, tzinfo=datetime.timezone.utc)),
        ),
    ]
