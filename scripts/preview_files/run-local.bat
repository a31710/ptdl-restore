@echo off
setlocal
cd /d "%~dp0"
title PTDL preview

rem Prefer the "py" launcher: plain "python" is sometimes only a Microsoft Store shortcut.
set "PYCMD="
where py >nul 2>nul
if not errorlevel 1 set "PYCMD=py -3"
if not defined PYCMD (
  where python >nul 2>nul
  if not errorlevel 1 set "PYCMD=python"
)
if not defined PYCMD goto nopython

%PYCMD% --version >nul 2>nul
if errorlevel 1 goto nopython

echo Starting PTDL preview with: %PYCMD%
%PYCMD% serve.py 8080
echo.
echo The server has stopped. If you saw an error above, please send it to the person helping you.
pause
exit /b 0

:nopython
echo.
echo Could not find a working Python 3 on this computer.
echo Install it from https://www.python.org/downloads/ and tick "Add python.exe to PATH".
echo If Python is already installed, open a terminal in this folder and run:  python serve.py
echo.
pause
exit /b 1
