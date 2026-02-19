@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo Environment not found. Running setup first...
  call setup.bat
  if errorlevel 1 exit /b 1
)

echo Starting app at http://127.0.0.1:5000
echo Press Ctrl+C to stop.
echo.

".venv\Scripts\python.exe" backend\app.py
