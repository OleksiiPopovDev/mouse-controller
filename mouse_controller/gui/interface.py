"""
Graphical interface for Mouse Controller
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from ..core.mouse_mover import MouseMover
from ..core.patterns import PatternGenerator
from ..utils.helpers import get_screen_center


class MouseControllerGUI:
    """Graphical interface for mouse cursor control"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Controller v1.0")
        self.root.geometry("600x700")
        self.root.configure(bg="#2c3e50")
        
        # Initialize components
        self.mover = MouseMover(failsafe=True, pause=0.1)
        self.pattern_gen = PatternGenerator()
        self.is_running = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup user interface"""
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#2c3e50", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🖱️ Mouse Controller",
            font=("Arial", 20, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50"
        )
        title_label.pack(pady=(0, 20))
        
        # Current position
        self.position_frame = tk.LabelFrame(
            main_frame,
            text="Current Position",
            font=("Arial", 12, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
            bd=2
        )
        self.position_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.position_label = tk.Label(
            self.position_frame,
            text="X: 0, Y: 0",
            font=("Arial", 14),
            fg="#ecf0f1",
            bg="#34495e"
        )
        self.position_label.pack(pady=10)
        
        # Position update
        self.update_position()
        
        # Basic movements
        basic_frame = tk.LabelFrame(
            main_frame,
            text="Basic Movements",
            font=("Arial", 12, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
            bd=2
        )
        basic_frame.pack(fill=tk.X, pady=(0, 10))
        
        basic_buttons = [
            ("📍 To Center", self.move_to_center),
            ("🎯 Random Position", self.move_random),
            ("🫨 Shake", self.shake_cursor),
        ]
        
        for i, (text, command) in enumerate(basic_buttons):
            btn = tk.Button(
                basic_frame,
                text=text,
                command=command,
                font=("Arial", 10),
                bg="#3498db",
                fg="white",
                activebackground="#2980b9",
                relief=tk.FLAT,
                padx=20,
                pady=5
            )
            btn.grid(row=0, column=i, padx=5, pady=10, sticky="ew")
            basic_frame.grid_columnconfigure(i, weight=1)
        
        # Geometric shapes
        shapes_frame = tk.LabelFrame(
            main_frame,
            text="Geometric Shapes",
            font=("Arial", 12, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
            bd=2
        )
        shapes_frame.pack(fill=tk.X, pady=(0, 10))
        
        shape_buttons = [
            ("🔄 Circle", self.move_circle),
            ("⬜ Square", self.move_square),
            ("🔺 Triangle", self.move_triangle),
            ("⭐ Star", self.move_star),
            ("🌀 Spiral", self.move_spiral),
            ("❤️ Heart", self.move_heart),
        ]
        
        for i, (text, command) in enumerate(shape_buttons):
            btn = tk.Button(
                shapes_frame,
                text=text,
                command=command,
                font=("Arial", 10),
                bg="#e74c3c",
                fg="white",
                activebackground="#c0392b",
                relief=tk.FLAT,
                padx=20,
                pady=5
            )
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            shapes_frame.grid_columnconfigure(col, weight=1)
        
        # Waves and complex movements
        waves_frame = tk.LabelFrame(
            main_frame,
            text="Waves and Complex Movements",
            font=("Arial", 12, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
            bd=2
        )
        waves_frame.pack(fill=tk.X, pady=(0, 10))
        
        wave_buttons = [
            ("〰️ Sine Wave", self.move_sine),
            ("8️⃣ Figure Eight", self.move_figure_eight),
            ("🎲 Random Walk", self.random_walk),
        ]
        
        for i, (text, command) in enumerate(wave_buttons):
            btn = tk.Button(
                waves_frame,
                text=text,
                command=command,
                font=("Arial", 10),
                bg="#9b59b6",
                fg="white",
                activebackground="#8e44ad",
                relief=tk.FLAT,
                padx=20,
                pady=5
            )
            btn.grid(row=0, column=i, padx=5, pady=10, sticky="ew")
            waves_frame.grid_columnconfigure(i, weight=1)
        
        # Settings
        settings_frame = tk.LabelFrame(
            main_frame,
            text="Settings",
            font=("Arial", 12, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
            bd=2
        )
        settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Speed
        speed_frame = tk.Frame(settings_frame, bg="#34495e")
        speed_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            speed_frame,
            text="Speed:",
            font=("Arial", 10),
            fg="#ecf0f1",
            bg="#34495e"
        ).pack(side=tk.LEFT)
        
        self.speed_var = tk.DoubleVar(value=1.0)
        self.speed_scale = tk.Scale(
            speed_frame,
            from_=0.1,
            to=3.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.speed_var,
            bg="#34495e",
            fg="#ecf0f1",
            highlightthickness=0,
            troughcolor="#2c3e50"
        )
        self.speed_scale.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Size
        size_frame = tk.Frame(settings_frame, bg="#34495e")
        size_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            size_frame,
            text="Size:",
            font=("Arial", 10),
            fg="#ecf0f1",
            bg="#34495e"
        ).pack(side=tk.LEFT)
        
        self.size_var = tk.IntVar(value=150)
        self.size_scale = tk.Scale(
            size_frame,
            from_=50,
            to=300,
            resolution=10,
            orient=tk.HORIZONTAL,
            variable=self.size_var,
            bg="#34495e",
            fg="#ecf0f1",
            highlightthickness=0,
            troughcolor="#2c3e50"
        )
        self.size_scale.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Status and stop button
        control_frame = tk.Frame(main_frame, bg="#2c3e50")
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.status_label = tk.Label(
            control_frame,
            text="🟢 Ready",
            font=("Arial", 12, "bold"),
            fg="#27ae60",
            bg="#2c3e50"
        )
        self.status_label.pack(side=tk.LEFT)
        
        self.stop_button = tk.Button(
            control_frame,
            text="🛑 STOP",
            command=self.emergency_stop,
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            relief=tk.FLAT,
            padx=20
        )
        self.stop_button.pack(side=tk.RIGHT)
        
        # Info
        info_label = tk.Label(
            main_frame,
            text="💡 Tip: Move mouse to top-left corner for emergency stop",
            font=("Arial", 9),
            fg="#95a5a6",
            bg="#2c3e50",
            wraplength=550
        )
        info_label.pack(pady=(10, 0))
        
    def update_position(self):
        """Update current cursor position"""
        if hasattr(self, 'mover'):
            x, y = self.mover.get_current_position()
            self.position_label.config(text=f"X: {x}, Y: {y}")
        self.root.after(500, self.update_position)  # Update every 500ms
        
    def set_status(self, status: str, color: str = "#27ae60"):
        """Set status"""
        self.status_label.config(text=status, fg=color)
        
    def run_in_thread(self, func, *args, **kwargs):
        """Run function in separate thread"""
        if self.is_running:
            messagebox.showwarning("Warning", "Operation already running!")
            return
            
        def wrapper():
            self.is_running = True
            self.set_status("🔄 Running...", "#f39c12")
            try:
                func(*args, **kwargs)
                self.set_status("✅ Completed", "#27ae60")
            except Exception as e:
                self.set_status("❌ Error", "#e74c3c")
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                self.is_running = False
                self.root.after(2000, lambda: self.set_status("🟢 Ready", "#27ae60"))
                
        thread = threading.Thread(target=wrapper, daemon=True)
        thread.start()
        
    def move_to_center(self):
        """Move to screen center"""
        self.run_in_thread(self.mover.move_to_center, self.speed_var.get())
        
    def move_random(self):
        """Move to random position"""
        from ..utils.helpers import get_safe_random_position
        x, y = get_safe_random_position(self.mover.screen_width, self.mover.screen_height, 100)
        self.run_in_thread(self.mover.move_to_position, x, y, self.speed_var.get())
        
    def shake_cursor(self):
        """Shake cursor"""
        self.run_in_thread(self.mover.shake_cursor, 3.0, 30)
        
    def move_circle(self):
        """Move in circle"""
        center_x, center_y = get_screen_center()
        radius = self.size_var.get()
        self.run_in_thread(self.mover.move_in_circle, center_x, center_y, radius, 100, True)
        
    def move_square(self):
        """Move in square"""
        center_x, center_y = get_screen_center()
        size = self.size_var.get()
        start_x = center_x - size // 2
        start_y = center_y - size // 2
        self.run_in_thread(self.mover.move_in_square, start_x, start_y, size)
        
    def move_triangle(self):
        """Move in triangle"""
        center_x, center_y = get_screen_center()
        size = self.size_var.get()
        points = self.pattern_gen.generate_triangle_points(center_x, center_y, size)
        self.run_in_thread(self.mover.move_smooth_path, points, 0.5)
        
    def move_star(self):
        """Move in star"""
        center_x, center_y = get_screen_center()
        size = self.size_var.get()
        outer_radius = size
        inner_radius = size // 2
        points = self.pattern_gen.generate_star_points(center_x, center_y, outer_radius, inner_radius, 5)
        self.run_in_thread(self.mover.move_smooth_path, points, 0.3)
        
    def move_spiral(self):
        """Move in spiral"""
        center_x, center_y = get_screen_center()
        max_radius = self.size_var.get()
        points = self.pattern_gen.generate_spiral_points(center_x, center_y, max_radius, 3, 50)
        self.run_in_thread(self.mover.move_smooth_path, points, 0.05)
        
    def move_heart(self):
        """Move in heart shape"""
        center_x, center_y = get_screen_center()
        size = self.size_var.get() // 30  # Scaling for heart
        points = self.pattern_gen.generate_heart_points(center_x, center_y, size, 100)
        self.run_in_thread(self.mover.move_smooth_path, points, 0.05)
        
    def move_sine(self):
        """Move in sine wave"""
        center_x, center_y = get_screen_center()
        length = self.size_var.get() * 2
        amplitude = self.size_var.get() // 3
        start_x = center_x - length // 2
        points = self.pattern_gen.generate_sine_wave_points(start_x, center_y, length, amplitude, 2.0, 100)
        self.run_in_thread(self.mover.move_smooth_path, points, 0.05)
        
    def move_figure_eight(self):
        """Move in figure eight"""
        center_x, center_y = get_screen_center()
        width = self.size_var.get()
        height = self.size_var.get() // 2
        points = self.pattern_gen.generate_figure_eight(center_x, center_y, width, height, 100)
        self.run_in_thread(self.mover.move_smooth_path, points, 0.05)
        
    def random_walk(self):
        """Random walk"""
        current_x, current_y = self.mover.get_current_position()
        steps = 20
        max_step = self.size_var.get() // 3
        points = self.pattern_gen.generate_random_walk(current_x, current_y, steps, max_step)
        self.run_in_thread(self.mover.move_smooth_path, points, 0.3)
        
    def emergency_stop(self):
        """Emergency stop"""
        self.is_running = False
        self.mover.emergency_stop()
        self.set_status("🛑 Stopped", "#e74c3c")
        
    def run(self):
        """Run GUI"""
        self.root.mainloop()


def main():
    """Main function to run GUI"""
    try:
        app = MouseControllerGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Critical Error", f"Failed to start application: {e}")


if __name__ == "__main__":
    main()
