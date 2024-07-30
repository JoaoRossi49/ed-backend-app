from django.urls import path
from .views import *

urlpatterns = [
    path('matricula/', MatriculaList.as_view()),
    path('matricula/<int:pk>/', MatriculaUpdate.as_view()),
    path('turmas/', TurmaList.as_view()),
    path('turmas/<int:pk>/', TurmaUpdate.as_view()),
    path('cbos/', CboList.as_view()),
    path('cursos/', CursoList.as_view()),
    path('empresas/', EmpresaList.as_view()),
    path('escolaridades/', EscolaridadeList.as_view()),
    path('contrato/<str:matricula>', download_docx),
    path('contrato-pdf/<int:pk>/', view_docx_as_pdf)
]

