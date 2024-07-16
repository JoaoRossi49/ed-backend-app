from django.contrib import admin
from .models import Matricula, Turma, Aula, Presenca, Curso, Empresa, Cbo, Modulo, Tipo_presenca

admin.site.register(Matricula)
admin.site.register(Curso)
admin.site.register(Empresa)
admin.site.register(Cbo)
admin.site.register(Modulo)
admin.site.register(Turma)
admin.site.register(Aula)
admin.site.register(Presenca)
admin.site.register(Tipo_presenca)