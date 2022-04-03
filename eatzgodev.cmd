@echo off

title EatzGo: Console -- main.py
echo "main.py -> the main script file."
%cd%\main.py
pause

title EatzGo: Console -- shell.py
echo "shell.py -> the shell that control varius things in this project."
%cd%\shell.py
pause

title EatzGo: Console -- WebSite
curl --tls-max 1.3 https://boubajoker.github.io/Eatz_Go/
start https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe