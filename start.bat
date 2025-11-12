@echo off
echo 🐍 Python Playground Suite - Starting...
echo.

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Docker is not running
    echo Please start Docker Desktop and try again
    pause
    exit /b 1
)

echo ✅ Docker is running
echo.

REM Build and start all services including runner
echo � Building and starting all services...
echo.
docker compose --profile build up --build -d

if errorlevel 1 (
    echo ❌ Failed to start services
    pause
    exit /b 1
)

echo.
echo ✅ All services started successfully!
echo.
echo 📊 Service URLs:
echo    - Frontend: http://localhost:5173
echo    - Backend API: http://localhost:8000
echo    - Database: localhost:5433
echo.
echo � Useful commands:
echo    - View logs: docker compose logs -f
echo    - Stop services: docker compose down
echo    - Restart: docker compose restart
echo.

pause
