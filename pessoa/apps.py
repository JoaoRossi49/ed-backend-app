from django.apps import AppConfig


class PessoaConfig(AppConfig):
    name = 'pessoa'
    def ready(self):
        import pessoa.signals