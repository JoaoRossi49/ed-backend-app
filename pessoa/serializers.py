from rest_framework import serializers
from .models import Pessoa, Contato, Endereco, Documento, Relacao
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

class RelacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacao
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    contato = ContatoSerializer(many=True)
    documento = DocumentoSerializer(many=True)
    
    data_nascimento = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])

    class Meta:
        model = Pessoa
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        contato_data = validated_data.pop('contato')
        documento_data = validated_data.pop('documento')
        
        endereco = Endereco.objects.create(**endereco_data)
        
        pessoa = Pessoa.objects.create(endereco=endereco, **validated_data)
        
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
        documento_data = validated_data.pop('documento')

        if endereco_data:
            for attr, value in endereco_data.items():
                setattr(instance.endereco, attr, value)
            instance.endereco.save()

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