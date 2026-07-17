@echo off
rem Simulador TCI en vivo — mar 11x mas fino (8000 granos, EXPERIMENTAL)
cd /d "%~dp0"
.venv\Scripts\python.exe ver.py --n 8000
if errorlevel 1 pause
