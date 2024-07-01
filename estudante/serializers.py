from rest_framework import serializers
from .models import Matricula, Turma

class TurmaSerializer(serializers.ModelSerializer):
    data_inicio = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])
    class Meta:
        model = Turma
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    turma_nome = serializers.CharField(source='turma.nome', read_only=True)

    class Meta:
        model = Matricula
        fields = '__all__'
        extra_fields = ['turma_nome']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(MatriculaSerializer, self).get_field_names(declared_fields, info)
        if hasattr(self.Meta, 'extra_fields'):
            expanded_fields.extend(self.Meta.extra_fields)
        return expanded_fields

class TurmaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ('id',)