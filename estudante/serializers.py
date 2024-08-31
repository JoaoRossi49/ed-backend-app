from rest_framework import serializers
from .models import *

class CboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cbo
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class EscolaridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escolaridade
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    data_inicio = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])
    class Meta:
        model = Turma
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):
    turma_nome = serializers.CharField(source='turma.nome', read_only=True)
    class Meta:
        model = Aula
        fields = '__all__'
        extra_fields = ['turma_nome']

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    escolaridade_nome = serializers.CharField(source='escolaridade.descricao', read_only=True)
    turma_nome = serializers.CharField(source='turma.nome', read_only=True)
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)
    empresa_nome = serializers.CharField(source='empresa.nome_fantasia', read_only=True)
    cbo_nome = serializers.CharField(source='cbo.descricao', read_only=True)
    data_inicio_contrato = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])
    data_terminio_contrato = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])
    data_inicio_empresa = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])
    data_terminio_empresa = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])

    class Meta:
        model = Matricula
        fields = '__all__'
        extra_fields = ['escolaridade_nome', 'turma_nome', 'curso_nome', 'empresa_nome', 'cbo_nome']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(MatriculaSerializer, self).get_field_names(declared_fields, info)
        if hasattr(self.Meta, 'extra_fields'):
            expanded_fields.extend(self.Meta.extra_fields)
        return expanded_fields

class TurmaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ('id',)