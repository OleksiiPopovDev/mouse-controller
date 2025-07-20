#!/bin/bash

# Mouse Controller - Git Setup and GitHub Push Script

echo "🚀 Setting up Mouse Controller repository..."

# Navigate to project directory
cd /Users/oleksii/Projects/mouse_controller

# Initialize Git repository if not already done
if [ ! -d ".git" ]; then
    echo "📝 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Add all files
echo "📁 Adding files to Git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Mouse Controller v1.0.0

🖱️ Professional mouse cursor control tool
✨ Features:
- Console and GUI interfaces
- Geometric patterns (circle, square, triangle, star)
- Complex movements (spiral, sine wave, heart, figure-eight)
- Safety mechanisms and failsafe mode
- Comprehensive test suite with pytest
- Cross-platform support (Windows, macOS, Linux)
- Full documentation and examples
- Claude Code integration ready

🛡️ Safety first:
- Failsafe mode enabled by default
- Screen boundary validation
- Emergency stop mechanisms
- Error handling and recovery

📦 Ready for production use!"

# Set main branch
echo "🌿 Setting up main branch..."
git branch -M main

echo ""
echo "✅ Git repository setup complete!"
echo ""
echo "🔗 Next steps to create GitHub repository:"
echo ""
echo "1. Using GitHub CLI (recommended):"
echo "   gh repo create mouse-controller --public --description 'Professional tool for programmatic mouse cursor movement control' --push"
echo ""
echo "2. Using GitHub web interface:"
echo "   a) Go to https://github.com/new"
echo "   b) Repository name: mouse-controller"
echo "   c) Description: Professional tool for programmatic mouse cursor movement control"
echo "   d) Set to Public"
echo "   e) Do NOT initialize with README (we have our own)"
echo "   f) Click 'Create repository'"
echo "   g) Run these commands:"
echo "      git remote add origin https://github.com/yourusername/mouse-controller.git"
echo "      git push -u origin main"
echo ""
echo "📋 Recommended repository settings:"
echo "   - Topics: python, mouse-control, automation, gui, patterns, pyautogui"
echo "   - Enable Issues and Wiki"
echo "   - Add branch protection rules for main branch"
echo ""
echo "🎉 Repository is ready to push!"
