#!/bin/bash
# AllAtomic Userbot - Startup Script
# Dev: @GhostMarshal | Channel: @ComputeCode

echo "╔═══════════════════════════════════════════════════════╗"
echo "║           ⚛️  AllAtomic Userbot Starting             ║"
echo "╚═══════════════════════════════════════════════════════╝"

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "📋 Copy .env.example to .env and fill in your values:"
    echo "   cp .env.example .env"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt

# Start the bot
echo "🚀 Starting AllAtomic Userbot..."
python3 app/main.py
