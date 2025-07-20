# Mouse Controller - Інструкції для розробників

## Швидкий старт

### 1. Встановлення залежностей
```bash
pip install -r requirements.txt
```

### 2. Запуск консольного інтерфейсу
```bash
python -m mouse_controller.main
```

### 3. Запуск GUI інтерфейсу
```bash
python examples/run_gui.py
```

### 4. Запуск прикладів
```bash
python examples/basic_usage.py
```

### 5. Запуск тестів
```bash
python -m pytest tests/ -v
```

## Структура проекту

```
mouse_controller/
├── README.md                     # Основна документація
├── requirements.txt              # Python залежності  
├── setup.py                      # Установка пакету
├── pyproject.toml               # Конфігурація проекту
├── .gitignore                   # Git ігнорування файлів
├── mouse_controller/            # Основний пакет
│   ├── __init__.py             # Ініціалізація пакету
│   ├── main.py                 # Консольний інтерфейс
│   ├── core/                   # Основна логіка
│   │   ├── __init__.py
│   │   ├── mouse_mover.py      # Клас управління мишею
│   │   └── patterns.py         # Генератор патернів
│   ├── gui/                    # Графічний інтерфейс
│   │   ├── __init__.py
│   │   └── interface.py        # GUI з Tkinter
│   └── utils/                  # Допоміжні функції
│       ├── __init__.py
│       └── helpers.py          # Утиліти
├── tests/                      # Тести
│   ├── __init__.py
│   └── test_mouse_mover.py     # Юніт тести
└── examples/                   # Приклади використання
    ├── basic_usage.py          # Базові приклади
    └── run_gui.py              # Запуск GUI
```

## Основні компоненти

### MouseMover
Основний клас для управління курсором миші:
- Переміщення в задані координати
- Відносне переміщення
- Рух по геометричних фігурах
- Безпечні механізми зупинки

### PatternGenerator  
Генератор патернів руху:
- Геометричні фігури (коло, квадрат, трикутник, зірка)
- Складні патерни (спіраль, синусоїда, серце, вісімка)
- Випадкові рухи

### GUI Interface
Графічний інтерфейс з можливостями:
- Інтуїтивне управління
- Налаштування швидкості та розміру
- Відображення поточної позиції
- Екстрена зупинка

## API Приклади

### Базове використання
```python
from mouse_controller import MouseMover, PatternGenerator

# Ініціалізація
mover = MouseMover(failsafe=True, pause=0.1)

# Переміщення в центр
mover.move_to_center(duration=1.0)

# Рух по колу
center_x, center_y = 500, 300
mover.move_in_circle(center_x, center_y, radius=100)
```

### Генерація патернів
```python
pattern_gen = PatternGenerator()

# Генерація точок зірки
points = pattern_gen.generate_star_points(400, 300, 100, 50, 5)

# Виконання руху по патерну
mover.move_smooth_path(points, duration_per_point=0.3)
```

### Власний патерн
```python
# Створення власного патерну
custom_points = [
    (100, 100),
    (200, 100), 
    (200, 200),
    (100, 200),
    (100, 100)
]

mover.move_smooth_path(custom_points, duration_per_point=0.5)
```

## Безпека

### Failsafe режим
- Переміщення миші в лівий верхній кут екрана зупиняє всі операції
- Автоматична перевірка меж екрана
- Обробка помилок та виключень

### Обмеження швидкості
- Мінімальна пауза між командами
- Обмеження тривалості рухів
- Валідація координат

## Розробка та тестування

### Запуск тестів
```bash
# Всі тести
python -m pytest tests/ -v

# Тести з покриттям
python -m pytest tests/ --cov=mouse_controller --cov-report=html

# Конкретний тест
python -m pytest tests/test_mouse_mover.py::TestMouseMover::test_move_to_center -v
```

### Лінтинг та форматування
```bash
# Перевірка стилю коду
flake8 mouse_controller/

# Автоматичне форматування
black mouse_controller/ tests/ examples/
```

### Збірка пакету
```bash
# Локальна установка
pip install -e .

# Збірка для розповсюдження  
python -m build
```

## Troubleshooting

### Проблема: "pyautogui.FailSafeException"
**Рішення**: Переміщення миші в кут екрана активує failsafe. Встановіть `failsafe=False` або уникайте кутів.

### Проблема: Тести не запускаються
**Рішення**: Переконайтеся що встановлений pytest: `pip install pytest`

### Проблема: GUI не відкривається
**Рішення**: Перевірте що tkinter встановлений. На Linux: `sudo apt-get install python3-tk`

### Проблема: Курсор рухається занадто швидко/повільно
**Рішення**: Налаштуйте параметр `duration` у функціях руху або змініть `pyautogui.PAUSE`.

## Ліцензія

MIT License - дивіться файл LICENSE для деталей.

## Контрибуція

1. Форк репозиторію
2. Створіть feature гілку: `git checkout -b feature/AmazingFeature`
3. Коміт змін: `git commit -m 'Add some AmazingFeature'`
4. Пуш в гілку: `git push origin feature/AmazingFeature`
5. Відкрийте Pull Request

## Автори

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## Подяки

- PyAutoGUI за основну функціональність
- Tkinter за GUI фреймворк
- Python спільнота за підтримку
