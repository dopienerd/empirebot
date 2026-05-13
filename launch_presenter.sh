#!/bin/bash
# Launch PowerPoint Presenter and open browser

cd /home/user/empirebot

# Kill any existing instance
pkill -f "pptx_presenter.py" 2>/dev/null
sleep 1

# Start the server
python3 /home/user/empirebot/pptx_presenter.py &
SERVER_PID=$!

# Wait for server to be ready
for i in {1..10}; do
    curl -s -o /dev/null http://localhost:5050 && break
    sleep 1
done

# Open browser
if command -v xdg-open &>/dev/null; then
    xdg-open http://localhost:5050
elif command -v firefox &>/dev/null; then
    firefox http://localhost:5050 &
elif command -v google-chrome &>/dev/null; then
    google-chrome http://localhost:5050 &
elif command -v chromium-browser &>/dev/null; then
    chromium-browser http://localhost:5050 &
fi

wait $SERVER_PID
