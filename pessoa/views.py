from rest_framework import generics
from .models import Pessoa, Endereco, Contato
from .serializers import PessoaSerializer, EnderecoSerializer, ContatoSerializer

class PessoaList(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
class EnderecoList(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoList(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer    