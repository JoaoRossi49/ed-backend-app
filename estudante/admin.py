from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import *
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

class Desligamento_matriculaAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'data_desligamento', 'motivo')
    list_filter = (('data_desligamento', DateFieldListFilter),)

class Atividade_teoricaAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'data_inicio', 'data_fim', 'periodo')

    def periodo(self, obj):
        return obj.hora_inicio + ' à ' + obj.hora_termino

admin.site.register(Turma, TurmaAdmin)
admin.site.register(Curso)
admin.site.register(Empresa)
admin.site.register(Cbo)
admin.site.register(CBOAssociado)
admin.site.register(Escolaridade)
#admin.site.register(DiaSemana)
admin.site.register(Psa)
admin.site.register(Matricula)
admin.site.register(Desligamento_matricula, Desligamento_matriculaAdmin)
admin.site.register(Atividade_teorica, Atividade_teoricaAdmin)
admin.site.register(Modulo)
admin.site.register(Aula)
admin.site.register(Tipo_presenca)
admin.site.register(Presenca, PresencaAdmin)
