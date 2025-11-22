import tkinter as tk
from tkinter import messagebox
import sys
import os

class MathCalculatorMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Математические калькуляторы")
        self.root.geometry("500x450")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        
        # Центрирование окна
        self.center_window()
        
        # Создание интерфейса
        self.create_widgets()
        
    def center_window(self):
        """Центрирует окно на экране"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Создает элементы интерфейса"""
        
        # Заголовок
        title_frame = tk.Frame(self.root, bg="white")
        title_frame.pack(pady=30)
        
        title_label = tk.Label(title_frame, text="🧮 Математические калькуляторы", 
                              bg="white", fg="#2C3E50", font=("Arial", 20, "bold"))
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Выберите тип вычислений", 
                                 bg="white", fg="#7F8C8D", font=("Arial", 12))
        subtitle_label.pack(pady=5)
        
        # Кнопки калькуляторов
        buttons_frame = tk.Frame(self.root, bg="white")
        buttons_frame.pack(pady=30)
        
        # Стиль для кнопок
        button_style = {
            "bg": "#3498DB",
            "fg": "white",
            "font": ("Arial", 12, "bold"),
            "width": 25,
            "height": 2,
            "relief": tk.FLAT,
            "cursor": "hand2",
            "bd": 0
        }
        
        # Кнопка для натуральных чисел
        natural_btn = tk.Button(buttons_frame, text="🔢 Натуральные числа", 
                               command=self.open_natural_calculator, **button_style)
        natural_btn.pack(pady=6)
        natural_btn.bind("<Enter>", lambda e: natural_btn.config(bg="#2980B9"))
        natural_btn.bind("<Leave>", lambda e: natural_btn.config(bg="#3498DB"))
        
        # Кнопка для целых чисел
        integer_btn = tk.Button(buttons_frame, text="🧮 Целые числа", 
                               command=self.open_integer_calculator, **button_style)
        integer_btn.pack(pady=6)
        integer_btn.bind("<Enter>", lambda e: integer_btn.config(bg="#2980B9"))
        integer_btn.bind("<Leave>", lambda e: integer_btn.config(bg="#3498DB"))
        
        # Кнопка для рациональных чисел
        rational_btn = tk.Button(buttons_frame, text="📐 Рациональные числа", 
                                command=self.open_rational_calculator, **button_style)
        rational_btn.pack(pady=6)
        rational_btn.bind("<Enter>", lambda e: rational_btn.config(bg="#2980B9"))
        rational_btn.bind("<Leave>", lambda e: rational_btn.config(bg="#3498DB"))
        
        # Кнопка для многочленов
        polynomial_btn = tk.Button(buttons_frame, text="📊 Многочлены", 
                                  command=self.open_polynomial_calculator, **button_style)
        polynomial_btn.pack(pady=6)
        polynomial_btn.bind("<Enter>", lambda e: polynomial_btn.config(bg="#2980B9"))
        polynomial_btn.bind("<Leave>", lambda e: polynomial_btn.config(bg="#3498DB"))
        
        # Разделитель
        separator = tk.Frame(self.root, bg="#ECF0F1", height=2)
        separator.pack(fill=tk.X, padx=50, pady=20)
        
        # Футер
        footer_frame = tk.Frame(self.root, bg="white")
        footer_frame.pack(pady=10)
        
        info_label = tk.Label(footer_frame, text="Разработано для математических вычислений", 
                             bg="white", fg="#95A5A6", font=("Arial", 9))
        info_label.pack()
        
        version_label = tk.Label(footer_frame, text="Версия 1.0", 
                                bg="white", fg="#BDC3C7", font=("Arial", 8))
        version_label.pack(pady=5)
    
    def open_natural_calculator(self):
        """Открывает калькулятор натуральных чисел"""
        try:
            # Импортируем и запускаем напрямую
            from Natural_GUI import NaturalApp
            natural_window = tk.Toplevel(self.root)
            NaturalApp(natural_window)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть калькулятор натуральных чисел: {str(e)}")
    
    def open_integer_calculator(self):
        """Открывает калькулятор целых чисел"""
        try:
            from Integer_GUI import IntegerApp
            integer_window = tk.Toplevel(self.root)
            IntegerApp(integer_window)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть калькулятор целых чисел: {str(e)}")
    
    def open_rational_calculator(self):
        """Открывает калькулятор рациональных чисел"""
        try:
            from Rational_GUI import RationalApp
            rational_window = tk.Toplevel(self.root)
            RationalApp(rational_window)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть калькулятор рациональных чисел: {str(e)}")
    
    def open_polynomial_calculator(self):
        """Открывает калькулятор многочленов"""
        try:
            from Polynomial_GUI import PolynomialApp
            polynomial_window = tk.Toplevel(self.root)
            PolynomialApp(polynomial_window)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть калькулятор многочленов: {str(e)}")

def main():
    root = tk.Tk()
    app = MathCalculatorMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()