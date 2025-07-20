# 🖱️ Mouse Controller

[![CI](https://github.com/yourusername/mouse-controller/workflows/CI/badge.svg)](https://github.com/yourusername/mouse-controller/actions)
[![codecov](https://codecov.io/gh/yourusername/mouse-controller/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/mouse-controller)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

Professional tool for programmatic mouse cursor movement control with various motion patterns.

## ✨ Features

- **Intuitive Interfaces**: Both console and GUI options
- **Rich Pattern Library**: 10+ movement patterns including geometric shapes and complex curves
- **Safety First**: Built-in failsafe mechanisms and boundary checking
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Extensible**: Easy to add custom patterns and movements
- **Well-Tested**: Comprehensive test suite with high coverage

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mouse-controller.git
cd mouse-controller

# Install dependencies
pip install -r requirements.txt

# Test installation
python test_installation.py
```

### Usage

**GUI Interface (Recommended for beginners):**
```bash
python examples/run_gui.py
```

**Console Interface:**
```bash
python -m mouse_controller.main
```

**Programmatic Usage:**
```python
from mouse_controller import MouseMover, PatternGenerator

# Initialize
mover = MouseMover()
pattern_gen = PatternGenerator()

# Basic movements
mover.move_to_center()
mover.move_in_circle(500, 300, radius=100)

# Complex patterns
points = pattern_gen.generate_star_points(400, 300, 100, 50, 5)
mover.move_smooth_path(points)
```

## 📱 Screenshots

### GUI Interface
![GUI Interface](docs/screenshots/gui_interface.png)

### Console Interface
![Console Interface](docs/screenshots/console_interface.png)

## 🎯 Available Patterns

| Category | Patterns |
|----------|----------|
| **Basic** | Center, Random Position, Relative Movement |
| **Geometric** | Circle, Square, Triangle, Star |
| **Complex** | Spiral, Sine Wave, Heart, Figure-Eight |
| **Random** | Shake, Random Walk, Noise Patterns |

## 🛡️ Safety Features

- **Failsafe Mode**: Move mouse to top-left corner to emergency stop
- **Boundary Validation**: Automatic screen edge detection
- **Speed Controls**: Configurable movement speeds
- **Error Recovery**: Graceful handling of exceptions

## 🔧 Development

### Setup Development Environment

```bash
# Install development dependencies
make install-dev

# Run tests
make test

# Check code quality
make lint

# Format code
make format
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=mouse_controller

# Run specific test
python -m pytest tests/test_mouse_mover.py::TestMouseMover::test_move_to_center -v
```

## 📚 Documentation

- [Quick Start Guide](QUICKSTART.md) - Get up and running quickly
- [Development Guide](DEVELOPMENT.md) - For contributors and developers  
- [API Documentation](docs/api.md) - Complete API reference
- [Examples](examples/) - Code examples and tutorials

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Run the test suite: `make test`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version, etc.)

## 📋 Roadmap

### Version 1.1.0
- [ ] Pattern recording and playback
- [ ] Real-time pattern preview
- [ ] Configuration file support
- [ ] Performance optimizations

### Version 1.2.0
- [ ] REST API for remote control
- [ ] Multi-monitor support
- [ ] Plugin system
- [ ] Advanced pattern editor

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## 🏗️ Architecture

```
mouse_controller/
├── core/              # Core movement logic
│   ├── mouse_mover.py # Main cursor control
│   └── patterns.py    # Pattern generators
├── gui/               # Graphical interface
├── utils/             # Helper functions
├── tests/             # Test suite
└── examples/          # Usage examples
```

## 🔧 Requirements

- **Python**: 3.7 or higher
- **Operating System**: Windows 10+, macOS 10.14+, Linux
- **Dependencies**: See [requirements.txt](requirements.txt)

### Platform-Specific Notes

**Linux**: May require `python3-tk` package:
```bash
sudo apt-get install python3-tk
```

**macOS**: Accessibility permissions may be required for mouse control.

**Windows**: Some antivirus software may flag mouse automation.

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PyAutoGUI](https://github.com/asweigart/pyautogui) - Core mouse control functionality
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI framework
- Python community for excellent libraries and support

## 📞 Support

- 📖 [Documentation](docs/)
- 🐛 [Issue Tracker](https://github.com/yourusername/mouse-controller/issues)
- 💬 [Discussions](https://github.com/yourusername/mouse-controller/discussions)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/mouse-controller&type=Date)](https://star-history.com/#yourusername/mouse-controller&Date)

---

<div align="center">

**[⬆ Back to Top](#-mouse-controller)**

Made with ❤️ by the Mouse Controller team

</div>
