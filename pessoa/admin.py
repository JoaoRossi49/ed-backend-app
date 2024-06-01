from django.contrib import admin
from .models import Pessoa, Endereco, Contato, Relacao, Documento

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Contato)
admin.site.register(Relacao)
admin.site.register(Documento)
