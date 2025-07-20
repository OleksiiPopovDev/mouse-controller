"""
Допоміжні модулі Mouse Controller
"""

from .helpers import *

__all__ = [
    "validate_coordinates",
    "get_screen_bounds", 
    "get_screen_center",
    "calculate_distance",
    "clamp_coordinates",
    "scale_coordinates", 
    "normalize_duration",
    "get_safe_random_position",
    "interpolate_points",
    "create_smooth_curve"
]
