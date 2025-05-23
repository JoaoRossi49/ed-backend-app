from rest_framework import serializers
from .models import Pessoa, Contato, Endereco, Documento, Perfil
from estudante.models import Matricula, Turma
from estudante.serializers import TurmaCreateSerializer, MatriculaSerializer

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
        
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    contato = ContatoSerializer(many=True)
    documento = DocumentoSerializer(many=True)
    endereco = EnderecoSerializer(required=False, allow_null=True, default=None)

    data_nascimento = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])

    class Meta:
        model = Pessoa
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        contato_data = validated_data.pop('contato')
        documento_data = validated_data.pop('documento')

        pessoa = Pessoa.objects.create(**validated_data)

        if endereco_data:
            endereco = Endereco.objects.create(**endereco_data)
            pessoa.endereco = endereco
            pessoa.save()
        elif 'endereco' in validated_data and validated_data['endereco'] is None:
            pessoa.endereco = None
            pessoa.save()

        for contato in contato_data:
            contato_obj = Contato.objects.create(**contato)
            pessoa.contato.add(contato_obj)

        for documento in documento_data:
            documento_obj = Documento.objects.create(**documento)
            pessoa.documento.add(documento_obj)

        return pessoa

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        contato_data = validated_data.pop('contato', None)
        documento_data = validated_data.pop('documento', None)

        if endereco_data:
            if instance.endereco:
                for attr, value in endereco_data.items():
                    setattr(instance.endereco, attr, value)
                instance.endereco.save()
            else:
                endereco = Endereco.objects.create(**endereco_data)
                instance.endereco = endereco
                instance.save()
        elif 'endereco' in validated_data and validated_data['endereco'] is None:
            instance.endereco = None
            instance.save()

        if contato_data:
            instance.contato.clear()
            for contato in contato_data:
                contato_obj = Contato.objects.create(**contato)
                instance.contato.add(contato_obj)

        if documento_data:
            instance.documento.clear()
            for documento in documento_data:
                documento_obj = Documento.objects.create(**documento)
                instance.documento.add(documento_obj)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'