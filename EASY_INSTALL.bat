@echo off
title PowerPoint Presenter - Easy Installer
echo ==========================================
echo   PowerPoint Presenter - Easy Installer
echo ==========================================
echo.

:: Set install directory
set INSTALL_DIR=%USERPROFILE%\PowerPointPresenter
echo Installing to: %INSTALL_DIR%
echo.

:: ---- STEP 1: Check for Python ----
echo [1/5] Checking for Python...
where python >nul 2>&1
if %errorlevel%==0 (
    echo       Python found!
    set PYTHON=python
    goto :has_python
)
where python3 >nul 2>&1
if %errorlevel%==0 (
    echo       Python3 found!
    set PYTHON=python3
    goto :has_python
)

:: Check common Python install locations
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set PYTHON=%LOCALAPPDATA%\Programs\Python\Python311\python.exe
    echo       Python found at %PYTHON%
    goto :has_python
)
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set PYTHON=%LOCALAPPDATA%\Programs\Python\Python312\python.exe
    echo       Python found at %PYTHON%
    goto :has_python
)
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    set PYTHON=%LOCALAPPDATA%\Programs\Python\Python313\python.exe
    echo       Python found at %PYTHON%
    goto :has_python
)

echo.
echo       Python is NOT installed. Installing now...
echo       Downloading Python installer...
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe' -OutFile '%TEMP%\python_installer.exe'"

if not exist "%TEMP%\python_installer.exe" (
    echo.
    echo ERROR: Could not download Python installer.
    echo Please download Python manually from https://www.python.org/downloads/
    echo IMPORTANT: Check "Add Python to PATH" during install!
    pause
    exit /b
)

echo       Running Python installer (this may take a minute)...
echo       IMPORTANT: If a window pops up, check "Add python.exe to PATH" and click "Install Now"
"%TEMP%\python_installer.exe" /passive InstallAllUsers=0 PrependPath=1 Include_pip=1
del "%TEMP%\python_installer.exe"

:: Refresh PATH
set PATH=%LOCALAPPDATA%\Programs\Python\Python312\;%LOCALAPPDATA%\Programs\Python\Python312\Scripts\;%PATH%

where python >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=python
) else (
    :: Try common locations after install
    for %%V in (313 312 311) do (
        if exist "%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe" (
            set PYTHON=%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe
            goto :has_python
        )
    )
    echo.
    echo ERROR: Python install may need a restart.
    echo Please close this window, restart your computer, then run this again.
    pause
    exit /b
)

:has_python
echo.

:: ---- STEP 2: Create install directory ----
echo [2/5] Creating install directory...
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
echo       Done.
echo.

:: ---- STEP 3: Download project files ----
echo [3/5] Downloading PowerPoint Presenter files...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/dopienerd/empirebot/archive/refs/heads/claude/connect-home-desktop-VCcv7.zip' -OutFile '%TEMP%\presenter.zip'"

if not exist "%TEMP%\presenter.zip" (
    echo ERROR: Could not download files. Check your internet connection.
    pause
    exit /b
)

echo       Extracting files...
powershell -Command "Expand-Archive -Path '%TEMP%\presenter.zip' -DestinationPath '%TEMP%\presenter_extract' -Force"

:: Copy files to install dir
xcopy "%TEMP%\presenter_extract\empirebot-claude-connect-home-desktop-VCcv7\*" "%INSTALL_DIR%\" /E /Y /Q >nul
del "%TEMP%\presenter.zip"
rmdir /S /Q "%TEMP%\presenter_extract" 2>nul
echo       Done.
echo.

:: ---- STEP 4: Install Python dependencies ----
echo [4/5] Installing Python packages...
%PYTHON% -m pip install python-pptx flask Pillow --quiet
echo       Done.
echo.

:: ---- STEP 5: Create Desktop shortcut ----
echo [5/5] Creating Desktop shortcut...
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%TEMP%\make_shortcut.vbs"
echo sLinkFile = oWS.SpecialFolders("Desktop") ^& "\PowerPoint Presenter.lnk" >> "%TEMP%\make_shortcut.vbs"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%TEMP%\make_shortcut.vbs"
echo oLink.TargetPath = "%INSTALL_DIR%\START_PRESENTATION.bat" >> "%TEMP%\make_shortcut.vbs"
echo oLink.WorkingDirectory = "%INSTALL_DIR%" >> "%TEMP%\make_shortcut.vbs"
echo oLink.Description = "Launch PowerPoint Presenter" >> "%TEMP%\make_shortcut.vbs"
if exist "%INSTALL_DIR%\presenter_icon.ico" (
    echo oLink.IconLocation = "%INSTALL_DIR%\presenter_icon.ico,0" >> "%TEMP%\make_shortcut.vbs"
)
echo oLink.Save >> "%TEMP%\make_shortcut.vbs"
cscript //nologo "%TEMP%\make_shortcut.vbs"
del "%TEMP%\make_shortcut.vbs"
echo       Done.
echo.

echo ==========================================
echo   INSTALLATION COMPLETE!
echo ==========================================
echo.
echo   A "PowerPoint Presenter" icon is now
echo   on your Desktop. Double-click it to
echo   start presenting!
echo.
echo   Files installed to: %INSTALL_DIR%
echo.

set /p LAUNCH="Launch PowerPoint Presenter now? (Y/N): "
if /i "%LAUNCH%"=="Y" (
    start "" "%INSTALL_DIR%\START_PRESENTATION.bat"
)

pause
