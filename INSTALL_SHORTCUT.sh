#!/bin/bash
# Creates a desktop shortcut for PowerPoint Presenter (Mac/Linux)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=========================================="
echo "   Installing Desktop Shortcut..."
echo "=========================================="

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS - create an .app bundle
    APP_PATH="$HOME/Desktop/PowerPoint Presenter.app"
    mkdir -p "$APP_PATH/Contents/MacOS"
    mkdir -p "$APP_PATH/Contents/Resources"

    cat > "$APP_PATH/Contents/MacOS/launch" << INNEREOF
#!/bin/bash
cd "$SCRIPT_DIR"
"$SCRIPT_DIR/START_PRESENTATION.sh"
INNEREOF
    chmod +x "$APP_PATH/Contents/MacOS/launch"

    cat > "$APP_PATH/Contents/Info.plist" << INNEREOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>PowerPoint Presenter</string>
    <key>CFBundleExecutable</key>
    <string>launch</string>
    <key>CFBundleIdentifier</key>
    <string>com.empirebot.presenter</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
</dict>
</plist>
INNEREOF

    # Copy icon if it exists
    if [ -f "$SCRIPT_DIR/presenter_icon.png" ]; then
        cp "$SCRIPT_DIR/presenter_icon.png" "$APP_PATH/Contents/Resources/icon.png"
    fi

    echo ""
    echo "Mac app created on Desktop: PowerPoint Presenter.app"

else
    # Linux - create .desktop file
    DESKTOP_FILE="$HOME/Desktop/PowerPoint-Presenter.desktop"

    cat > "$DESKTOP_FILE" << INNEREOF
[Desktop Entry]
Version=1.0
Type=Application
Name=PowerPoint Presenter
Comment=View and present .pptx files without PowerPoint
Exec=$SCRIPT_DIR/START_PRESENTATION.sh
Icon=$SCRIPT_DIR/presenter_icon.png
Terminal=false
Categories=Office;Presentation;
StartupNotify=true
INNEREOF

    chmod +x "$DESKTOP_FILE"

    # Trust the desktop file on GNOME
    if command -v gio &>/dev/null; then
        gio set "$DESKTOP_FILE" metadata::trusted true 2>/dev/null
    fi

    echo ""
    echo "Desktop shortcut created: PowerPoint-Presenter.desktop"
fi

echo ""
echo "You can now double-click 'PowerPoint Presenter' on your Desktop!"
echo ""
