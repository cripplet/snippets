@echo off
cls
echo MAKE SURE MESSENGER APPLICATION IS ENABLED:
echo CTRL PNL
echo CLASSIC VIEW
echo ADMIN TOOLS
echo COMP MGNT
echo SERVICES AND APP
echo SERV
echo MSGR
echo AUTO
echo START
echo USER CAN ALSO BE COMPUTER NAME: HOME= PAVILION6635

:A
echo MESSENGER
set /p n=User:
set /p m=Message:
net send %n% %m%
Pause
Goto A