#!/bin/bash

# AllAtomic Userbot Startup Script

echo "⚛️  Starting AllAtomic Userbot..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ .env file not found! Copy .env.example to .env and fill in your credentials."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt --break-system-packages

# Run the bot
echo "🚀 Starting AllAtomic..."
python3 -m AllAtomic
