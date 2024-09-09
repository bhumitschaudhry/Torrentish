@echo off
set PYTHON_VERSION=3.10
set INSTALLER_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
python --version 2>nul | findstr /C:"Python %PYTHON_VERSION%" >nul
if %errorlevel% neq 0 (
    echo Python %PYTHON_VERSION% is not installed.
    echo Downloading and installing Python %PYTHON_VERSION%...
    powershell -Command "Start-Process -Wait %INSTALLER_URL% -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1'"
)
python -m pip install -r requirements.txt
Torrentish.exe
