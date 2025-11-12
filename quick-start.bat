@echo off
echo 🚀 Quick Start - Python Playground Suite
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

REM Start services without rebuilding
echo 🚀 Starting services (without rebuild)...
docker compose --profile build up -d

if errorlevel 1 (
    echo ❌ Failed to start services
    echo Try using start.bat for a full rebuild
    pause
    exit /b 1
)

echo.
echo ✅ All services started!
echo.
echo 📊 Service URLs:
echo    - Frontend: http://localhost:5173
echo    - Backend API: http://localhost:8000
echo.
echo 💡 Tip: Use 'docker compose logs -f' to view logs
echo.

pause
