"""
Mouse Controller - Professional tool for mouse cursor movement control
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .core.mouse_mover import MouseMover
from .core.patterns import PatternGenerator

__all__ = ["MouseMover", "PatternGenerator"]
