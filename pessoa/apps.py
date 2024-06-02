from django.apps import AppConfig


class PessoaConfig(AppConfig):
    name = 'pessoa'
    print('entrou no app de pessoa')
    def ready(self):
        print('entrou no ready')
        import pessoa.signals