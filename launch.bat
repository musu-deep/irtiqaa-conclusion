@echo off
setlocal
cd /d "%~dp0"

start "" http://127.0.0.1:8027/index.html

python -m http.server 8027
