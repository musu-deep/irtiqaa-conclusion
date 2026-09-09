@echo off
setlocal
cd /d "%~dp0"

if not exist .venv (
    py -3 -m venv .venv
)

call .venv\Scripts\activate.bat

python -m pip install --upgrade pip >nul
pip install -r desktop_requirements.txt >nul

python app.py
