@echo off

:loop

set /p ip="CMD> "

py subscribe.py %ip%

goto loop