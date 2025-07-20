#!/usr/bin/env python3
"""
Quick installation and functionality test for Mouse Controller
"""

import sys
import traceback
import os
import locale

# Try to set UTF-8 encoding for better emoji support
try:
    if sys.platform == "win32":
        import io
        # Try to set UTF-8 mode
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        else:
            # Fallback for older Python versions
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
except Exception:
    # If UTF-8 setup fails, we'll use ASCII-safe output
    pass

# Helper function to safely print with emojis
def safe_print(text):
    """Print text, falling back to ASCII if Unicode fails"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Replace emojis with ASCII alternatives
        ascii_text = text.encode('ascii', 'replace').decode('ascii')
        print(ascii_text)

def test_imports():
    """Test imports"""
    try:
        safe_print("🔍 Testing imports...")
        
        import pyautogui
        safe_print("✅ pyautogui imported successfully")
        
        from mouse_controller import MouseMover, PatternGenerator
        safe_print("✅ MouseMover imported successfully")
        safe_print("✅ PatternGenerator imported successfully")
        
        from mouse_controller.utils.helpers import validate_coordinates, get_screen_center
        safe_print("✅ Helper functions imported successfully")
        
        return True
    except Exception as e:
        safe_print(f"❌ Import error: {e}")
        traceback.print_exc()
        return False

def test_basic_functionality():
    """Test basic functionality"""
    try:
        safe_print("\n🧪 Testing basic functionality...")
        
        from mouse_controller import MouseMover, PatternGenerator
        from mouse_controller.utils.helpers import get_screen_center
        
        # Initialize without mouse movement
        mover = MouseMover(failsafe=False, pause=0)
        safe_print("✅ MouseMover initialized")
        
        # Get screen dimensions
        safe_print(f"🖥️  Screen size: {mover.screen_width}x{mover.screen_height}")
        safe_print(f"📍 Screen center: ({mover.center_x}, {mover.center_y})")
        
        # Test PatternGenerator
        pattern_gen = PatternGenerator()
        safe_print("✅ PatternGenerator initialized")
        
        # Generate test points
        center_x, center_y = get_screen_center()
        circle_points = pattern_gen.generate_circle_points(center_x, center_y, 100, 10)
        safe_print(f"✅ Generated {len(circle_points)} points for circle")
        
        square_points = pattern_gen.generate_square_points(100, 100, 200)
        safe_print(f"✅ Generated {len(square_points)} points for square")
        
        # Test coordinate validation
        from mouse_controller.utils.helpers import validate_coordinates
        valid = validate_coordinates(center_x, center_y, mover.screen_width, mover.screen_height)
        safe_print(f"✅ Coordinate validation: {'successful' if valid else 'failed'}")
        
        return True
    except Exception as e:
        safe_print(f"❌ Functionality error: {e}")
        traceback.print_exc()
        return False

def test_gui_availability():
    """Test GUI availability"""
    try:
        safe_print("\n🖼️  Testing GUI...")
        
        import tkinter as tk
        safe_print("✅ tkinter available")
        
        # Test without actually opening GUI
        from mouse_controller.gui.interface import MouseControllerGUI
        safe_print("✅ GUI module imported successfully")
        
        return True
    except ImportError as e:
        safe_print(f"⚠️  GUI unavailable: {e}")
        safe_print("💡 For GUI, tkinter is required: sudo apt-get install python3-tk (Linux)")
        return False
    except Exception as e:
        safe_print(f"❌ GUI error: {e}")
        return False

def main():
    """Main test function"""
    safe_print("🚀 Mouse Controller - Installation Test")
    safe_print("=" * 50)
    
    tests_passed = 0
    total_tests = 3
    
    # Test imports
    if test_imports():
        tests_passed += 1
    
    # Test functionality
    if test_basic_functionality():
        tests_passed += 1
    
    # Test GUI
    if test_gui_availability():
        tests_passed += 1
    
    safe_print("\n" + "=" * 50)
    safe_print(f"📊 Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        safe_print("🎉 All tests passed successfully!")
        safe_print("🖱️  Mouse Controller is ready to use!")
        safe_print("\n💡 Try:")
        safe_print("   python -m mouse_controller.main  (console mode)")
        safe_print("   python examples/run_gui.py       (GUI mode)")
        safe_print("   python examples/basic_usage.py   (examples)")
    else:
        safe_print("⚠️  Some tests failed. Please check installation.")
        
    return tests_passed == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
