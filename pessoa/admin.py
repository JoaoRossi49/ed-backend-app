from django.contrib import admin
from .models import Pessoa, Endereco, Contato, Documento, Tipo_pessoa

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Contato)
admin.site.register(Documento)
admin.site.register(Tipo_pessoa)
