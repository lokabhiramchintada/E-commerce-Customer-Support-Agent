@echo off
echo ====================================
echo E-commerce Customer Support Agent
echo Setup Script
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Python found
echo.

REM Create virtual environment
if not exist "venv" (
    echo [2/5] Creating virtual environment...
    python -m venv venv
) else (
    echo [2/5] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo [4/5] Installing dependencies...
pip install -r requirements.txt

REM Setup environment file
if not exist ".env" (
    echo [5/5] Setting up environment file...
    copy .env.example .env
    echo.
    echo ====================================
    echo IMPORTANT: Configure your API key!
    echo ====================================
    echo Please edit the .env file and add your Google Gemini API key
    echo.
    notepad .env
) else (
    echo [5/5] Environment file already exists
)

echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo.
echo To run the application:
echo   1. Activate virtual environment: venv\Scripts\activate
echo   2. Run the server: python main.py
echo   3. Open http://localhost:8000 in your browser
echo.
pause
