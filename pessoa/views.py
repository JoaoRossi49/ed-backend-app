from rest_framework import viewsets, generics
from .models import Pessoa, Contato, Endereco, Documento, Relacao
from .serializers import PessoaSerializer, ContatoSerializer, EnderecoSerializer, DocumentoSerializer, RelacaoSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

from log.models import Acesso, UserProfile

class PessoaList(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaUpdate(generics.RetrieveUpdateAPIView):
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

        try:
            user = User.objects.get(username=username)
        except:
            return Response({'error': 'Usuário não encontrado'}, status.HTTP_404_NOT_FOUND)

        user_profile = UserProfile.objects.get(user=user)

        if user_profile.bloqueado:
            return Response({'error': 'Usuário bloqueado devido a várias tentativas de login'}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(username=username, password=password)

        if user is not None:
            user_profile.tentativas = 0
            user_profile.save()
            log = Acesso(user = user, tipo_evento = 'S', ip= request.META.get('REMOTE_ADDR'))
            log.save()
            return Response(status=status.HTTP_200_OK)
        else:
            user_profile.tentativas += 1
            user_profile.save()
            log = Acesso(user = user_profile, tipo_evento = 'F', ip= request.META.get('REMOTE_ADDR'))
            log.save()
            if user_profile.tentativas >= 3:
                user_profile.bloqueado = True
                user_profile.save()
                log = Acesso(user = user_profile, tipo_evento = 'F', ip= request.META.get('REMOTE_ADDR'))
                log.save()
                return Response({'error': 'Usuário bloqueado devido a várias tentativas de login'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)