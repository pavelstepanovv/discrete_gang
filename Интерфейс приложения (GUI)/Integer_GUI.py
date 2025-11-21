import tkinter as tk
from tkinter import messagebox
from Integer import Integer
import argparse


class IntegerApp:
    def __init__(self, root):
        # Улучшенная цветовая схема Барби с лучшей читаемостью
        self.bg_color = "#FFB6C1"  # Светло-розовый фон (мягче)
        self.window_color = "#FFE4E6"  # Очень светлый розовый для окон
        self.text_color = "#8B005D"  # Темно-пурпурный (высокая контрастность)
        self.backlight = "#C71585"  # Яркий розовый для выделения
        self.accent_color = "#DB7093"  # Нежный розово-лиловый для акцентов
        self.hover_color = "#FF69B4"  # Классический розовый Барби при наведении
        self.button_color = self.accent_color

        self.root = root
        self.root.title("💖 Калькулятор целых чисел Барби")
        self.root.geometry("450x550")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 0.97)

        self.method_var = tk.StringVar(value="Сложение двух чисел")

        # Заголовок
        title_label = tk.Label(root, text="👑 Калькулятор целых чисел Барби", 
                              bg=self.bg_color, fg=self.text_color, font=("Arial", 16, "bold"))
        title_label.pack(pady=15)

        # Подзаголовок
        subtitle_label = tk.Label(root, text="Розовая математика для принцесс! ✨", 
                                 bg=self.bg_color, fg=self.backlight, font=("Arial", 11, "italic"))
        subtitle_label.pack(pady=5)

        # Выбор метода
        methods = [
            "Абсолютная величина",
            "Определение знака", 
            "Умножение на -1",
            "Преобразование натурального в целое",
            "Сложение двух чисел",
            "Вычитание двух чисел",
            "Умножение двух чисел",
            "Целочисленное деление",
            "Остаток от деления"
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=15)

        tk.Label(method_frame, text="Выберите операцию:", bg=self.bg_color, fg=self.text_color, 
                font=("Arial", 11)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.window_color, fg=self.text_color, 
                               activebackground=self.hover_color, activeforeground=self.text_color,
                               font=("Arial", 10), width=22, relief=tk.RAISED, bd=2)
        self.method_menu["menu"].config(bg=self.window_color, fg=self.text_color)
        self.method_menu.pack(side=tk.LEFT, padx=10)

        # Контейнер для полей ввода
        self.input_frame = tk.Frame(root, bg=self.bg_color)
        self.input_frame.pack(pady=15)

        # Первое число (всегда видно)
        self.first_number_label = tk.Label(self.input_frame, text="👑 Первое число:", bg=self.bg_color, 
                                          fg=self.backlight, font=("Arial", 10, "bold"))
        self.first_number_label.grid(row=0, column=0, sticky="w", pady=5)
        
        self.first_number_entry = tk.Entry(self.input_frame, bg="white", fg=self.text_color, width=25, 
                                          font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.first_number_entry.grid(row=1, column=0, pady=5)

        # Второе число (изначально скрыто)
        self.second_number_label = tk.Label(self.input_frame, text="💎 Второе число:", bg=self.bg_color, 
                                           fg=self.text_color, font=("Arial", 10))
        self.second_number_label.grid(row=0, column=1, sticky="w", pady=5, padx=(20, 0))
        
        self.second_number_entry = tk.Entry(self.input_frame, bg="white", fg=self.text_color, width=25, 
                                           font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.second_number_entry.grid(row=1, column=1, pady=5, padx=(20, 0))

        # Натуральное число для преобразования (специальное поле)
        self.natural_label = tk.Label(self.input_frame, text="🔢 Натуральное число:", bg=self.bg_color, 
                                     fg=self.text_color, font=("Arial", 10))
        self.natural_label.grid(row=2, column=0, sticky="w", pady=(15, 5))
        
        self.natural_entry = tk.Entry(self.input_frame, bg="white", fg=self.text_color, width=25, 
                                     font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.natural_entry.grid(row=3, column=0, pady=5)

        # Изначально скрываем ненужные поля
        self.hide_all_extra_fields()

        # Метка для результата с барби-оформлением
        result_frame = tk.Frame(root, bg=self.backlight, bd=3, relief=tk.GROOVE)
        result_frame.pack(pady=20, padx=25, fill=tk.X)
        
        result_title = tk.Label(result_frame, text="🎀 Результат:", bg=self.backlight, fg="white", 
                               font=("Arial", 11, "bold"))
        result_title.pack(pady=(8, 0))
        
        self.result_label = tk.Label(result_frame, text="Здесь появится результат вычислений...", 
                                    bg="white", fg=self.text_color, font=("Arial", 12), 
                                    wraplength=380, justify=tk.CENTER, height=3)
        self.result_label.pack(pady=8, padx=8, fill=tk.BOTH, expand=True)

        # Кнопка выполнения с барби-темой
        self.calculate_button = tk.Button(root, text="💖 Вычислить!", command=self.calculate, 
                                         bg=self.button_color, fg="white", font=("Arial", 12, "bold"), 
                                         height=1, width=15, relief=tk.RAISED, bd=3,
                                         cursor="hand2")
        self.calculate_button.pack(pady=15)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))

        # Футер с барби-темой
        footer_label = tk.Label(root, text="Сделано с 💕 для математических принцесс", 
                               bg=self.bg_color, fg=self.text_color, font=("Arial", 9))
        footer_label.pack(pady=10)

    def hide_all_extra_fields(self):
        """Скрывает все дополнительные поля ввода"""
        self.second_number_label.grid_remove()
        self.second_number_entry.grid_remove()
        self.natural_label.grid_remove()
        self.natural_entry.grid_remove()

    def on_option_change(self, value):
        method_name = self.method_var.get()
        
        # Сбрасываем все поля
        self.hide_all_extra_fields()
        self.first_number_label.config(fg=self.backlight, text="👑 Первое число:")
        # По умолчанию показываем поле первого числа (если ранее было скрыто)
        self.first_number_label.grid()
        self.first_number_entry.grid()
        
        # Показываем только нужные поля с соответствующими эмодзи
        if method_name in ["Сложение двух чисел", "Вычитание двух чисел", "Умножение двух чисел",
                          "Целочисленное деление", "Остаток от деления"]:
            self.second_number_label.config(fg=self.backlight, text="💎 Второе число:")
            self.second_number_label.grid()
            self.second_number_entry.grid()
            
        elif method_name == "Преобразование натурального в целое":
            # Показываем только поле для ввода натурального числа
            self.first_number_label.grid_remove()
            self.first_number_entry.grid_remove()
            self.natural_label.config(fg=self.backlight, text="🔢 Введите натуральное число:")
            self.natural_label.grid()
            self.natural_entry.grid()

        # Для методов с одним числом скрываем все дополнительные поля
        elif method_name in ["Абсолютная величина", "Определение знака", "Умножение на -1"]:
            pass  # Только первое число

    def get_Integer(self, number_str):
        """Преобразует строку в Integer с проверкой"""
        if not number_str:
            raise ValueError("Пустая строка")
        # Проверяем, что это целое число (может начинаться с минуса)
        if number_str[0] == '-':
            if not all(c.isdigit() for c in number_str[1:]) or len(number_str) == 1:
                raise ValueError("Не целое число")
        else:
            if not all(c.isdigit() for c in number_str):
                raise ValueError("Не целое число")
        return Integer(number_str)

    def get_Natural(self, number_str):
        """Преобразует строку в натуральное число с проверкой"""
        if not number_str:
            raise ValueError("Пустая строка")
        if not all(c.isdigit() for c in number_str):
            raise ValueError("Не натуральное число")
        return Integer(number_str)  # Natural будет создан внутри Integer

    def calculate(self):
        self.result_label.config(text='Вычисляю... 👑', fg=self.text_color)
        method_name = self.method_var.get()

        # Методы, где требуется ввод первого числа
        first_methods = ["Сложение двух чисел", "Вычитание двух чисел", "Умножение двух чисел",
                         "Целочисленное деление", "Остаток от деления", "Абсолютная величина",
                         "Определение знака", "Умножение на -1"]

        # Обработка специального метода: преобразование натурального в целое
        if method_name == "Преобразование натурального в целое":
            natural_str = self.natural_entry.get().strip()
            try:
                natural_number = self.get_Natural(natural_str)
                result = Integer.TRANS_N_Z(natural_number)
                self.result_label.config(text=f"✨ Natural('{natural_str}') → {result}")
            except ValueError:
                if not natural_str:
                    messagebox.showerror("Ошибка", "💔 Пожалуйста, введите натуральное число")
                else:
                    messagebox.showerror("Ошибка", "💔 Число должно быть натуральным (только цифры)")
                return
            return

        # Для остальных методов требуем ввод первого числа
        if method_name in first_methods:
            first_number_str = self.first_number_entry.get().strip()
            try:
                first_number = self.get_Integer(first_number_str)
            except ValueError:
                if not first_number_str:
                    messagebox.showerror("Ошибка", "💔 Пожалуйста, введите первое число")
                else:
                    messagebox.showerror("Ошибка", "💔 Первое число должно быть целым (может начинаться с минуса)")
                return

        # Обработка парных операций (нужен второй операнд)
        if method_name in ["Сложение двух чисел", "Вычитание двух чисел", "Умножение двух чисел",
                          "Целочисленное деление", "Остаток от деления"]:
            second_number_str = self.second_number_entry.get().strip()
            try:
                second_number = self.get_Integer(second_number_str)
            except ValueError:
                if not second_number_str:
                    messagebox.showerror("Ошибка", "💔 Пожалуйста, введите второе число")
                else:
                    messagebox.showerror("Ошибка", "💔 Второе число должно быть целым (может начинаться с минуса)")
                return

            if method_name == "Сложение двух чисел":
                result = first_number.ADD_ZZ_Z(second_number)
                self.result_label.config(text=f"🎀 {first_number} + {second_number} = {result}")

            elif method_name == "Вычитание двух чисел":
                result = first_number.SUB_ZZ_Z(second_number)
                self.result_label.config(text=f"🎀 {first_number} - {second_number} = {result}")

            elif method_name == "Умножение двух чисел":
                result = first_number.MUL_ZZ_Z(second_number)
                self.result_label.config(text=f"🎀 {first_number} × {second_number} = {result}")

            elif method_name == "Целочисленное деление":
                try:
                    result = first_number.DIV_ZZ_Z(second_number)
                    self.result_label.config(text=f"🎀 {first_number} ÷ {second_number} = {result}")
                except ZeroDivisionError:
                    messagebox.showerror("Ошибка", "💔 Деление на ноль невозможно")
                    return

            elif method_name == "Остаток от деления":
                try:
                    result = first_number.MOD_ZZ_Z(second_number)
                    self.result_label.config(text=f"🎀 {first_number} mod {second_number} = {result}")
                except ZeroDivisionError:
                    messagebox.showerror("Ошибка", "💔 Деление на ноль невозможно")
                    return

            return

        # Одно-аргументные методы
        if method_name == "Абсолютная величина":
            result = first_number.ABS_Z_N()
            self.result_label.config(text=f"✨ |{first_number}| = {result}")

        elif method_name == "Определение знака":
            sign_result = first_number.POZ_Z_D()
            sign_texts = {
                2: f"✨ {first_number} — положительное число",
                0: f"✨ {first_number} — равно нулю",
                1: f"✨ {first_number} — отрицательное число"
            }
            self.result_label.config(text=sign_texts[sign_result])

        elif method_name == "Умножение на -1":
            result = first_number.MUL_ZM_Z()
            self.result_label.config(text=f"✨ -({first_number}) = {result}")


def create_IntegerApp(root):
    new_root = tk.Toplevel(root)
    app = IntegerApp(new_root)
    return app