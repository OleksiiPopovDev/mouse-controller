"""
Console interface for Mouse Controller
"""

import sys
import time
from mouse_controller.core.mouse_mover import MouseMover
from mouse_controller.core.patterns import PatternGenerator
from mouse_controller.utils.helpers import get_screen_center, get_safe_random_position


def print_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("🖱️  MOUSE CONTROLLER v1.0")
    print("=" * 50)
    print("1  - Move to screen center")
    print("2  - Move in circle")
    print("3  - Move in square")
    print("4  - Move in triangle")
    print("5  - Move in star")
    print("6  - Move in spiral")
    print("7  - Move in sine wave")
    print("8  - Move in heart shape")
    print("9  - Move in figure eight")
    print("10 - Shake cursor")
    print("11 - Random walk")
    print("12 - Move to random position")
    print("13 - Move to custom position")
    print("14 - Show current cursor position")
    print("0  - Exit")
    print("-" * 50)
    print("💡 Tip: Move mouse to top-left corner for emergency stop")
    print("=" * 50)


def get_user_input(prompt: str, input_type=str, default=None):
    """Safely get user input"""
    try:
        user_input = input(f"{prompt}: ").strip()
        if not user_input and default is not None:
            return default
        return input_type(user_input)
    except ValueError:
        print("❌ Invalid value. Please try again.")
        return get_user_input(prompt, input_type, default)
    except KeyboardInterrupt:
        print("\n👋 Program terminated by user")
        sys.exit(0)


def safe_execute(func, *args, **kwargs):
    """Safely execute function with error handling"""
    try:
        success = func(*args, **kwargs)
        if success:
            print("✅ Operation completed successfully")
        else:
            print("❌ Error during operation")
        return success
    except Exception as e:
        print(f"❌ Critical error: {e}")
        return False


def wait_with_countdown(seconds: int, message: str = "Operation will start in"):
    """Countdown before executing operation"""
    for i in range(seconds, 0, -1):
        print(f"\r{message} {i} seconds...", end="", flush=True)
        time.sleep(1)
    print("\r" + " " * 50, end="")  # Clear line
    print("\r🚀 Starting execution!", flush=True)


def main():
    """Main function for console interface"""
    print("🎯 Initializing Mouse Controller...")

    try:
        mover = MouseMover(failsafe=True, pause=0.1)
        pattern_gen = PatternGenerator()
    except Exception as e:
        print(f"❌ Initialization error: {e}")
        return

    print("✅ Mouse Controller ready!")

    while True:
        try:
            print_menu()
            choice = get_user_input("Select option", str, "0")

            if choice == "0":
                print("👋 Goodbye!")
                break

            elif choice == "1":
                print("📍 Moving to screen center...")
                wait_with_countdown(3)
                safe_execute(mover.move_to_center, 1.0)

            elif choice == "2":
                print("🔄 Setting up circle movement")
                center_x, center_y = get_screen_center()
                radius = get_user_input("Circle radius (pixels)", int, 100)
                clockwise = get_user_input("Clockwise? (y/n)", str, "y").lower() == "y"

                print(
                    f"🔄 Moving in circle (radius: {radius}, center: {center_x}, {center_y})"
                )
                wait_with_countdown(3)
                safe_execute(
                    mover.move_in_circle, center_x, center_y, radius, 100, clockwise
                )

            elif choice == "3":
                print("⬜ Setting up square movement")
                center_x, center_y = get_screen_center()
                size = get_user_input("Square size (pixels)", int, 200)
                start_x = center_x - size // 2
                start_y = center_y - size // 2

                print(f"⬜ Moving in square (size: {size})")
                wait_with_countdown(3)
                safe_execute(mover.move_in_square, start_x, start_y, size)

            elif choice == "4":
                print("🔺 Moving in triangle")
                center_x, center_y = get_screen_center()
                size = get_user_input("Triangle size (pixels)", int, 200)

                points = pattern_gen.generate_triangle_points(center_x, center_y, size)
                wait_with_countdown(3)
                safe_execute(mover.move_smooth_path, points, 0.5)

            elif choice == "5":
                print("⭐ Setting up star movement")
                center_x, center_y = get_screen_center()
                outer_radius = get_user_input("Outer radius (pixels)", int, 150)
                inner_radius = get_user_input("Inner radius (pixels)", int, 75)
                star_points = get_user_input("Number of points", int, 5)

                points = pattern_gen.generate_star_points(
                    center_x, center_y, outer_radius, inner_radius, star_points
                )
                print(f"⭐ Moving in star ({star_points} points)")
                wait_with_countdown(3)
                safe_execute(mover.move_smooth_path, points, 0.3)

            elif choice == "6":
                print("🌀 Setting up spiral")
                center_x, center_y = get_screen_center()
                max_radius = get_user_input("Maximum radius (pixels)", int, 200)
                turns = get_user_input("Number of turns", int, 3)

                points = pattern_gen.generate_spiral_points(
                    center_x, center_y, max_radius, turns, 50
                )
                print(f"🌀 Moving in spiral ({turns} turns)")
                wait_with_countdown(3)
                safe_execute(mover.move_smooth_path, points, 0.05)

            elif choice == "7":
                print("〰️ Setting up sine wave")
                center_x, center_y = get_screen_center()
                length = get_user_input("Wave length (pixels)", int, 400)
                amplitude = get_user_input("Amplitude (pixels)", int, 100)
                frequency = get_user_input("Frequency", float, 2.0)

                start_x = center_x - length // 2
                points = pattern_gen.generate_sine_wave_points(
                    start_x, center_y, length, amplitude, frequency, 100
                )
                print(
                    f"〰️ Moving in sine wave (length: {length}, amplitude: {amplitude})"
                )
                wait_with_countdown(3)
                safe_execute(mover.move_smooth_path, points, 0.05)

            elif choice == "8":
                print("❤️ Moving in heart shape")
                center_x, center_y = get_screen_center()
                size = get_user_input("Heart size", int, 5)

                points = pattern_gen.generate_heart_points(
                    center_x, center_y, size, 100
                )
                wait_with_countdown(3)
                safe_execute(mover.move_smooth_path, points, 0.05)

            elif choice == "9":
                print("8️⃣ Moving in figure eight")
                center_x, center_y = get_screen_center()
                width = get_user_input("Width (pixels)", int, 200)
                height = get_user_input("Height (pixels)", int, 100)

                points = pattern_gen.generate_figure_eight(
                    center_x, center_y, width, height, 100
                )
                wait_with_countdown(3)
                safe_execute(mover.move_smooth_path, points, 0.05)

            elif choice == "10":
                print("🫨 Setting up cursor shake")
                duration = get_user_input("Duration (seconds)", float, 3.0)
                intensity = get_user_input("Intensity (pixels)", int, 50)

                print(f"🫨 Shaking cursor ({duration}s, intensity: {intensity})")
                wait_with_countdown(3)
                safe_execute(mover.shake_cursor, duration, intensity)

            elif choice == "11":
                print("🎲 Setting up random walk")
                current_x, current_y = mover.get_current_position()
                steps = get_user_input("Number of steps", int, 20)
                max_step = get_user_input("Maximum step size (pixels)", int, 50)

                points = pattern_gen.generate_random_walk(
                    current_x, current_y, steps, max_step
                )
                print(f"🎲 Random walk ({steps} steps)")
                wait_with_countdown(3)
                safe_execute(mover.move_smooth_path, points, 0.3)

            elif choice == "12":
                print("🎯 Moving to random position")
                x, y = get_safe_random_position(
                    mover.screen_width, mover.screen_height, 100
                )
                print(f"🎯 Moving to ({x}, {y})")
                wait_with_countdown(3)
                safe_execute(mover.move_to_position, x, y, 1.0)

            elif choice == "13":
                print("📍 Moving to custom position")
                x = get_user_input("X coordinate", int)
                y = get_user_input("Y coordinate", int)
                duration = get_user_input("Duration (seconds)", float, 1.0)

                print(f"📍 Moving to ({x}, {y})")
                wait_with_countdown(3)
                safe_execute(mover.move_to_position, x, y, duration)

            elif choice == "14":
                current_x, current_y = mover.get_current_position()
                print(f"📍 Current cursor position: ({current_x}, {current_y})")

            else:
                print("❌ Invalid choice. Please try again.")

        except KeyboardInterrupt:
            print("\n\n🛑 User interruption. Executing emergency stop...")
            mover.emergency_stop()
            print("👋 Program terminated")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            print("🔄 Returning to main menu...")


if __name__ == "__main__":
    main()
