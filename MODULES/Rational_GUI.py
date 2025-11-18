import tkinter as tk
from tkinter import messagebox
from Rational import Rational
from Integer import Integer
from Natural import Natural

class RationalApp:
    def __init__(self, root):
        # Цветовая схема Гарри Поттера
        self.bg_color = "#1A472A"
        self.window_color = "#2E8B57"
        self.text_color = "#FFD700"
        self.backlight = "#FFA500"
        self.accent_color = "#8B0000"
        self.hover_color = "#DAA520"
        self.button_color = self.accent_color

        self.root = root
        self.root.title("Калькулятор рациональных чисел Хогвартс")
        self.root.geometry("480x550")
        self.root.configure(bg=self.bg_color)

        self.method_var = tk.StringVar(value="Сложение дробей")

        # Заголовок
        title_label = tk.Label(root, text="🧙 Калькулятор рациональных чисел", 
                              bg=self.bg_color, fg=self.text_color, font=("Arial", 16, "bold"))
        title_label.pack(pady=15)

        # Подзаголовок
        subtitle_label = tk.Label(root, text="Магия дробей от Хогвартса! ✨", 
                                 bg=self.bg_color, fg=self.backlight, font=("Arial", 11, "italic"))
        subtitle_label.pack(pady=5)

        # Выбор метода
        methods = [
            "Сокращение дроби",
            "Проверка на целое", 
            "Преобразование целого в дробное",
            "Преобразование дробного в целое",
            "Сложение дробей",
            "Вычитание дробей",
            "Умножение дробей",
            "Деление дробей"
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=15)

        tk.Label(method_frame, text="Выберите заклинание:", bg=self.bg_color, fg=self.text_color, 
                font=("Arial", 11)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.window_color, fg="black",
                               activebackground=self.hover_color, activeforeground="black",
                               font=("Arial", 10), width=18, relief=tk.RAISED, bd=2)
        self.method_menu["menu"].config(bg=self.window_color, fg="black")
        self.method_menu.pack(side=tk.LEFT, padx=10)

        # Контейнер для полей ввода
        self.input_frame = tk.Frame(root, bg=self.bg_color)
        self.input_frame.pack(pady=15)

        # Первая дробь
        self.first_fraction_label = tk.Label(self.input_frame, text="📜 Первая дробь:", bg=self.bg_color, 
                                           fg=self.backlight, font=("Arial", 10, "bold"))
        self.first_fraction_label.grid(row=0, column=0, sticky="w", pady=5)
        
        self.first_fraction_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=25, 
                                           font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.first_fraction_entry.grid(row=1, column=0, pady=5)

        # Вторая дробь
        self.second_fraction_label = tk.Label(self.input_frame, text="⚡ Вторая дробь:", bg=self.bg_color, 
                                            fg=self.text_color, font=("Arial", 10))
        self.second_fraction_label.grid(row=0, column=1, sticky="w", pady=5, padx=(20, 0))
        
        self.second_fraction_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=25, 
                                            font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.second_fraction_entry.grid(row=1, column=1, pady=5, padx=(20, 0))

        # Целое число
        self.integer_label = tk.Label(self.input_frame, text="🏰 Целое число:", bg=self.bg_color, 
                                    fg=self.text_color, font=("Arial", 10))
        self.integer_label.grid(row=2, column=0, sticky="w", pady=(15, 5))
        
        self.integer_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=25, 
                                    font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.integer_entry.grid(row=3, column=0, pady=5)

        # Подсказка
        hint_label = tk.Label(self.input_frame, text="Формат: a/b или целое число", 
                             bg=self.bg_color, fg=self.backlight, font=("Arial", 9, "italic"))
        hint_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

        # Изначально скрываем ненужные поля
        self.hide_all_extra_fields()

        # Метка для результата
        result_frame = tk.Frame(root, bg=self.backlight, bd=3, relief=tk.GROOVE)
        result_frame.pack(pady=20, padx=25, fill=tk.X)
        
        result_title = tk.Label(result_frame, text="🎯 Результат заклинания:", bg=self.backlight, fg="black", 
                               font=("Arial", 11, "bold"))
        result_title.pack(pady=(8, 0))
        
        self.result_label = tk.Label(result_frame, text="Здесь появится результат магических вычислений...", 
                                    bg="white", fg="black", font=("Arial", 12), 
                                    wraplength=380, justify=tk.CENTER, height=3)
        self.result_label.pack(pady=8, padx=8, fill=tk.BOTH, expand=True)

        # Кнопка выполнения
        self.calculate_button = tk.Button(root, text="⚡ Вычислить", command=self.calculate, 
                                         bg=self.button_color, fg="white", font=("Arial", 12, "bold"), 
                                         height=1, width=15, relief=tk.RAISED, bd=3,
                                         cursor="hand2")
        self.calculate_button.pack(pady=15)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))

        # Футер
        footer_label = tk.Label(root, text="Сделано с 💝 для юных волшебников математики", 
                               bg=self.bg_color, fg=self.text_color, font=("Arial", 9))
        footer_label.pack(pady=10)

    def hide_all_extra_fields(self):
        self.second_fraction_label.grid_remove()
        self.second_fraction_entry.grid_remove()
        self.integer_label.grid_remove()
        self.integer_entry.grid_remove()

    def on_option_change(self, value):
        method_name = self.method_var.get()
        self.hide_all_extra_fields()
        self.first_fraction_label.config(fg=self.backlight, text="📜 Первая дробь:")
        
        if method_name in ["Сложение дробей", "Вычитание дробей", "Умножение дробей", "Деление дробей"]:
            self.second_fraction_label.config(fg=self.backlight, text="⚡ Вторая дробь:")
            self.second_fraction_label.grid()
            self.second_fraction_entry.grid()
        elif method_name == "Преобразование целого в дробное":
            self.integer_label.config(fg=self.backlight, text="🏰 Целое число:")
            self.integer_label.grid()
            self.integer_entry.grid()

    def get_Rational(self, fraction_str):
        if not fraction_str:
            raise ValueError("Пустая строка")
        
        if '/' in fraction_str:
            parts = fraction_str.split('/')
            if len(parts) != 2:
                raise ValueError("Неверный формат дроби")
            numerator_str, denominator_str = parts
            if numerator_str[0] == '-':
                if not all(c.isdigit() for c in numerator_str[1:]) or len(numerator_str) == 1:
                    raise ValueError("Неверный числитель")
            else:
                if not all(c.isdigit() for c in numerator_str):
                    raise ValueError("Неверный числитель")
            if not all(c.isdigit() for c in denominator_str) or denominator_str == '0':
                raise ValueError("Неверный знаменатель")
        else:
            if fraction_str[0] == '-':
                if not all(c.isdigit() for c in fraction_str[1:]) or len(fraction_str) == 1:
                    raise ValueError("Не целое число")
            else:
                if not all(c.isdigit() for c in fraction_str):
                    raise ValueError("Не целое число")
        
        return Rational(fraction_str)

    def get_Integer(self, number_str):
        if not number_str:
            raise ValueError("Пустая строка")
        if number_str[0] == '-':
            if not all(c.isdigit() for c in number_str[1:]) or len(number_str) == 1:
                raise ValueError("Не целое число")
        else:
            if not all(c.isdigit() for c in number_str):
                raise ValueError("Не целое число")
        return Integer(number_str)

    def calculate(self):
        self.result_label.config(text='Произношу заклинание... ⚡', fg="black")
        method_name = self.method_var.get()
        first_fraction_str = self.first_fraction_entry.get().strip()

        try:
            first_fraction = self.get_Rational(first_fraction_str)
        except ValueError as e:
            if not first_fraction_str:
                messagebox.showerror("Ошибка", "⚡ Пожалуйста, введите первую дробь")
            else:
                messagebox.showerror("Ошибка", f"⚡ Неверный формат дроби: {str(e)}")
            return

        if method_name in ["Сложение дробей", "Вычитание дробей", "Умножение дробей", "Деление дробей"]:
            second_fraction_str = self.second_fraction_entry.get().strip()

            try:
                second_fraction = self.get_Rational(second_fraction_str)
            except ValueError as e:
                if not second_fraction_str:
                    messagebox.showerror("Ошибка", "⚡ Пожалуйста, введите вторую дробь")
                else:
                    messagebox.showerror("Ошибка", f"⚡ Неверный формат дроби: {str(e)}")
                return

            if method_name == "Сложение дробей":
                result = first_fraction.ADD_QQ_Q(second_fraction)
                self.result_label.config(text=f"🎯 {first_fraction} + {second_fraction} = {result}")

            elif method_name == "Вычитание дробей":
                result = first_fraction.SUB_QQ_Q(second_fraction)
                self.result_label.config(text=f"🎯 {first_fraction} - {second_fraction} = {result}")

            elif method_name == "Умножение дробей":
                result = first_fraction.MUL_QQ_Q(second_fraction)
                self.result_label.config(text=f"🎯 {first_fraction} × {second_fraction} = {result}")

            elif method_name == "Деление дробей":
                try:
                    result = first_fraction.DIV_QQ_Q(second_fraction)
                    self.result_label.config(text=f"🎯 {first_fraction} ÷ {second_fraction} = {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"⚡ {str(e)}")
                    return

        elif method_name == "Преобразование целого в дробное":
            integer_str = self.integer_entry.get().strip()
            try:
                integer_number = self.get_Integer(integer_str)
                result = Rational.TRANS_Z_Q(integer_number)
                self.result_label.config(text=f"✨ Integer('{integer_str}') → {result}")
            except ValueError:
                if not integer_str:
                    messagebox.showerror("Ошибка", "⚡ Пожалуйста, введите целое число")
                else:
                    messagebox.showerror("Ошибка", "⚡ Число должно быть целым (может начинаться с минуса)")
                return

        else:
            if method_name == "Сокращение дроби":
                result = first_fraction.RED_Q_Q()
                self.result_label.config(text=f"✨ {first_fraction} → {result}")

            elif method_name == "Проверка на целое":
                is_integer = first_fraction.INT_Q_B()
                if is_integer == 'да':
                    self.result_label.config(text=f"✅ {first_fraction} — целое число")
                else:
                    self.result_label.config(text=f"❌ {first_fraction} — дробное число")

            elif method_name == "Преобразование дробного в целое":
                try:
                    result = first_fraction.TRANS_Q_Z()
                    self.result_label.config(text=f"✨ {first_fraction} → {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"⚡ {str(e)}")
                    return


def create_RationalApp(root):
    new_root = tk.Toplevel(root)
    app = RationalApp(new_root)
    return app