@echo off

:loop

set /p ip="CMD> "

py publish.py %ip%

goto loop