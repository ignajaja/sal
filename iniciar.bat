@echo off
cd /d %~dp0
call venv-30-mensajes\Scripts\activate.bat
start "" http://127.0.0.1:8000
python mensajes/manage.py runserver 127.0.0.1:8000 --noreload