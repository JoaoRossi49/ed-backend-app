from django.urls import path
from .views import *

urlpatterns = [
    path('matricula/', MatriculaList.as_view())
]

