from rest_framework import serializers
from .models import Pessoa, Contato, Endereco, Documento, Relacao

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    contato = ContatoSerializer()

    class Meta:
        model = Pessoa
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        contato_data = validated_data.pop('contato')
        
        endereco = Endereco.objects.create(**endereco_data)
        contato = Contato.objects.create(**contato_data)
        
        pessoa = Pessoa.objects.create(endereco=endereco, **validated_data)
        pessoa.contato.add(contato)
        
        return pessoa

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        contato_data = validated_data.pop('contato', None)
        
        if endereco_data:
            for attr, value in endereco_data.items():
                setattr(instance.endereco, attr, value)
            instance.endereco.save()

        if contato_data:
            instance.contato.clear()
            contato_obj = Contato.objects.create(**contato_data)
            instance.contato.add(contato_obj)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class RelacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacao
        fields = '__all__'
