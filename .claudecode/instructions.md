# Claude Code Instructions for Mouse Controller

## Project Overview
This is a professional Python project for programmatic mouse cursor control with various motion patterns including geometric shapes, complex patterns, and safety mechanisms.

## Key Components

### Core Classes
- `MouseMover`: Main class for cursor control with safety features
- `PatternGenerator`: Creates various movement patterns (circles, stars, spirals, etc.)
- GUI and console interfaces for user interaction

### Important Files
- `mouse_controller/core/mouse_mover.py`: Core movement logic
- `mouse_controller/core/patterns.py`: Pattern generation algorithms
- `mouse_controller/main.py`: Console interface
- `mouse_controller/gui/interface.py`: Tkinter GUI
- `tests/test_mouse_mover.py`: Unit tests

## Development Guidelines

### Code Style
- Follow PEP 8 standards
- Use type hints where appropriate
- Include comprehensive docstrings
- Maintain consistent error handling

### Testing
- Run tests with: `python -m pytest tests/ -v`
- Maintain high test coverage for core functionality
- Mock pyautogui calls in tests to avoid actual mouse movement

### Safety Considerations
- Always validate coordinates before movement
- Implement failsafe mechanisms (top-left corner emergency stop)
- Use reasonable movement speeds to prevent issues
- Handle exceptions gracefully

## Common Tasks

### Adding New Patterns
1. Add generation method to `PatternGenerator` class
2. Add corresponding GUI button and console menu option
3. Write tests for the new pattern
4. Update documentation

### Modifying Movement Behavior
1. Edit `MouseMover` class methods
2. Ensure safety validations remain intact
3. Update tests accordingly
4. Test thoroughly with different screen resolutions

### GUI Enhancements
1. Modify `mouse_controller/gui/interface.py`
2. Follow existing Tkinter patterns
3. Ensure thread safety for movement operations
4. Maintain consistent styling

## Testing Strategy
- Unit tests for core logic (mocked pyautogui calls)
- Integration tests for pattern generation
- Manual testing for GUI functionality
- Safety testing for boundary conditions

## Deployment Notes
- Ensure pyautogui is properly installed
- Test on different operating systems
- Verify tkinter availability for GUI
- Document platform-specific requirements
