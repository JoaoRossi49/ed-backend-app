from rest_framework import viewsets, generics
from .models import Pessoa, Contato, Endereco, Documento, Relacao
from .serializers import PessoaSerializer, ContatoSerializer, EnderecoSerializer, DocumentoSerializer, RelacaoSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response

class PessoaList(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
class EnderecoList(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoList(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer   

class DocumentoList(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class RelacaoList(generics.ListCreateAPIView):
    queryset = Relacao.objects.all()
    serializer_class = RelacaoSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(password=password, username=username)
        
        if user is not None:
            return Response({'authenticated': True})
        else:
            return Response({'authenticated': False})

class PessoaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer