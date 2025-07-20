"""
Pattern generator for mouse cursor movement
"""

import math
import random
from typing import List, Tuple


class PatternGenerator:
    """Class for generating various cursor movement patterns"""
    
    @staticmethod
    def generate_circle_points(center_x: int, center_y: int, radius: int, 
                             steps: int = 50, clockwise: bool = True) -> List[Tuple[int, int]]:
        """
        Generate points for circular movement
        
        Args:
            center_x: X coordinate of center
            center_y: Y coordinate of center
            radius: Circle radius
            steps: Number of points
            clockwise: Clockwise movement
            
        Returns:
            List of coordinates [(x, y), ...]
        """
        points = []
        direction = 1 if clockwise else -1
        
        for i in range(steps + 1):
            angle = direction * 2 * math.pi * i / steps
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            points.append((x, y))
            
        return points
    
    @staticmethod
    def generate_square_points(start_x: int, start_y: int, size: int) -> List[Tuple[int, int]]:
        """
        Generate points for square movement
        
        Args:
            start_x: X coordinate of start
            start_y: Y coordinate of start
            size: Square side size
            
        Returns:
            List of coordinates
        """
        return [
            (start_x, start_y),
            (start_x + size, start_y),
            (start_x + size, start_y + size),
            (start_x, start_y + size),
            (start_x, start_y)
        ]
    
    @staticmethod
    def generate_triangle_points(center_x: int, center_y: int, size: int) -> List[Tuple[int, int]]:
        """
        Generate points for triangle movement
        
        Args:
            center_x: X coordinate of center
            center_y: Y coordinate of center
            size: Triangle size
            
        Returns:
            List of coordinates
        """
        height = int(size * math.sqrt(3) / 2)
        
        return [
            (center_x, center_y - height // 2),  # Top point
            (center_x - size // 2, center_y + height // 2),  # Left bottom
            (center_x + size // 2, center_y + height // 2),  # Right bottom
            (center_x, center_y - height // 2)  # Return to start
        ]
    
    @staticmethod
    def generate_star_points(center_x: int, center_y: int, outer_radius: int, 
                           inner_radius: int, points: int = 5) -> List[Tuple[int, int]]:
        """
        Generate points for star movement
        
        Args:
            center_x: X coordinate of center
            center_y: Y coordinate of center
            outer_radius: Outer radius
            inner_radius: Inner radius
            points: Number of star points
            
        Returns:
            List of coordinates
        """
        coordinates = []
        angle_step = math.pi / points
        
        for i in range(points * 2):
            angle = i * angle_step - math.pi / 2
            radius = outer_radius if i % 2 == 0 else inner_radius
            
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            coordinates.append((x, y))
        
        # Close the shape
        coordinates.append(coordinates[0])
        return coordinates
    
    @staticmethod
    def generate_spiral_points(center_x: int, center_y: int, max_radius: int, 
                             turns: int = 3, steps_per_turn: int = 50) -> List[Tuple[int, int]]:
        """
        Generate points for spiral movement
        
        Args:
            center_x: X coordinate of center
            center_y: Y coordinate of center
            max_radius: Maximum spiral radius
            turns: Number of turns
            steps_per_turn: Steps per turn
            
        Returns:
            List of coordinates
        """
        points = []
        total_steps = turns * steps_per_turn
        
        for i in range(total_steps + 1):
            angle = 2 * math.pi * i / steps_per_turn
            radius = max_radius * i / total_steps
            
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            points.append((x, y))
            
        return points
    
    @staticmethod
    def generate_sine_wave_points(start_x: int, start_y: int, length: int, 
                                amplitude: int, frequency: float = 1.0, 
                                steps: int = 100) -> List[Tuple[int, int]]:
        """
        Generate points for sine wave movement
        
        Args:
            start_x: X coordinate of start
            start_y: Y coordinate of start
            length: Wave length
            amplitude: Wave amplitude
            frequency: Wave frequency
            steps: Number of points
            
        Returns:
            List of coordinates
        """
        points = []
        
        for i in range(steps + 1):
            x = start_x + int(length * i / steps)
            y = start_y + int(amplitude * math.sin(2 * math.pi * frequency * i / steps))
            points.append((x, y))
            
        return points
    
    @staticmethod
    def generate_random_walk(start_x: int, start_y: int, steps: int, 
                           max_step_size: int = 50) -> List[Tuple[int, int]]:
        """
        Generate points for random walk movement
        
        Args:
            start_x: X coordinate of start
            start_y: Y coordinate of start
            steps: Number of steps
            max_step_size: Maximum step size
            
        Returns:
            List of coordinates
        """
        points = [(start_x, start_y)]
        current_x, current_y = start_x, start_y
        
        for _ in range(steps):
            dx = random.randint(-max_step_size, max_step_size)
            dy = random.randint(-max_step_size, max_step_size)
            
            current_x += dx
            current_y += dy
            points.append((current_x, current_y))
            
        return points
    
    @staticmethod
    def generate_figure_eight(center_x: int, center_y: int, width: int, 
                            height: int, steps: int = 100) -> List[Tuple[int, int]]:
        """
        Generate points for figure-eight movement
        
        Args:
            center_x: X coordinate of center
            center_y: Y coordinate of center
            width: Figure width
            height: Figure height
            steps: Number of points
            
        Returns:
            List of coordinates
        """
        points = []
        
        for i in range(steps + 1):
            t = 2 * math.pi * i / steps
            
            # Parametric equations for figure 8
            x = int(center_x + width * math.sin(t) / 2)
            y = int(center_y + height * math.sin(2 * t) / 4)
            
            points.append((x, y))
            
        return points
    
    @staticmethod
    def generate_heart_points(center_x: int, center_y: int, size: int, 
                            steps: int = 100) -> List[Tuple[int, int]]:
        """
        Generate points for heart shape movement
        
        Args:
            center_x: X coordinate of center
            center_y: Y coordinate of center
            size: Heart size
            steps: Number of points
            
        Returns:
            List of coordinates
        """
        points = []
        
        for i in range(steps + 1):
            t = 2 * math.pi * i / steps
            
            # Parametric equations for heart
            x = int(center_x + size * 16 * math.sin(t)**3)
            y = int(center_y - size * (13 * math.cos(t) - 5 * math.cos(2*t) - 
                                      2 * math.cos(3*t) - math.cos(4*t)))
            
            points.append((x, y))
            
        return points
