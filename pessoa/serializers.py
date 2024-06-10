from rest_framework import serializers
from .models import Pessoa, Contato, Endereco, Documento, Relacao
from estudante.models import Matricula, Turma

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
    turma_id = serializers.IntegerField(write_only=True, required=False)
    
    data_nascimento = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])

    class Meta:
        model = Pessoa
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        contato_data = validated_data.pop('contato')
        documento_data = validated_data.pop('documento')
        turma_id = validated_data.pop('turma_id', None)
        
        endereco = Endereco.objects.create(**endereco_data)
        
        pessoa = Pessoa.objects.create(endereco=endereco, **validated_data)
        
        for contato in contato_data:
            contato_obj = Contato.objects.create(**contato)
            pessoa.contato.add(contato_obj)
            
        for documento in documento_data:
            documento_obj = Documento.objects.create(**documento)
            pessoa.documento.add(documento_obj)  

        turma = None
        if turma_id:
            try:
                turma = Turma.objects.get(id=turma_id)
            except Turma.DoesNotExist:
                raise serializers.ValidationError({"turma": "Turma não encontrada."})
            
        #Cria-se uma nova matrícula    
        Matricula.objects.create(pessoa=pessoa, turma=turma) 

        return pessoa

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        contato_data = validated_data.pop('contato', None)
        documento_data = validated_data.pop('documento')
        turma_id = validated_data.pop('turma_id', None)

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

        if turma_id:
            try:
                turma = Turma.objects.get(id=turma_id)
            except Turma.DoesNotExist:
                raise serializers.ValidationError({"turma": "Turma não encontrada."})

            # Atualiza ou cria uma matrícula associada à pessoa e à turma
            matricula, created = Matricula.objects.update_or_create(
                pessoa=instance, 
                defaults={'turma': turma}
            )
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance