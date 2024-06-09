# GIE (Gestão de instituições de ensino) - Backend application

Criação de sistema de informação que unifique processos, gerencie acesso de usuários e garanta níveis adequados de disponibilidade de dados e segurança de informação afim de melhorar os processos de instituições de ensino filantrópicas.
Essa aplicação é responsável pelo gerenciamento de lógica de negócio e administração de dados providos por formulários e telas interativas contidas no repositório [ed-frontend-app](https://github.com/JoaoRossi49/ed-frontend-app).

## Índice

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Autores](#autores)

## Instalação

### Pré-requisitos

- [Python 3.11.9](https://www.python.org/downloads/)
- [Django 5.0.0](https://www.djangoproject.com/download/)
- [pip](https://pip.pypa.io/en/stable/)

### Clonando o Repositório

```bash
git clone https://github.com/JoaoRossi49/ed-backend-app
cd ed-backend-app
```

### Criando um Ambiente Virtual

```bash
python3 -m venv env
source env/bin/activate  
# No Windows use `env\Scripts\activate`
```

### Instalando Dependências

```bash
pip install -r requirements.txt
```

## Configuração

### Configuração do Banco de Dados

Edite o arquivo `settings.py` e configure o banco de dados:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
    }
}
```

### Migrações

Aplique as migrações do banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Uso

### Executando o Servidor de Desenvolvimento

Para iniciar o servidor de desenvolvimento, execute:

```bash
python manage.py runserver
```

Acesse o projeto em [http://localhost:8000](http://localhost:8000).

### Criando um Superusuário

Para acessar a interface de administração do Django, você precisa criar um superusuário:

```bash
python manage.py createsuperuser
```

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autores

- **João Rossi** - *Desenvolvedor* - [JoaoRossi49](https://github.com/JoaoRossi49)

