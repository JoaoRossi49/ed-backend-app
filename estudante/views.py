from rest_framework import generics
from .models import Matricula
from .serializers import MatriculaSerializer

class MatriculaList(generics.ListCreateAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer