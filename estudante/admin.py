from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Matricula, Turma, Aula, Presenca, Curso, Empresa, Cbo, Modulo, Tipo_presenca, Escolaridade
from pessoa.models import Pessoa


class PresencaAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'data_presenca', 'aula_id')
    list_filter = (('data_presenca', DateFieldListFilter),)

    def aula(self, obj):
        return obj.aula_id.tema

class MatriculaInline(admin.TabularInline):
    model = Matricula
    fields  = ('pessoa', 'curso', 'empresa', 'cbo')
    readonly_fields  = ('pessoa', 'curso', 'empresa', 'cbo')
    can_delete = False    
    extra = 0  

class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]
    list_display = ('nome', 'data_inclusao')


admin.site.register(Matricula)
admin.site.register(Curso)
admin.site.register(Empresa)
admin.site.register(Cbo)
admin.site.register(Modulo)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aula)
admin.site.register(Presenca, PresencaAdmin)
admin.site.register(Tipo_presenca)
admin.site.register(Escolaridade)