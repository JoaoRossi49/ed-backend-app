@echo off

REM Navega até mosquitto
cd C:\Program Files\mosquitto

REM Inicia brooker mosquitto 
start mosquitto.exe -p 8080 -v 
timeout /T 5 /NOBREAK

REM Navegar para o diretório do projeto Django
cd C:\git\api_dispositivo\geotrack

REM Ativar o ambiente virtual
call venv\Scripts\activate

REM Iniciar o servidor Django
python manage.py runserver --noreload

