# Generated by Django 5.0.2 on 2024-02-26 23:54

import django.db.models.deletion
import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_auto_20240205_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='data_inclusao',
            field=models.DateTimeField(db_default=django.db.models.functions.datetime.Now()),
        ),
        migrations.AddField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='data_inclusao',
            field=models.DateTimeField(db_default=django.db.models.functions.datetime.Now()),
        ),
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pais',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nome_social',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='tipo_contato',
            field=models.CharField(choices=[('CELULAR', 'Celular'), ('TELEFONE', 'Telefone'), ('EMAIL', 'E-mail')], max_length=10),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_inclusao',
            field=models.DateTimeField(db_default=django.db.models.functions.datetime.Now()),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_documento', models.CharField(max_length=60)),
                ('data_inclusao', models.DateTimeField(db_default=django.db.models.functions.datetime.Now())),
                ('tipo_documento', models.CharField(choices=[('RG', 'Documento de identidade'), ('CPF', 'Cadastro de pessoa física'), ('CTPS', 'Carteira nascional de trabalho'), ('PASS', 'Passaporte'), ('CNH', 'Carteira de motorista'), ('EL', 'Título de eleitor'), ('CNS', 'Cartão nascional de saúde')], max_length=40)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Relacao_familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_relacao', models.CharField(choices=[('PAI', 'Pai'), ('MÃE', 'Mãe'), ('FILHO', 'Filho'), ('FILHA', 'Filha'), ('IRMÃO', 'Irmão'), ('IRMÃ', 'Irmã'), ('AVÔ', 'Avô'), ('AVÓ', 'Avó'), ('TIO', 'Tio'), ('TIA', 'Tia'), ('PRIMO', 'Primo'), ('PRIMA', 'Prima'), ('SOGRO', 'Sogro'), ('SOGRa', 'Sogra'), ('GENRO', 'Genro'), ('NORA', 'Nora'), ('MARIDO', 'Marido'), ('ESPOSA', 'Esposa'), ('SOBRINHO', 'Sobrinho'), ('SOBRINHA', 'Sobrinha'), ('NETO', 'Neto'), ('NETA', 'Neta'), ('PAI_ADOTIVO', 'Pai Adotivo'), ('MÃE_ADOTIVA', 'Mãe Adotiva'), ('FILHO_ADOTIVO', 'Filho Adotivo'), ('FILHA_ADOTIVA', 'Filha Adotiva')], max_length=40)),
                ('pessoa_filho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relacoes_filho', to='pessoa.pessoa')),
                ('pessoa_pai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relacoes_pai', to='pessoa.pessoa')),
            ],
        ),
    ]