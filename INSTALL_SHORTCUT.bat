@echo off
title Installing PowerPoint Presenter Shortcut
echo ==========================================
echo   Installing Desktop Shortcut...
echo ==========================================

:: Create VBS script to make a shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%temp%\create_shortcut.vbs"
echo sLinkFile = oWS.SpecialFolders("Desktop") ^& "\PowerPoint Presenter.lnk" >> "%temp%\create_shortcut.vbs"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%temp%\create_shortcut.vbs"
echo oLink.TargetPath = "%~dp0START_PRESENTATION.bat" >> "%temp%\create_shortcut.vbs"
echo oLink.WorkingDirectory = "%~dp0" >> "%temp%\create_shortcut.vbs"
echo oLink.Description = "Launch PowerPoint Presenter" >> "%temp%\create_shortcut.vbs"
echo oLink.IconLocation = "%~dp0presenter_icon.ico,0" >> "%temp%\create_shortcut.vbs"
echo oLink.Save >> "%temp%\create_shortcut.vbs"

cscript //nologo "%temp%\create_shortcut.vbs"
del "%temp%\create_shortcut.vbs"

echo.
echo Desktop shortcut created!
echo You can now double-click "PowerPoint Presenter" on your Desktop.
echo.
pause
