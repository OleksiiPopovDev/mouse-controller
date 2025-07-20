# Makefile for Mouse Controller project

.PHONY: help install test lint format clean gui console examples build

# Show available commands
help:
	@echo "Mouse Controller - Available commands:"
	@echo ""
	@echo "  install     - Install dependencies"
	@echo "  test        - Run tests"
	@echo "  lint        - Check code (flake8)"
	@echo "  format      - Format code (black)"
	@echo "  clean       - Clean temporary files"
	@echo "  gui         - Run GUI interface"
	@echo "  console     - Run console interface"
	@echo "  examples    - Run examples"
	@echo "  build       - Build package"
	@echo ""

# Install dependencies
install:
	pip install -r requirements.txt
	pip install -e .

# Install dev dependencies
install-dev:
	pip install -r requirements.txt
	pip install pytest pytest-cov black flake8
	pip install -e .

# Run tests
test:
	python -m pytest tests/ -v

# Run tests with coverage
test-cov:
	python -m pytest tests/ --cov=mouse_controller --cov-report=html --cov-report=term

# Code linting
lint:
	flake8 mouse_controller/ tests/ examples/

# Code formatting
format:
	black mouse_controller/ tests/ examples/

# Clean temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .coverage

# Run GUI
gui:
	python examples/run_gui.py

# Run console interface
console:
	python -m mouse_controller.main

# Run examples
examples:
	python examples/basic_usage.py

# Build package
build: clean
	python -m build

# Check package
check:
	python -m twine check dist/*

# Full check (tests + linting)
check-all: test lint
	@echo "✅ All checks passed successfully!"

# Prepare for release
release-prep: clean test lint format
	@echo "📦 Preparing for release..."
	python -m build
	python -m twine check dist/*
	@echo "✅ Ready for release!"

# Local installation
install-local:
	pip install -e .

# Uninstall package
uninstall:
	pip uninstall mouse-controller -y

# Show project structure
tree:
	@echo "📁 Project structure:"
	@find . -type f -name "*.py" | head -20
	@echo "..."

# Quick test of one file
test-quick:
	python -m pytest tests/test_mouse_mover.py::TestMouseMover::test_initialization -v

# Run specific test
test-one TEST_NAME:
	python -m pytest tests/test_mouse_mover.py::$(TEST_NAME) -v

# Show test coverage
coverage:
	python -m pytest tests/ --cov=mouse_controller --cov-report=term-missing

# Generate documentation (if needed)
docs:
	@echo "📚 Generating documentation..."
	@echo "README.md and DEVELOPMENT.md already created"

# Check imports
check-imports:
	python -c "from mouse_controller import MouseMover, PatternGenerator; print('✅ Imports working')"

# Demo
demo: examples

# Project information
info:
	@echo "🖱️  Mouse Controller v1.0"
	@echo "📁 Location: $(PWD)"
	@echo "🐍 Python: $(shell python --version)"
	@echo "📦 Pip: $(shell pip --version)"
	@echo ""
	@echo "📋 Statistics:"
	@echo "   Python files: $(shell find . -name '*.py' | wc -l)"
	@echo "   Lines of code: $(shell find . -name '*.py' -exec wc -l {} + | tail -1)"
	@echo "   Tests: $(shell find tests/ -name 'test_*.py' | wc -l)"
