from django.apps import AppConfig


class EstudanteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estudante'
    def ready(self):
        import estudante.signals 
