"""
Тести для Mouse Controller
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Додавання шляху до модуля
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mouse_controller.core.mouse_mover import MouseMover
from mouse_controller.core.patterns import PatternGenerator
from mouse_controller.utils.helpers import validate_coordinates, get_screen_center


class TestMouseMover(unittest.TestCase):
    """Тести для класу MouseMover"""

    def setUp(self):
        """Налаштування перед кожним тестом"""
        with patch("pyautogui.size", return_value=(1920, 1080)):
            self.mover = MouseMover(failsafe=False, pause=0)

    def test_initialization(self):
        """Тест ініціалізації MouseMover"""
        self.assertEqual(self.mover.screen_width, 1920)
        self.assertEqual(self.mover.screen_height, 1080)
        self.assertEqual(self.mover.center_x, 960)
        self.assertEqual(self.mover.center_y, 540)

    @patch("pyautogui.position")
    def test_get_current_position(self, mock_position):
        """Тест отримання поточної позиції"""
        mock_position.return_value = MagicMock(x=100, y=200)
        x, y = self.mover.get_current_position()
        self.assertEqual(x, 100)
        self.assertEqual(y, 200)

    @patch("pyautogui.moveTo")
    def test_move_to_position_valid(self, mock_move):
        """Тест переміщення в валідну позицію"""
        result = self.mover.move_to_position(500, 300, 1.0)
        self.assertTrue(result)
        mock_move.assert_called_once_with(500, 300, duration=1.0)

    def test_move_to_position_invalid(self):
        """Тест переміщення в невалідну позицію"""
        result = self.mover.move_to_position(-100, 300, 1.0)
        self.assertFalse(result)

        result = self.mover.move_to_position(500, 2000, 1.0)
        self.assertFalse(result)

    @patch("pyautogui.moveTo")
    @patch("pyautogui.position")
    def test_move_relative(self, mock_position, mock_move):
        """Тест відносного переміщення"""
        mock_position.return_value = MagicMock(x=100, y=100)

        result = self.mover.move_relative(50, 75, 1.0)
        self.assertTrue(result)
        mock_move.assert_called_once_with(150, 175, duration=1.0)

    @patch("pyautogui.moveTo")
    def test_move_to_center(self, mock_move):
        """Тест переміщення в центр"""
        result = self.mover.move_to_center(1.0)
        self.assertTrue(result)
        mock_move.assert_called_once_with(960, 540, duration=1.0)


class TestPatternGenerator(unittest.TestCase):
    """Тести для класу PatternGenerator"""

    def setUp(self):
        """Налаштування перед кожним тестом"""
        self.pattern_gen = PatternGenerator()

    def test_generate_circle_points(self):
        """Тест генерації точок кола"""
        points = self.pattern_gen.generate_circle_points(100, 100, 50, 10)
        self.assertEqual(len(points), 11)  # steps + 1

        # Перша і остання точки повинні бути близькими (замкнене коло)
        first_point = points[0]
        last_point = points[-1]
        self.assertAlmostEqual(first_point[0], last_point[0], delta=2)
        self.assertAlmostEqual(first_point[1], last_point[1], delta=2)

    def test_generate_square_points(self):
        """Тест генерації точок квадрата"""
        points = self.pattern_gen.generate_square_points(50, 50, 100)
        expected_points = [
            (50, 50),  # Лівий верхній кут
            (150, 50),  # Правий верхній кут
            (150, 150),  # Правий нижній кут
            (50, 150),  # Лівий нижній кут
            (50, 50),  # Повернення в початок
        ]
        self.assertEqual(points, expected_points)

    def test_generate_triangle_points(self):
        """Тест генерації точок трикутника"""
        points = self.pattern_gen.generate_triangle_points(100, 100, 100)
        self.assertEqual(len(points), 4)  # 3 точки + повернення в початок

        # Перша і остання точки повинні збігатися
        self.assertEqual(points[0], points[-1])

    def test_generate_star_points(self):
        """Тест генерації точок зірки"""
        points = self.pattern_gen.generate_star_points(100, 100, 50, 25, 5)
        expected_length = 5 * 2 + 1  # points * 2 + замикання
        self.assertEqual(len(points), expected_length)

    def test_generate_spiral_points(self):
        """Тест генерації точок спіралі"""
        points = self.pattern_gen.generate_spiral_points(100, 100, 50, 2, 10)
        expected_length = 2 * 10 + 1  # turns * steps_per_turn + 1
        self.assertEqual(len(points), expected_length)

    def test_generate_random_walk(self):
        """Тест генерації випадкового блукання"""
        points = self.pattern_gen.generate_random_walk(100, 100, 5, 10)
        self.assertEqual(len(points), 6)  # початкова точка + steps

        # Перша точка повинна бути початковою
        self.assertEqual(points[0], (100, 100))


class TestHelpers(unittest.TestCase):
    """Тести для допоміжних функцій"""

    def test_validate_coordinates_valid(self):
        """Тест валідації правильних координат"""
        self.assertTrue(validate_coordinates(100, 100, 1920, 1080))
        self.assertTrue(validate_coordinates(0, 0, 1920, 1080))
        self.assertTrue(validate_coordinates(1919, 1079, 1920, 1080))

    def test_validate_coordinates_invalid(self):
        """Тест валідації неправильних координат"""
        self.assertFalse(validate_coordinates(-1, 100, 1920, 1080))
        self.assertFalse(validate_coordinates(100, -1, 1920, 1080))
        self.assertFalse(validate_coordinates(1920, 100, 1920, 1080))
        self.assertFalse(validate_coordinates(100, 1080, 1920, 1080))

    @patch("pyautogui.size", return_value=(1920, 1080))
    def test_get_screen_center(self, mock_size):
        """Тест отримання центру екрана"""
        center_x, center_y = get_screen_center()
        self.assertEqual(center_x, 960)
        self.assertEqual(center_y, 540)


class TestIntegration(unittest.TestCase):
    """Інтеграційні тести"""

    @patch("pyautogui.size", return_value=(1920, 1080))
    @patch("pyautogui.moveTo")
    def test_full_workflow(self, mock_move, mock_size):
        """Тест повного робочого процесу"""
        # Ініціалізація
        mover = MouseMover(failsafe=False, pause=0)
        pattern_gen = PatternGenerator()

        # Генерація патерну
        center_x, center_y = get_screen_center()
        points = pattern_gen.generate_circle_points(center_x, center_y, 100, 10)

        # Виконання руху
        result = mover.move_smooth_path(points, 0.1)
        self.assertTrue(result)

        # Перевірка що moveTo було викликано для кожної точки
        self.assertEqual(mock_move.call_count, len(points))


if __name__ == "__main__":
    # Запуск тестів
    unittest.main(verbosity=2)
