#!/usr/bin/env python3
"""
Quick installation and functionality test for Mouse Controller
"""

import sys
import traceback

def test_imports():
    """Test imports"""
    try:
        print("🔍 Testing imports...")
        
        import pyautogui
        print("✅ pyautogui imported successfully")
        
        from mouse_controller import MouseMover, PatternGenerator
        print("✅ MouseMover imported successfully")
        print("✅ PatternGenerator imported successfully")
        
        from mouse_controller.utils.helpers import validate_coordinates, get_screen_center
        print("✅ Helper functions imported successfully")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        traceback.print_exc()
        return False

def test_basic_functionality():
    """Test basic functionality"""
    try:
        print("\n🧪 Testing basic functionality...")
        
        from mouse_controller import MouseMover, PatternGenerator
        from mouse_controller.utils.helpers import get_screen_center
        
        # Initialize without mouse movement
        mover = MouseMover(failsafe=False, pause=0)
        print("✅ MouseMover initialized")
        
        # Get screen dimensions
        print(f"🖥️  Screen size: {mover.screen_width}x{mover.screen_height}")
        print(f"📍 Screen center: ({mover.center_x}, {mover.center_y})")
        
        # Test PatternGenerator
        pattern_gen = PatternGenerator()
        print("✅ PatternGenerator initialized")
        
        # Generate test points
        center_x, center_y = get_screen_center()
        circle_points = pattern_gen.generate_circle_points(center_x, center_y, 100, 10)
        print(f"✅ Generated {len(circle_points)} points for circle")
        
        square_points = pattern_gen.generate_square_points(100, 100, 200)
        print(f"✅ Generated {len(square_points)} points for square")
        
        # Test coordinate validation
        from mouse_controller.utils.helpers import validate_coordinates
        valid = validate_coordinates(center_x, center_y, mover.screen_width, mover.screen_height)
        print(f"✅ Coordinate validation: {'successful' if valid else 'failed'}")
        
        return True
    except Exception as e:
        print(f"❌ Functionality error: {e}")
        traceback.print_exc()
        return False

def test_gui_availability():
    """Test GUI availability"""
    try:
        print("\n🖼️  Testing GUI...")
        
        import tkinter as tk
        print("✅ tkinter available")
        
        # Test without actually opening GUI
        from mouse_controller.gui.interface import MouseControllerGUI
        print("✅ GUI module imported successfully")
        
        return True
    except ImportError as e:
        print(f"⚠️  GUI unavailable: {e}")
        print("💡 For GUI, tkinter is required: sudo apt-get install python3-tk (Linux)")
        return False
    except Exception as e:
        print(f"❌ GUI error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Mouse Controller - Installation Test")
    print("=" * 50)
    
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
    
    print("\n" + "=" * 50)
    print(f"📊 Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed successfully!")
        print("🖱️  Mouse Controller is ready to use!")
        print("\n💡 Try:")
        print("   python -m mouse_controller.main  (console mode)")
        print("   python examples/run_gui.py       (GUI mode)")
        print("   python examples/basic_usage.py   (examples)")
    else:
        print("⚠️  Some tests failed. Please check installation.")
        
    return tests_passed == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
