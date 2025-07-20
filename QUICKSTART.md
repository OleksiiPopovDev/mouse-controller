# 🖱️ Mouse Controller - Quick Start

## What is this?

Mouse Controller is a professional tool for programmatic mouse cursor control with the ability to create complex movement patterns.

## 🚀 Quick Installation

```bash
# 1. Clone project
git clone <repository-url>
cd mouse_controller

# 2. Install dependencies
pip install -r requirements.txt

# 3. Test installation
python test_installation.py
```

## 🎯 Running

### Console Interface
```bash
python -m mouse_controller.main
```

### GUI Interface
```bash
python examples/run_gui.py
```

### Code Examples
```bash
python examples/basic_usage.py
```

## 📋 Makefile Commands

```bash
make help          # Show all commands
make install       # Install project
make test          # Run tests
make gui           # Run GUI
make console       # Run console
make examples      # Run examples
make clean         # Clean temporary files
```

## 🔧 Programmatic Usage

```python
from mouse_controller import MouseMover, PatternGenerator

# Basic usage
mover = MouseMover()
mover.move_to_center()

# Circle movement
center_x, center_y = 500, 300
mover.move_in_circle(center_x, center_y, radius=100)

# Custom patterns
pattern_gen = PatternGenerator()
points = pattern_gen.generate_star_points(400, 300, 100, 50, 5)
mover.move_smooth_path(points)
```

## ⚡ Main Features

- **Basic movements**: center, random position, relative movement
- **Geometric shapes**: circle, square, triangle, star
- **Complex patterns**: spiral, sine wave, heart, figure-eight
- **GUI interface**: intuitive control
- **Safety**: failsafe mode, coordinate validation

## 🛡️ Safety

- Move mouse to **top-left corner** of screen to stop all operations
- Automatic screen boundary checking
- Safe movement speeds

## 📚 Documentation

- `README.md` - Main documentation
- `DEVELOPMENT.md` - Developer instructions
- `examples/` - Usage examples
- `tests/` - Unit tests

## 🐞 Troubleshooting

**Error: "No module named 'pyautogui'"**
```bash
pip install pyautogui
```

**GUI doesn't start**
```bash
# Linux
sudo apt-get install python3-tk

# macOS
brew install tcl-tk

# Windows
# tkinter usually pre-installed
```

**Tests don't run**
```bash
pip install pytest
```

## 📞 Support

If you encounter problems:
1. Run `python test_installation.py`
2. Check `requirements.txt`
3. Read `DEVELOPMENT.md`

## 🎉 Ready!

The project is fully ready to use. Start with:
```bash
python examples/run_gui.py
```

Good luck! 🖱️✨
