from rest_framework import viewsets, generics
from .models import Pessoa, Contato, Endereco, Documento, Perfil
from .serializers import PessoaSerializer, ContatoSerializer, EnderecoSerializer, DocumentoSerializer, PerfilSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from log.models import Acesso, UserProfile

class PessoaList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
class PessoaUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer 
    
class EnderecoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer   

class DocumentoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class PerfilList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PerfilSerializer

    def get_queryset(self):
        user = self.request.user
        return Perfil.objects.filter(user=user)

class LoginView(APIView):
    permission_classes = [AllowAny]
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
            refresh = RefreshToken.for_user(user)
            user_profile.tentativas = 0
            user_profile.save()
            log = Acesso(user = user, tipo_evento = 'S', ip= request.META.get('REMOTE_ADDR'))
            log.save()
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
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