"""
Basic usage examples for Mouse Controller
"""

import sys
import os
import time

# Add path to module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mouse_controller.core.mouse_mover import MouseMover
from mouse_controller.core.patterns import PatternGenerator
from mouse_controller.utils.helpers import get_screen_center, get_safe_random_position


def example_basic_movements():
    """Example of basic cursor movements"""
    print("🖱️ Example: Basic cursor movements")

    # Initialize
    mover = MouseMover(failsafe=True, pause=0.1)

    print("1. Moving to screen center...")
    mover.move_to_center(duration=2.0)
    time.sleep(1)

    print("2. Moving to random position...")
    x, y = get_safe_random_position(mover.screen_width, mover.screen_height, 100)
    mover.move_to_position(x, y, duration=1.5)
    time.sleep(1)

    print("3. Relative movement...")
    mover.move_relative(100, -50, duration=1.0)
    time.sleep(1)

    print("4. Cursor shake...")
    mover.shake_cursor(duration=2.0, intensity=30)

    print("✅ Basic movements completed!")


def example_geometric_shapes():
    """Example of movements along geometric shapes"""
    print("🔷 Example: Geometric shapes")

    mover = MouseMover(failsafe=True, pause=0.05)
    center_x, center_y = get_screen_center()

    print("1. Moving in circle...")
    mover.move_in_circle(center_x, center_y, radius=150, steps=50, clockwise=True)
    time.sleep(1)

    print("2. Moving in square...")
    mover.move_in_square(center_x - 100, center_y - 100, size=200)
    time.sleep(1)

    print("3. Moving in triangle...")
    pattern_gen = PatternGenerator()
    triangle_points = pattern_gen.generate_triangle_points(center_x, center_y, 200)
    mover.move_smooth_path(triangle_points, duration_per_point=0.5)
    time.sleep(1)

    print("4. Moving in star...")
    star_points = pattern_gen.generate_star_points(center_x, center_y, 150, 75, 5)
    mover.move_smooth_path(star_points, duration_per_point=0.3)

    print("✅ Geometric shapes completed!")


def example_complex_patterns():
    """Example of complex movement patterns"""
    print("🌀 Example: Complex patterns")

    mover = MouseMover(failsafe=True, pause=0.02)
    pattern_gen = PatternGenerator()
    center_x, center_y = get_screen_center()

    print("1. Spiral...")
    spiral_points = pattern_gen.generate_spiral_points(
        center_x, center_y, 200, turns=3, steps_per_turn=50
    )
    mover.move_smooth_path(spiral_points, duration_per_point=0.05)
    time.sleep(1)

    print("2. Sine wave...")
    sine_points = pattern_gen.generate_sine_wave_points(
        center_x - 300, center_y, length=600, amplitude=100, frequency=2.0, steps=100
    )
    mover.move_smooth_path(sine_points, duration_per_point=0.05)
    time.sleep(1)

    print("3. Figure eight...")
    eight_points = pattern_gen.generate_figure_eight(
        center_x, center_y, 200, 100, steps=100
    )
    mover.move_smooth_path(eight_points, duration_per_point=0.05)
    time.sleep(1)

    print("4. Heart...")
    heart_points = pattern_gen.generate_heart_points(center_x, center_y, 5, steps=100)
    mover.move_smooth_path(heart_points, duration_per_point=0.05)

    print("✅ Complex patterns completed!")


def example_random_movements():
    """Example of random movements"""
    print("🎲 Example: Random movements")

    mover = MouseMover(failsafe=True, pause=0.1)
    pattern_gen = PatternGenerator()

    current_x, current_y = mover.get_current_position()

    print("1. Random walk...")
    random_points = pattern_gen.generate_random_walk(
        current_x, current_y, steps=15, max_step_size=80
    )
    mover.move_smooth_path(random_points, duration_per_point=0.5)
    time.sleep(1)

    print("2. Series of random positions...")
    for i in range(5):
        x, y = get_safe_random_position(mover.screen_width, mover.screen_height, 100)
        print(f"   Move {i+1}: ({x}, {y})")
        mover.move_to_position(x, y, duration=1.0)
        time.sleep(0.5)

    print("✅ Random movements completed!")


def example_custom_pattern():
    """Example of creating custom pattern"""
    print("🎨 Example: Custom pattern")

    mover = MouseMover(failsafe=True, pause=0.02)
    center_x, center_y = get_screen_center()

    # Create custom pattern - diamond with cross inside
    custom_points = []

    # Outer diamond
    diamond_size = 150
    diamond_points = [
        (center_x, center_y - diamond_size),  # Top
        (center_x + diamond_size, center_y),  # Right
        (center_x, center_y + diamond_size),  # Bottom
        (center_x - diamond_size, center_y),  # Left
        (center_x, center_y - diamond_size),  # Return to start
    ]
    custom_points.extend(diamond_points)

    # Move to center for cross
    custom_points.append((center_x, center_y))

    # Cross inside
    cross_size = 75
    cross_points = [
        (center_x - cross_size, center_y),  # Left
        (center_x + cross_size, center_y),  # Right
        (center_x, center_y),  # Center
        (center_x, center_y - cross_size),  # Top
        (center_x, center_y + cross_size),  # Bottom
    ]
    custom_points.extend(cross_points)

    print("Executing custom pattern: diamond with cross...")
    mover.move_smooth_path(custom_points, duration_per_point=0.3)

    print("✅ Custom pattern completed!")


def main():
    """Main function demonstrating all examples"""
    print("🚀 Mouse Controller Demonstration")
    print("=" * 50)
    print("Press Enter to continue between examples...")
    print("For emergency stop, move mouse to top-left corner")
    print("=" * 50)

    try:
        input("Press Enter to start...")

        example_basic_movements()
        input("\nPress Enter for next example...")

        example_geometric_shapes()
        input("\nPress Enter for next example...")

        example_complex_patterns()
        input("\nPress Enter for next example...")

        example_random_movements()
        input("\nPress Enter for next example...")

        example_custom_pattern()

        print("\n🎉 All examples completed!")
        print("Thank you for using Mouse Controller!")

    except KeyboardInterrupt:
        print("\n\n🛑 Demonstration interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")


if __name__ == "__main__":
    main()
