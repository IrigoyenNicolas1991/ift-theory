@echo off
rem Simulador TCI en vivo — config verificada (720 granos, la del simulador web)
cd /d "%~dp0"
.venv\Scripts\python.exe ver.py %*
if errorlevel 1 pause
