@echo off
title PowerPoint Presenter
echo ==========================================
echo    PowerPoint Presenter - Starting...
echo ==========================================
echo.

:: Check for Python
where python >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=python
) else (
    where python3 >nul 2>&1
    if %errorlevel%==0 (
        set PYTHON=python3
    ) else (
        echo ERROR: Python is not installed!
        echo Download it from https://www.python.org/downloads/
        echo Make sure to check "Add Python to PATH" during install.
        pause
        exit /b
    )
)

:: Install dependencies if needed
echo Installing dependencies...
%PYTHON% -m pip install python-pptx flask Pillow --quiet

:: Kill any existing instance
taskkill /f /im python.exe /fi "WINDOWTITLE eq pptx_presenter*" >nul 2>&1

:: Start the server
echo.
echo Starting presentation server...
start "" http://localhost:5050
%PYTHON% "%~dp0pptx_presenter.py"
