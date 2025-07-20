#!/usr/bin/env python3
"""
Скрипт для запуску GUI інтерфейсу Mouse Controller
"""

import sys
import os

# Додавання шляху до модуля
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

try:
    from mouse_controller.gui.interface import main

    if __name__ == "__main__":
        main()
except ImportError as e:
    print(f"❌ Помилка імпорту: {e}")
    print("Переконайтеся, що встановлені всі залежності:")
    print("pip install -r requirements.txt")
except Exception as e:
    print(f"❌ Помилка запуску: {e}")
