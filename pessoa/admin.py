from django.contrib import admin
from .models import Pessoa, Endereco, Contato, Documento, Tipo_pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome_pessoa', 'data_nascimento', 'idade')
    
    def idade(self, obj):
        return obj.calcular_idade()
    idade.short_description = 'Idade'
    
    def nome_pessoa(self, obj):
        return obj.nome_social if obj.nome_social else obj.nome


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('pessoas_display', 'descricao', 'tipo_contato')
    
    def pessoas_display(self, obj):
        return ", ".join([pessoa.nome for pessoa in obj.pessoas.all()])
    pessoas_display.short_description = 'Pessoas Associadas'


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Endereco)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Documento)
admin.site.register(Tipo_pessoa)
