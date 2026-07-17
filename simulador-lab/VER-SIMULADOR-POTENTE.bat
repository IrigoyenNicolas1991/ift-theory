@echo off
rem Simulador TCI POTENTE — motor P3M: 60.000 granos en cancha 900px
rem (subile con: ver.py --motor 2 --n 150000 --lado 1400)
cd /d "%~dp0"
.venv\Scripts\python.exe ver.py --motor 2
if errorlevel 1 pause
