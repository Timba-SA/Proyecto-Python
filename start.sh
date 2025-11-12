#!/bin/bash
set -e

echo "🐍 Python Playground Suite - Starting..."
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Error: Docker is not running"
    echo "Please start Docker and try again"
    exit 1
fi

echo "✅ Docker is running"
echo ""

# Build and start all services including runner
echo "� Building and starting all services..."
echo ""
docker compose --profile build up --build -d

echo ""
echo "✅ All services started successfully!"
echo ""
echo "📊 Service URLs:"
echo "   - Frontend: http://localhost:5173"
echo "   - Backend API: http://localhost:8000"
echo "   - Database: localhost:5433"
echo ""
echo "📝 Useful commands:"
echo "   - View logs: docker compose logs -f"
echo "   - Stop services: docker compose down"
echo "   - Restart: docker compose restart"
echo ""
