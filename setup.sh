#!/bin/bash

echo "🎨 Setting up Creative Visual Coding App..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "⚠️  Please edit .env file with your OpenAI API key"
    echo "   You can get one from: https://platform.openai.com/api-keys"
fi

# Create data directory
mkdir -p data

# Build and start services
echo "🐳 Building and starting Docker services..."
docker-compose up --build -d

echo "✅ Setup complete!"
echo ""
echo "🌐 Access your app:"
echo "   Frontend: http://localhost:3000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "📝 Don't forget to:"
echo "   1. Add your OpenAI API key to .env file"
echo "   2. Restart services: docker-compose restart"
echo ""
echo "🛑 To stop: docker-compose down" 