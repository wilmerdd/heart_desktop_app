@echo off
pip install pyinstaller
pyinstaller --onefile --windowed app.py --name HeartPredictor
pause
