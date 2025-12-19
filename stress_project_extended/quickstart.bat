@echo off
echo ============================================================
echo ML Stress Detection - Quick Start
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo.
echo Installing requirements...
pip install -r requirements.txt

REM Run setup
echo.
echo Running setup script...
python setup_ml.py

echo.
echo ============================================================
echo Setup complete! 
echo ============================================================
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then visit: http://localhost:8000
echo ============================================================
pause
