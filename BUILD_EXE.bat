@echo off
setlocal
cd /d "%~dp0"

if not exist .venv (
    py -3 -m venv .venv
)

call .venv\Scripts\activate.bat

python -m pip install --upgrade pip
pip install -r desktop_requirements.txt
pip install pyinstaller

echo.
echo Building ERTIQA Observatory desktop application...
pyinstaller --noconfirm ERTIQA_Observatory.spec

echo.
echo Build complete.
echo Run this file:
echo dist\ERTIQA_Observatory\ERTIQA_Observatory.exe
echo.
pause
