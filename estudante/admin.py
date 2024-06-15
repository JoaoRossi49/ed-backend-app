from django.contrib import admin
from .models import Matricula, Turma, Aula, Presenca

admin.site.register(Matricula)
admin.site.register(Turma)
admin.site.register(Aula)
admin.site.register(Presenca)