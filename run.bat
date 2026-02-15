@echo off
cd /d %~dp0

echo Activando entorno virtual...
call venv\Scripts\activate

python main.py

pause

