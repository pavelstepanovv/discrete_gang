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

        # Окно результата (заменил Label на Text с прокруткой колесиком)
        result_frame = tk.Frame(root, bg=self.backlight, bd=3, relief=tk.GROOVE)
        result_frame.pack(pady=10, padx=25, fill=tk.BOTH, expand=False)

        result_title = tk.Label(result_frame, text="🎯 Результат заклинания:", bg=self.backlight, fg="black", 
                               font=("Arial", 11, "bold"))
        result_title.pack(pady=(8, 0))

        text_container = tk.Frame(result_frame, bg=self.backlight)
        text_container.pack(pady=8, padx=8, fill=tk.BOTH, expand=True)

        self.result_text = tk.Text(text_container, bg="white", fg="black", font=("Arial", 12),
                       wrap=tk.WORD, height=8, relief=tk.SUNKEN, bd=2)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.result_text.config(state=tk.DISABLED)

        scrollbar = tk.Scrollbar(text_container, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text['yscrollcommand'] = scrollbar.set

        def _on_mousewheel(event):
            self.result_text.yview_scroll(-1 * (event.delta // 120), "units")

        self.result_text.bind('<Enter>', lambda e: self.result_text.focus_set())
        self.result_text.bind('<MouseWheel>', _on_mousewheel)

        def set_result(text, fg="black"):
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, text)
            self.result_text.config(fg=fg)
            self.result_text.config(state=tk.DISABLED)

        self.set_result = set_result

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
        # По умолчанию показываем метку и поле для первой дроби
        self.first_fraction_label.config(fg=self.backlight, text="📜 Первая дробь:")
        self.first_fraction_label.grid()
        self.first_fraction_entry.grid()

        if method_name in ["Сложение дробей", "Вычитание дробей", "Умножение дробей", "Деление дробей"]:
            # Две дроби — показываем обе
            self.second_fraction_label.config(fg=self.backlight, text="⚡ Вторая дробь:")
            self.second_fraction_label.grid()
            self.second_fraction_entry.grid()
        elif method_name == "Преобразование дробного в целое":
            # Просим именно дробь в формате a/b
            self.first_fraction_label.config(fg=self.backlight, text="📜 Введите дробь (формат a/b):")
            self.first_fraction_label.grid()
            self.first_fraction_entry.grid()

        elif method_name == "Преобразование целого в дробное":
            # Для преобразования целого в дробное показываем только поле целого
            self.first_fraction_label.grid_remove()
            self.first_fraction_entry.grid_remove()
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
            # Явно проверяем, что числитель и знаменатель не пустые
            if numerator_str == '' or denominator_str == '':
                raise ValueError("Неверный формат дроби")
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
        self.set_result('Произношу заклинание... ⚡', fg="black")
        method_name = self.method_var.get()

        # Для методов, работающих с первой дробью, читаем и проверяем её ввод
        fraction_methods = ["Сокращение дроби", "Проверка на целое",
                            "Сложение дробей", "Вычитание дробей", "Умножение дробей", "Деление дробей"]

        first_fraction = None
        # Для методов, где требуется дробь общего вида, парсим и проверяем
        if method_name in fraction_methods:
            first_fraction_str = self.first_fraction_entry.get().strip()
            try:
                first_fraction = self.get_Rational(first_fraction_str)
            except ValueError as e:
                if not first_fraction_str:
                    messagebox.showerror("Ошибка", "⚡ Пожалуйста, введите первую дробь")
                else:
                    messagebox.showerror("Ошибка", f"⚡ Неверный формат дроби: {str(e)}")
                return

        # Специальная ветка для преобразования дробного в целое: требуем формат a/b (числитель и знаменатель не пустые)
        if method_name == "Преобразование дробного в целое":
            first_fraction_str = self.first_fraction_entry.get().strip()
            if not first_fraction_str:
                messagebox.showerror("Ошибка", "⚡ Пожалуйста, введите первую дробь в формате a/b (например 5/1)")
                return
            if '/' not in first_fraction_str:
                messagebox.showerror("Ошибка", "⚡ Введите дробь в формате a/b (например 5/1), а не целое число")
                return
            parts = first_fraction_str.split('/')
            if len(parts) != 2 or parts[0] == '' or parts[1] == '':
                messagebox.showerror("Ошибка", "⚡ Неверный формат дроби: требуется 'числитель/знаменатель'")
                return
            try:
                first_fraction = self.get_Rational(first_fraction_str)
            except ValueError as e:
                messagebox.showerror("Ошибка", f"⚡ Неверный формат дроби: {str(e)}")
                return

        # Обработка методов
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
                self.set_result(f"🎯 {first_fraction} + {second_fraction} = {result}")

            elif method_name == "Вычитание дробей":
                result = first_fraction.SUB_QQ_Q(second_fraction)
                self.set_result(f"🎯 {first_fraction} - {second_fraction} = {result}")

            elif method_name == "Умножение дробей":
                result = first_fraction.MUL_QQ_Q(second_fraction)
                self.set_result(f"🎯 {first_fraction} × {second_fraction} = {result}")

            elif method_name == "Деление дробей":
                try:
                    result = first_fraction.DIV_QQ_Q(second_fraction)
                    self.set_result(f"🎯 {first_fraction} ÷ {second_fraction} = {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"⚡ {str(e)}")
                    return

        elif method_name == "Преобразование целого в дробное":
            integer_str = self.integer_entry.get().strip()
            try:
                integer_number = self.get_Integer(integer_str)
                result = Rational.TRANS_Z_Q(integer_number)
                # Показываем явно представление в виде дроби с /1
                self.set_result(f"✨ Integer('{integer_str}') → {result.numerator}/{result.denominator}")
            except ValueError:
                if not integer_str:
                    messagebox.showerror("Ошибка", "⚡ Пожалуйста, введите целое число")
                else:
                    messagebox.showerror("Ошибка", "⚡ Число должно быть целым (может начинаться с минуса)")
                return

        else:
            if method_name == "Сокращение дроби":
                result = first_fraction.RED_Q_Q()
                # Показываем результат в виде дроби даже если знаменатель = 1
                self.set_result(f"✨ {first_fraction} → {result.numerator}/{result.denominator}")

            elif method_name == "Проверка на целое":
                is_integer = first_fraction.INT_Q_B()
                if is_integer == 'да':
                    self.set_result(f"✅ {first_fraction} — целое число")
                else:
                    self.set_result(f"❌ {first_fraction} — дробное число")

            elif method_name == "Преобразование дробного в целое":
                try:
                    # Требуем, чтобы пользователь ввёл дробь формата a/b (даже если знаменатель 1)
                    first_fraction_str = self.first_fraction_entry.get().strip()
                    if '/' not in first_fraction_str:
                        messagebox.showerror("Ошибка", "⚡ Введите дробь в формате a/b (например 5/1), а не целое число")
                        return

                    result = first_fraction.TRANS_Q_Z()
                    # Показываем исходную строку ввода и целочисленный результат
                    self.set_result(f"✨ {first_fraction_str} → {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"⚡ {str(e)}")
                    return


def create_RationalApp(root):
    new_root = tk.Toplevel(root)
    app = RationalApp(new_root)
    return app