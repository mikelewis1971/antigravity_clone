@echo off
REM Antigravity Local - Windows Launcher

echo ========================================
echo   Antigravity Local
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9 or higher
    pause
    exit /b 1
)

REM Check if dependencies are installed
python -c "import llama_cpp" >nul 2>&1
if errorlevel 1 (
    echo Dependencies not installed. Running setup...
    python setup.py
    if errorlevel 1 (
        echo Setup failed.
        pause
        exit /b 1
    )
)

echo Starting Antigravity Local server...
echo.
echo Server will be available at: http://localhost:8000
echo Press Ctrl+C to stop the server
echo.

REM Start the server
cd backend
python api.py

pause
