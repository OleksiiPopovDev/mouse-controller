# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [1.0.0] - 2025-01-20

### Added
- Initial release of Mouse Controller
- Core MouseMover class with basic movement functions
- PatternGenerator with geometric and complex patterns
- Console interface with menu-driven navigation
- GUI interface using Tkinter
- Safety mechanisms including failsafe mode
- Comprehensive test suite with pytest
- Documentation and examples
- Support for the following patterns:
  - Basic movements (center, random, relative)
  - Geometric shapes (circle, square, triangle, star)
  - Complex patterns (spiral, sine wave, heart, figure-eight)
  - Random movements (shake, random walk)
- Utility functions for coordinate validation and helpers
- Cross-platform support (Windows, macOS, Linux)
- Makefile for development automation
- GitHub Actions CI/CD pipeline
- Claude Code integration support

### Features
- **MouseMover class**: Professional cursor control with safety features
- **Pattern generation**: 10+ different movement patterns
- **Dual interfaces**: Both console and GUI options
- **Safety first**: Failsafe mode and boundary checking
- **Extensible**: Easy to add new patterns and features
- **Well tested**: Comprehensive test coverage
- **Documentation**: Complete setup and usage guides

### Safety Features
- Failsafe mode (move to top-left corner to stop)
- Automatic screen boundary validation
- Configurable movement speeds
- Emergency stop functionality
- Error handling and recovery

### Dependencies
- pyautogui >= 0.9.54
- pytest >= 7.0.0 (for development)
- tkinter (usually included with Python)

### Supported Platforms
- Windows 10+
- macOS 10.14+
- Linux (Ubuntu 18.04+, other distributions)

### Known Issues
- GUI may require additional setup on some Linux distributions
- Some antivirus software may flag mouse automation as suspicious
- High DPI displays may require coordinate adjustment

[Unreleased]: https://github.com/yourusername/mouse-controller/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yourusername/mouse-controller/releases/tag/v1.0.0
