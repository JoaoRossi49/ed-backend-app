from rest_framework import generics
from .models import Pessoa, Endereco
from .serializers import PessoaSerializer, EnderecoSerializer

class PessoaList(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
class EnderecoList(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer