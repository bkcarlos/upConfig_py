@echo off

rem echo %~dp0venv\Scripts
rem echo %~dp0venv\Lib\site-packages
set PATH=%PATH%;%~dp0venv\Scripts;%~dp0venv\Lib\site-packages;
python upConfig.cpython-37.pyc
pause
