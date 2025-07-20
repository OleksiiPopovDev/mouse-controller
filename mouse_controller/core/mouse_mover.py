"""
Core MouseMover module for mouse cursor control
"""

import pyautogui
import time
import math
import logging
from typing import Tuple
from ..utils.helpers import validate_coordinates


class MouseMover:
    """Class for controlling mouse cursor movement"""

    def __init__(self, failsafe: bool = True, pause: float = 0.1):
        """
        Initialize MouseMover

        Args:
            failsafe: Enable safe mode (move to corner to stop)
            pause: Pause between commands (seconds)
        """
        pyautogui.FAILSAFE = failsafe
        pyautogui.PAUSE = pause

        self.screen_width, self.screen_height = pyautogui.size()
        self.center_x = self.screen_width // 2
        self.center_y = self.screen_height // 2

        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.logger.info(
            f"MouseMover initialized. Screen size: {self.screen_width}x{self.screen_height}"
        )

    def get_current_position(self) -> Tuple[int, int]:
        """Get current cursor position"""
        pos = pyautogui.position()
        return pos.x, pos.y

    def move_to_position(self, x: int, y: int, duration: float = 1.0) -> bool:
        """
        Smoothly move cursor to specified position

        Args:
            x: X coordinate
            y: Y coordinate
            duration: Movement duration in seconds

        Returns:
            True if movement successful, False if error
        """
        try:
            if not validate_coordinates(x, y, self.screen_width, self.screen_height):
                self.logger.error(f"Invalid coordinates: ({x}, {y})")
                return False

            self.logger.info(f"Moving to position ({x}, {y})")
            pyautogui.moveTo(x, y, duration=duration)
            return True

        except Exception as e:
            self.logger.error(f"Error during movement: {e}")
            return False

    def move_relative(
        self, x_offset: int, y_offset: int, duration: float = 1.0
    ) -> bool:
        """
        Move cursor relative to current position

        Args:
            x_offset: X offset
            y_offset: Y offset
            duration: Movement duration in seconds
        """
        try:
            current_x, current_y = self.get_current_position()
            new_x = current_x + x_offset
            new_y = current_y + y_offset

            return self.move_to_position(new_x, new_y, duration)

        except Exception as e:
            self.logger.error(f"Error during relative movement: {e}")
            return False

    def move_to_center(self, duration: float = 1.0) -> bool:
        """Move cursor to screen center"""
        return self.move_to_position(self.center_x, self.center_y, duration)

    def move_in_circle(
        self,
        center_x: int,
        center_y: int,
        radius: int = 100,
        steps: int = 50,
        clockwise: bool = True,
    ) -> bool:
        """
        Move cursor in a circle

        Args:
            center_x: X coordinate of circle center
            center_y: Y coordinate of circle center
            radius: Circle radius
            steps: Number of steps for complete circle
            clockwise: Clockwise movement
        """
        try:
            self.logger.info(
                f"Moving in circle: center ({center_x}, {center_y}), radius {radius}"
            )

            direction = 1 if clockwise else -1

            for i in range(steps + 1):
                angle = direction * 2 * math.pi * i / steps
                x = int(center_x + radius * math.cos(angle))
                y = int(center_y + radius * math.sin(angle))

                if not validate_coordinates(
                    x, y, self.screen_width, self.screen_height
                ):
                    continue

                pyautogui.moveTo(x, y, duration=0.02)

            return True

        except Exception as e:
            self.logger.error(f"Error during circle movement: {e}")
            return False

    def move_in_square(self, start_x: int, start_y: int, size: int = 200) -> bool:
        """
        Move cursor in a square

        Args:
            start_x: X coordinate of starting point
            start_y: Y coordinate of starting point
            size: Square side size
        """
        try:
            self.logger.info(
                f"Moving in square: start ({start_x}, {start_y}), size {size}"
            )

            points = [
                (start_x, start_y),
                (start_x + size, start_y),
                (start_x + size, start_y + size),
                (start_x, start_y + size),
                (start_x, start_y),
            ]

            for point in points:
                if validate_coordinates(
                    point[0], point[1], self.screen_width, self.screen_height
                ):
                    pyautogui.moveTo(point[0], point[1], duration=0.5)

            return True

        except Exception as e:
            self.logger.error(f"Error during square movement: {e}")
            return False

    def shake_cursor(self, duration: float = 2.0, intensity: int = 50) -> bool:
        """
        Shake cursor with random movements

        Args:
            duration: Shake duration in seconds
            intensity: Shake intensity (maximum offset in pixels)
        """
        try:
            import random

            self.logger.info(
                f"Shaking cursor: duration {duration}s, intensity {intensity}"
            )

            start_time = time.time()
            original_pos = pyautogui.position()

            while time.time() - start_time < duration:
                x_offset = random.randint(-intensity, intensity)
                y_offset = random.randint(-intensity, intensity)

                new_x = original_pos.x + x_offset
                new_y = original_pos.y + y_offset

                if validate_coordinates(
                    new_x, new_y, self.screen_width, self.screen_height
                ):
                    pyautogui.moveTo(new_x, new_y, duration=0.05)

                time.sleep(0.05)

            # Return to original position
            pyautogui.moveTo(original_pos.x, original_pos.y, duration=0.3)
            return True

        except Exception as e:
            self.logger.error(f"Error during cursor shake: {e}")
            return False

    def move_smooth_path(self, points: list, duration_per_point: float = 0.5) -> bool:
        """
        Smooth movement along specified path

        Args:
            points: List of points [(x1, y1), (x2, y2), ...]
            duration_per_point: Time to move to each point
        """
        try:
            self.logger.info(f"Moving along path with {len(points)} points")

            for point in points:
                if validate_coordinates(
                    point[0], point[1], self.screen_width, self.screen_height
                ):
                    pyautogui.moveTo(point[0], point[1], duration=duration_per_point)
                else:
                    self.logger.warning(f"Skipping invalid point: {point}")

            return True

        except Exception as e:
            self.logger.error(f"Error during path movement: {e}")
            return False

    def emergency_stop(self):
        """Emergency stop - move cursor to screen corner"""
        try:
            pyautogui.moveTo(0, 0, duration=0.1)
            self.logger.info("Emergency stop executed")
        except Exception:
            pass
