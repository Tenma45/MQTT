@echo off

:loop

set /p ip="CMD> "

py broker.py %ip%

goto loop