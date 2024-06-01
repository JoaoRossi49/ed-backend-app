from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Acesso, UserProfile

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
    list_display = ('user', 'bloqueado')
    search_fields = ('user__username',)