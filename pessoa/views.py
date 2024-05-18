from rest_framework import generics
from .models import Pessoa, Endereco, Contato
from .serializers import PessoaSerializer, EnderecoSerializer, ContatoSerializer
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

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('senha')
        print(email, password)
        user = authenticate(username=email, password=password)
        
        if user is not None:
            return Response({'authenticated': True})
        else:
            return Response({'authenticated': False})