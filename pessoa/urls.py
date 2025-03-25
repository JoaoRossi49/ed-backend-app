from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PessoaList.as_view()),
    path('<int:pk>/', PessoaUpdate.as_view()),
    path('endereco/',EnderecoList.as_view()),
    path('contato/', ContatoList.as_view()),
    path('login/', LoginView.as_view()),
    path('perfil/', PerfilList.as_view()),
]

