from django.urls import path, include
from .views import *

urlpatterns = [
    path('pessoa/', PessoaList.as_view()),
    path('endereco/',EnderecoList.as_view()),
    path('contato/', ContatoList.as_view())
]

