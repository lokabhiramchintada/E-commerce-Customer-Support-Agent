#!/bin/bash

echo "===================================="
echo "E-commerce Customer Support Agent"
echo "Setup Script"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[1/5] Python found"
echo ""

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "[2/5] Creating virtual environment..."
    python3 -m venv venv
else
    echo "[2/5] Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "[3/5] Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "[4/5] Installing dependencies..."
pip install -r requirements.txt

# Setup environment file
if [ ! -f ".env" ]; then
    echo "[5/5] Setting up environment file..."
    cp .env.example .env
    echo ""
    echo "===================================="
    echo "IMPORTANT: Configure your API key!"
    echo "===================================="
    echo "Please edit the .env file and add your Google Gemini API key"
    echo "Run: nano .env"
else
    echo "[5/5] Environment file already exists"
fi

echo ""
echo "===================================="
echo "Setup Complete!"
echo "===================================="
echo ""
echo "To run the application:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run the server: python main.py"
echo "  3. Open http://localhost:8000 in your browser"
echo ""
