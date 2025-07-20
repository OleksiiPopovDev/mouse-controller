"""
Helper functions for mouse_controller
"""

import pyautogui
from typing import Tuple


def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """
    Check if coordinates are within screen bounds
    
    Args:
        x: X coordinate
        y: Y coordinate
        screen_width: Screen width
        screen_height: Screen height
        
    Returns:
        True if coordinates are valid, False otherwise
    """
    return 0 <= x < screen_width and 0 <= y < screen_height


def get_screen_bounds() -> Tuple[int, int]:
    """
    Get screen dimensions
    
    Returns:
        Tuple of (width, height)
    """
    return pyautogui.size()


def get_screen_center() -> Tuple[int, int]:
    """
    Get screen center coordinates
    
    Returns:
        Tuple of (center_x, center_y)
    """
    width, height = get_screen_bounds()
    return width // 2, height // 2


def calculate_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    Calculate distance between two points
    
    Args:
        point1: First point (x, y)
        point2: Second point (x, y)
        
    Returns:
        Distance between points
    """
    import math
    
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return math.sqrt(dx**2 + dy**2)


def clamp_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> Tuple[int, int]:
    """
    Clamp coordinates to screen bounds
    
    Args:
        x: X coordinate
        y: Y coordinate
        screen_width: Screen width
        screen_height: Screen height
        
    Returns:
        Clamped coordinates (x, y)
    """
    x = max(0, min(x, screen_width - 1))
    y = max(0, min(y, screen_height - 1))
    return x, y


def scale_coordinates(x: int, y: int, scale_factor: float) -> Tuple[int, int]:
    """
    Scale coordinates
    
    Args:
        x: X coordinate
        y: Y coordinate
        scale_factor: Scaling factor
        
    Returns:
        Scaled coordinates (x, y)
    """
    return int(x * scale_factor), int(y * scale_factor)


def normalize_duration(duration: float, min_duration: float = 0.1, 
                      max_duration: float = 5.0) -> float:
    """
    Normalize movement duration
    
    Args:
        duration: Given duration
        min_duration: Minimum duration
        max_duration: Maximum duration
        
    Returns:
        Normalized duration
    """
    return max(min_duration, min(duration, max_duration))


def get_safe_random_position(screen_width: int, screen_height: int, 
                           margin: int = 50) -> Tuple[int, int]:
    """
    Generate safe random position on screen with margins from edges
    
    Args:
        screen_width: Screen width
        screen_height: Screen height
        margin: Margin from screen edges
        
    Returns:
        Random coordinates (x, y)
    """
    import random
    
    x = random.randint(margin, screen_width - margin)
    y = random.randint(margin, screen_height - margin)
    return x, y


def interpolate_points(start: Tuple[int, int], end: Tuple[int, int], 
                      steps: int) -> list:
    """
    Interpolate points between start and end position
    
    Args:
        start: Start point (x, y)
        end: End point (x, y)
        steps: Number of intermediate points
        
    Returns:
        List of intermediate points
    """
    if steps <= 0:
        return [start, end]
    
    points = []
    dx = (end[0] - start[0]) / (steps + 1)
    dy = (end[1] - start[1]) / (steps + 1)
    
    for i in range(steps + 2):
        x = int(start[0] + dx * i)
        y = int(start[1] + dy * i)
        points.append((x, y))
    
    return points


def create_smooth_curve(points: list, smoothness: int = 3) -> list:
    """
    Create smooth curve from set of points
    
    Args:
        points: List of points [(x, y), ...]
        smoothness: Smoothness level
        
    Returns:
        Smoothed list of points
    """
    if len(points) < 3:
        return points
    
    smooth_points = [points[0]]
    
    for i in range(1, len(points) - 1):
        # Add intermediate points for smoothing
        prev_point = points[i - 1]
        curr_point = points[i]
        next_point = points[i + 1]
        
        # Interpolation between points
        for j in range(smoothness):
            t = j / smoothness
            x = int(curr_point[0] * (1 - t) + next_point[0] * t)
            y = int(curr_point[1] * (1 - t) + next_point[1] * t)
            smooth_points.append((x, y))
    
    smooth_points.append(points[-1])
    return smooth_points
