from rest_framework import serializers
from .models import Matricula, Turma

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    data_inicio = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])
    class Meta:
        model = Turma
        fields = '__all__'