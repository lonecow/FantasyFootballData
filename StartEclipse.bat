@echo off
:: Local workspace
set LOCAL-WS=_EWS-PYDEV

:: This is where we will store a batch file that allows for setting of "Environmental Variables"
:: This will be a batch file in the home directory that you can update variables
IF EXIST %HOMEPATH%\Environment.bat ( call %HOMEPATH%\Environment.bat )

if not exist "%PYDEV%" goto ERR
if not exist "%PYDEVWSREF%" goto SKIPCOPY

if not exist "%LOCAL-WS%" (echo Copying reference Workspace... & xcopy "%PYDEVWSREF%" "%LOCAL-WS%" /S /E /I /H /Q)

:SKIPCOPY
start "Pydev" "%PYDEV%" -clean -data "%LOCAL-WS%" -Import "EclipseProject"
exit

:ERR
echo Environmental variable PYDEV=[%PYDEV%] pointing to installation of Eclipse is not set or incorrect!
pause

