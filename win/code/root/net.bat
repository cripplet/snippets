@echo off

echo NOTE "PID" IN TASK LIST > net.txt
netstat /o >> net.txt
tasklist >> net.txt

driverquery > driverquery.txt