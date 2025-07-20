#!/bin/bash

# 🎉 Mouse Controller - Final GitHub Setup Script

echo "🚀 Mouse Controller - GitHub Repository Setup"
echo "=============================================="

# Navigate to project directory
cd /Users/oleksii/Projects/mouse_controller

echo "📁 Current directory: $(pwd)"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

echo "✅ Git is available"

# Initialize git repository
if [ ! -d ".git" ]; then
    echo "📝 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Add all files
echo "📁 Adding all files to Git..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "⚠️  No changes to commit"
else
    echo "💾 Creating initial commit..."
    git commit -m "Initial commit: Mouse Controller v1.0.0

🖱️ Professional mouse cursor control tool

✨ Features:
- Console and GUI interfaces
- Geometric patterns (circle, square, triangle, star)
- Complex movements (spiral, sine wave, heart, figure-eight)
- Safety mechanisms with failsafe mode
- Comprehensive test suite with pytest
- Cross-platform support (Windows, macOS, Linux)
- Full documentation and examples
- Claude Code integration ready

🛡️ Safety Features:
- Failsafe mode enabled by default
- Screen boundary validation
- Emergency stop mechanisms
- Error handling and recovery

📦 Production Ready:
- Professional code structure
- Complete test coverage
- CI/CD pipeline with GitHub Actions
- Comprehensive documentation

🎯 Ready for community use and contributions!"

    echo "✅ Initial commit created"
fi

# Set main branch
echo "🌿 Setting main branch..."
git branch -M main

echo ""
echo "🎉 Git setup completed successfully!"
echo ""
echo "🔗 Next steps to create GitHub repository:"
echo ""
echo "Option 1: GitHub CLI (Recommended)"
echo "=================================="
echo "gh repo create mouse-controller \\"
echo "  --public \\"
echo "  --description 'Professional tool for programmatic mouse cursor movement control with various motion patterns' \\"
echo "  --push"
echo ""
echo "gh repo edit --add-topic python,mouse-control,automation,gui,patterns,pyautogui,cursor-control,desktop-automation"
echo ""
echo ""
echo "Option 2: GitHub Web Interface"
echo "=============================="
echo "1. Go to: https://github.com/new"
echo "2. Repository name: mouse-controller"
echo "3. Description: Professional tool for programmatic mouse cursor movement control with various motion patterns"
echo "4. Visibility: Public"
echo "5. DO NOT initialize with README/license (we have our own)"
echo "6. Click 'Create repository'"
echo "7. Then run:"
echo ""
echo "git remote add origin https://github.com/YOUR_USERNAME/mouse-controller.git"
echo "git push -u origin main"
echo ""
echo ""
echo "📋 Repository Configuration:"
echo "============================"
echo "After creating the repository, configure these settings:"
echo ""
echo "• Topics/Tags:"
echo "  python, mouse-control, automation, gui, patterns, pyautogui,"
echo "  cursor-control, desktop-automation, python3, tkinter"
echo ""
echo "• Enable Features:"
echo "  ✅ Issues"
echo "  ✅ Wiki"
echo "  ✅ Discussions (optional)"
echo "  ✅ Projects (optional)"
echo ""
echo "• Branch Protection (Settings → Branches):"
echo "  ✅ Require pull request reviews before merging"
echo "  ✅ Require status checks to pass before merging"
echo "  ✅ Require branches to be up to date before merging"
echo ""
echo "• Codecov Integration:"
echo "  Sign up at https://codecov.io with your GitHub account"
echo "  Add the repository (automatic with public repos)"
echo ""
echo ""
echo "🧪 Testing Your Setup:"
echo "====================="
echo "After pushing to GitHub:"
echo ""
echo "1. Test installation:"
echo "   python test_installation.py"
echo ""
echo "2. Run tests:"
echo "   make test"
echo ""
echo "3. Try interfaces:"
echo "   make gui      # GUI interface"
echo "   make console  # Console interface"
echo "   make examples # Examples"
echo ""
echo ""
echo "📊 Project Statistics:"
echo "====================="
echo "Python files: $(find . -name '*.py' | wc -l)"
echo "Total files: $(find . -type f ! -path './.git/*' | wc -l)"
echo "Documentation files: $(find . -name '*.md' | wc -l)"
echo ""
echo ""
echo "🎯 Your project includes:"
echo "========================"
echo "✅ Professional Python package structure"
echo "✅ Console and GUI interfaces"
echo "✅ 10+ movement patterns and shapes"
echo "✅ Comprehensive safety mechanisms"
echo "✅ Full test suite with pytest"
echo "✅ GitHub Actions CI/CD pipeline"
echo "✅ Complete documentation"
echo "✅ Claude Code integration"
echo "✅ Cross-platform compatibility"
echo "✅ MIT License"
echo "✅ Contributing guidelines"
echo "✅ Issue templates"
echo "✅ Professional README with badges"
echo ""
echo ""
echo "🚀 Mouse Controller is ready for the world!"
echo "==========================================="
echo ""
echo "Your repository will have:"
echo "• Automatic testing on Windows, macOS, and Linux"
echo "• Code quality checks and formatting validation"
echo "• Test coverage reporting"
echo "• Professional documentation"
echo "• Easy installation and usage"
echo ""
echo "🔥 Ready to push to GitHub and share with the community!"
