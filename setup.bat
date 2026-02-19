@echo off
setlocal

cd /d "%~dp0"

set "VENV=.venv"
set "PYTHON=%VENV%\Scripts\python.exe"

if not exist "%PYTHON%" (
  call :create_venv
  if errorlevel 1 exit /b 1
)

call :install_requirements
if errorlevel 1 (
  echo Dependency install failed. Recreating .venv and retrying once...
  rmdir /s /q "%VENV%" >nul 2>&1
  call :create_venv
  if errorlevel 1 exit /b 1
  call :install_requirements
  if errorlevel 1 exit /b 1
)

echo.
echo Setup complete.
echo Use start.bat to run the app.
exit /b 0

:create_venv
echo Creating virtual environment in .venv...
py -3 -m venv "%VENV%" >nul 2>&1
if errorlevel 1 (
  python -m venv "%VENV%"
)

if not exist "%PYTHON%" (
  echo Failed to create virtual environment. Make sure Python is installed.
  exit /b 1
)
exit /b 0

:install_requirements
echo Installing backend dependencies...
"%PYTHON%" -m pip install --upgrade pip
if errorlevel 1 exit /b 1
"%PYTHON%" -m pip install -r backend\requirements.txt
if errorlevel 1 exit /b 1
exit /b 0
