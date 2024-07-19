from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Acesso, UserProfile, Cadastro
from django.utils.html import format_html

@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    list_display = ('user', 'data_inclusao', 'ip')
    search_fields = ('user',)
    list_filter = (
        ('data_inclusao', admin.DateFieldListFilter),  # Adiciona o filtro de data_inclusao
    )
    date_hierarchy = 'data_inclusao'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bloqueado')
    search_fields = ('user__username',)
    
    def nome(self, obj):
        return obj.user
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(bloqueado=True)

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('tipo_evento', 'model_afetada', 'data_inclusao', 'formatted_details')
    list_filter = ('data_inclusao', 'tipo_evento', 'model_afetada')

    def formatted_details(self, obj):
        detalhes = obj.format_detalhes()
        if not detalhes:
            return "No details available"
        
        old_details = detalhes.get('old', {})
        new_details = detalhes.get('new', {})

        rows = []
        if old_details and new_details:
            for field, old_value in old_details.items():
                new_value = new_details.get(field, '')
                rows.append(f'<tr><td>{field}</td><td>{old_value}</td><td>{new_value}</td></tr>')
        
        return format_html(
            '<table border="1"><thead><tr><th>Coluna afetada</th><th>Valor antigo</th><th>Valor atual</th></tr></thead><tbody>{}</tbody></table>',
            format_html(''.join(rows))
        )

    formatted_details.short_description = 'Details'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False