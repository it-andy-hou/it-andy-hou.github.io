@echo off
title Andy wiki

choice /t 2 /d y /n >nul

start chrome.exe http://127.0.0.1:8000/

python -m mkdocs serve

pause