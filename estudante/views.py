from rest_framework import generics
from .models import Matricula, Turma, Cbo, Curso, Empresa, Escolaridade
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CboList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cbo.objects.all()
    serializer_class = CboSerializer

class CursoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EmpresaList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EscolaridadeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Escolaridade.objects.all()
    serializer_class = EscolaridadeSerializer

class MatriculaList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MatriculaSerializer

    def get_queryset(self):
        queryset = Matricula.objects.all()
        ativo = self.request.data.get('ativo')
        turma = self.request.data.get('turma')
        
        if ativo is not None:
            queryset = queryset.filter(ativo=ativo)
        
        if turma is not None:
            queryset = queryset.filter(turma=turma)
        
        return queryset

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MatriculaUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer 

class TurmaList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    
class TurmaUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer 