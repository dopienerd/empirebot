#!/bin/bash
# One-click PowerPoint Presenter launcher for Mac/Linux

echo "=========================================="
echo "   PowerPoint Presenter - Starting..."
echo "=========================================="
echo ""

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Find Python
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "ERROR: Python is not installed!"
    echo "Install it from https://www.python.org/downloads/"
    read -p "Press Enter to exit..."
    exit 1
fi

# Install dependencies if needed
echo "Installing dependencies..."
$PYTHON -m pip install python-pptx flask Pillow --quiet 2>/dev/null

# Kill any existing instance
pkill -f "pptx_presenter.py" 2>/dev/null
sleep 1

# Start the server in background
$PYTHON "$SCRIPT_DIR/pptx_presenter.py" &
SERVER_PID=$!

# Wait for server
echo "Waiting for server..."
for i in {1..10}; do
    curl -s -o /dev/null http://localhost:5050 && break
    sleep 1
done

# Open browser
echo "Opening browser..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    open http://localhost:5050
elif command -v xdg-open &>/dev/null; then
    xdg-open http://localhost:5050
fi

echo ""
echo "Presenter is running at http://localhost:5050"
echo "Press Ctrl+C to stop."
echo ""

wait $SERVER_PID
