@echo off
title Gragg Robotics - Meeting Command Center
echo ==========================================
echo   GRAGG ROBOTICS - Meeting Command Center
echo   APEX Meeting with Marissa - 9:30 AM
echo ==========================================
echo.

:: Find Python
where python >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=python
    goto :found
)
where python3 >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=python3
    goto :found
)
for %%V in (313 312 311) do (
    if exist "%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe" (
        set PYTHON=%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe
        goto :found
    )
)
echo ERROR: Python not found. Install from python.org
pause
exit /b

:found
echo Found Python: %PYTHON%
echo.
echo Installing dependencies...
%PYTHON% -m pip install flask python-pptx Pillow --quiet 2>nul
echo.
echo Starting Meeting Command Center...
echo.
echo   Opening http://localhost:5050 in your browser...
echo   Keep this window open during the meeting.
echo   Press Ctrl+C to stop.
echo.
start "" http://localhost:5050
%PYTHON% "%~dp0meeting_dashboard.py"
