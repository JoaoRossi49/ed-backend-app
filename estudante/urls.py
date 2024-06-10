from django.urls import path
from .views import *

urlpatterns = [
    path('matricula/', MatriculaList.as_view()),
    path('turmas/', TurmaList.as_view()),
    path('turmas/<int:pk>/', TurmaUpdate.as_view())
]

