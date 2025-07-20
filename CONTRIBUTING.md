# Contributing to Mouse Controller

First off, thank you for considering contributing to Mouse Controller! 🎉

The following is a set of guidelines for contributing to Mouse Controller. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Guidelines](#documentation-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

- Be respectful and inclusive
- Focus on what is best for the community
- Show empathy towards other community members
- Accept constructive criticism gracefully

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find that the issue has already been reported. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what behavior you expected**
- **Include screenshots or screen recordings if applicable**
- **Specify your environment** (OS, Python version, screen resolution, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the enhancement**
- **Explain why this enhancement would be useful**
- **Specify if this is a breaking change**

### Your First Code Contribution

Unsure where to begin contributing? You can start by looking through these issue types:

- `good first issue` - Issues that are good for newcomers
- `help wanted` - Issues that need assistance
- `documentation` - Documentation improvements
- `testing` - Testing improvements

### Types of Contributions We're Looking For

- **New movement patterns** - Add creative cursor movement patterns
- **GUI improvements** - Enhance the user interface
- **Performance optimizations** - Make the code faster and more efficient
- **Documentation** - Improve or add documentation
- **Testing** - Add or improve test coverage
- **Bug fixes** - Fix issues in the codebase
- **Safety features** - Enhance safety mechanisms

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment (recommended)

### Setup Steps

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/mouse-controller.git
   cd mouse-controller
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   make install-dev
   # Or manually:
   pip install -r requirements.txt
   pip install pytest pytest-cov black flake8
   pip install -e .
   ```

4. **Verify installation**
   ```bash
   python test_installation.py
   make test
   ```

### Development Tools

We use several tools to maintain code quality:

- **Black** - Code formatting
- **Flake8** - Linting
- **Pytest** - Testing
- **Make** - Build automation

Run these before submitting:
```bash
make format  # Format code with black
make lint    # Check code with flake8
make test    # Run test suite
```

## Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes**
   - Write clean, readable code
   - Add tests for new functionality
   - Update documentation as needed
   - Follow the coding standards

3. **Test your changes**
   ```bash
   make test
   make lint
   python test_installation.py
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add amazing feature
   
   - Detailed description of changes
   - Why this change is needed
   - Any breaking changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Use a clear and descriptive title
   - Fill out the PR template completely
   - Link related issues
   - Add screenshots for UI changes

### Pull Request Requirements

- [ ] Tests pass (`make test`)
- [ ] Code is formatted (`make format`)
- [ ] Linting passes (`make lint`)
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated (for significant changes)
- [ ] No breaking changes (or clearly documented)

## Style Guidelines

### Python Code Style

We follow PEP 8 with some modifications:

- **Line length**: 88 characters (Black default)
- **Quotes**: Use double quotes for strings
- **Imports**: Group imports (standard library, third-party, local)
- **Type hints**: Use type hints for public APIs
- **Docstrings**: Use Google-style docstrings

Example:
```python
def move_to_position(self, x: int, y: int, duration: float = 1.0) -> bool:
    """
    Move cursor to specified position.
    
    Args:
        x: X coordinate
        y: Y coordinate  
        duration: Movement duration in seconds
        
    Returns:
        True if movement successful, False otherwise
        
    Raises:
        ValueError: If coordinates are invalid
    """
    if not self._validate_coordinates(x, y):
        raise ValueError(f"Invalid coordinates: ({x}, {y})")
    
    try:
        pyautogui.moveTo(x, y, duration=duration)
        return True
    except Exception as e:
        self.logger.error(f"Movement failed: {e}")
        return False
```

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Good commit messages:
```
Add spiral pattern generation

- Implement Archimedean spiral algorithm
- Add configurable turn count and step size
- Include comprehensive tests
- Update GUI with spiral option

Fixes #123
```

## Testing Guidelines

### Writing Tests

- Write tests for all new functionality
- Use descriptive test names
- Mock external dependencies (especially pyautogui)
- Test both success and failure cases
- Aim for high test coverage

Example test:
```python
def test_move_to_position_valid_coordinates(self, mock_moveto):
    """Test moving to valid coordinates succeeds"""
    mover = MouseMover(failsafe=False)
    result = mover.move_to_position(500, 300, 1.0)
    
    assert result is True
    mock_moveto.assert_called_once_with(500, 300, duration=1.0)

def test_move_to_position_invalid_coordinates(self):
    """Test moving to invalid coordinates fails"""
    mover = MouseMover(failsafe=False)
    result = mover.move_to_position(-100, 300, 1.0)
    
    assert result is False
```

### Running Tests

```bash
# Run all tests
make test

# Run specific test file
python -m pytest tests/test_mouse_mover.py -v

# Run with coverage
make test-cov

# Run specific test
python -m pytest tests/test_mouse_mover.py::TestMouseMover::test_move_to_center -v
```

## Documentation Guidelines

### Code Documentation

- All public classes and methods should have docstrings
- Use Google-style docstrings
- Include type hints for parameters and return values
- Document exceptions that may be raised

### User Documentation

- Update README.md for significant changes
- Add examples for new features
- Update QUICKSTART.md for setup changes
- Include screenshots for GUI changes

### API Documentation

- Document new APIs in docs/api.md
- Include usage examples
- Explain parameter constraints
- Document safety considerations

## Safety Considerations

Mouse Controller deals with system automation, so safety is paramount:

### Code Safety
- Always validate input parameters
- Implement proper boundary checking
- Include failsafe mechanisms
- Handle exceptions gracefully
- Test on multiple platforms

### User Safety
- Document safety features clearly
- Provide emergency stop mechanisms
- Warn about potential issues
- Include usage best practices

### Testing Safety
- Mock pyautogui calls in tests
- Avoid actual mouse movement in CI
- Test boundary conditions thoroughly
- Verify failsafe mechanisms work

## Getting Help

If you need help with development:

- 📖 Read the [Development Guide](DEVELOPMENT.md)
- 💬 Start a [Discussion](https://github.com/yourusername/mouse-controller/discussions)
- 🐛 Open an [Issue](https://github.com/yourusername/mouse-controller/issues)
- 📧 Contact the maintainers

## Recognition

Contributors will be recognized in:
- README.md contributors section
- CHANGELOG.md for significant contributions
- Release notes for major features

Thank you for contributing to Mouse Controller! 🚀
