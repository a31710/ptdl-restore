@echo off
rem Chay ban xem truoc tren may: bam dup file nay, roi mo http://localhost:8080
cd /d "%~dp0"
python serve.py 8080
pause
