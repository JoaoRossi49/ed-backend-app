from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from django.core.exceptions import SuspiciousOperation
from estudante.contratos.pdf_utils import modify_docx
import os
from django.conf import settings
from io import BytesIO
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .calendarios.html_calendar import gerar_calendario


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

#    def post(self, request, *args, **kwargs):
#        queryset = self.get_queryset()
#        serializer = self.get_serializer(queryset, many=True)
#        return Response(serializer.data)


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

class AulaList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    
class AulaUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer 

class ModuloList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer
    
class ModuloUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer 

def renderizar_calendario(request, matricula):
    html_content = gerar_calendario(matricula)
    response = HttpResponse(html_content, content_type='text/html')
    return response
   
def download_docx(request, matricula):
    doc_path = os.path.join(settings.BASE_DIR, 'estudante', 'contratos', 'templates', f'contrato.docx')
    
    doc_buffer = modify_docx(doc_path, matricula)

    response = HttpResponse(doc_buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="contrato_modificado.docx"'
    return response

def convert_docx_to_pdf(doc_buffer):
    doc = Document(doc_buffer)
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter

    y = height - 40
    for para in doc.paragraphs:
        if y < 40: 
            c.showPage()
            y = height - 40
        c.drawString(40, y, para.text)
        y -= 20

    c.save()
    pdf_buffer.seek(0)
    return pdf_buffer

def view_docx_as_pdf(request):
    # Caminho do arquivo DOCX
    doc_path = os.path.join(settings.BASE_DIR, 'estudante', 'contratos', 'templates', 'contrato15.docx')
    search_text = '[NOME_EMPRESA]'
    replace_text = 'Empresa de alimentos LTDA'

    # Modificar o DOCX e obter o buffer modificado
    doc_buffer = modify_docx(doc_path, search_text, replace_text)

    # Converter DOCX para PDF
    pdf_buffer = convert_docx_to_pdf(doc_buffer)

    # Retornar PDF para o navegador
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="documento.pdf"'
    return response