import tkinter as tk
from tkinter import messagebox
from Polynomial import Polynomial
import argparse


class PolynomialApp:
    def __init__(self, root):
        # Улучшенная цветовая схема Миньонов
        self.bg_color = "#FFD700"  # Желтый как миньоны
        self.window_color = "#4169E1"  # Синий как комбинезоны
        self.text_color = "#000080"  # Темно-синий как очки (хороший контраст)
        self.backlight = "#DC143C"  # Ярко-красный как язык
        self.accent_color = "#000080"  # Темно-синий для акцентов
        self.hover_color = "#32CD32"  # Зеленый как бананы
        self.button_color = self.accent_color

        self.root = root
        self.root.title("😎 Калькулятор многочленов Миньоны")
        self.root.geometry("650x680")  # Немного увеличил для большего текста
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 0.97)

        # Создаем основной фрейм с прокруткой
        main_frame = tk.Frame(root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.method_var = tk.StringVar(value="Сложение многочленов")

        # Заголовок
        title_label = tk.Label(main_frame, text="😎 Калькулятор многочленов", 
                              bg=self.bg_color, fg=self.text_color, font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Подзаголовок
        subtitle_label = tk.Label(main_frame, text="Ба-на-на! Математика с миньонами! 🍌", 
                                 bg=self.bg_color, fg=self.backlight, font=("Arial", 12, "italic"))
        subtitle_label.pack(pady=2)

        # Выбор метода
        methods = [
            "Сложение многочленов",
            "Вычитание многочленов", 
            "Умножение на рациональное число",
            "Умножение на x^k",
            "Старший коэффициент",
            "Степень многочлена",
            "НОК знаменателей и НОД числителей",
            "Умножение многочленов",
            "Деление многочленов",
            "Остаток от деления",
            "НОД многочленов",
            "Производная многочлена",
            "Кратные корни в простые"
        ]

        method_frame = tk.Frame(main_frame, bg=self.bg_color)
        method_frame.pack(pady=10)

        tk.Label(method_frame, text="Выберите задание:", bg=self.bg_color, fg=self.text_color, 
                font=("Arial", 11)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.window_color, fg="white",
                               activebackground=self.hover_color, activeforeground="white",
                               font=("Arial", 10), width=20, relief=tk.RAISED, bd=2)
        self.method_menu["menu"].config(bg=self.window_color, fg="white")
        self.method_menu.pack(side=tk.LEFT, padx=8)

        # Контейнер для полей ввода
        self.input_frame = tk.Frame(main_frame, bg=self.bg_color)
        self.input_frame.pack(pady=10, fill=tk.X)

        # Первый многочлен (всегда видно)
        self.first_poly_label = tk.Label(self.input_frame, text="😎 Первый многочлен:", bg=self.bg_color, 
                                        fg=self.text_color, font=("Arial", 11, "bold"))
        self.first_poly_label.grid(row=0, column=0, sticky="w", pady=3)
        
        self.first_poly_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=35, 
                                       font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.first_poly_entry.grid(row=1, column=0, pady=3, columnspan=2, sticky="ew")

        # Второй многочлен (изначально скрыто)
        self.second_poly_label = tk.Label(self.input_frame, text="🤓 Второй многочлен:", bg=self.bg_color, 
                                         fg=self.text_color, font=("Arial", 11))
        self.second_poly_label.grid(row=2, column=0, sticky="w", pady=(8, 3))
        
        self.second_poly_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=35, 
                                        font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.second_poly_entry.grid(row=3, column=0, pady=3, columnspan=2, sticky="ew")

        # Рациональное число (специальное поле)
        self.rational_label = tk.Label(self.input_frame, text="🍌 Рациональное число:", bg=self.bg_color, 
                                      fg=self.text_color, font=("Arial", 11))
        self.rational_label.grid(row=4, column=0, sticky="w", pady=(8, 3))
        
        self.rational_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=20, 
                                     font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.rational_entry.grid(row=5, column=0, pady=3, sticky="w")

        # Степень k (специальное поле)
        self.k_label = tk.Label(self.input_frame, text="👓 Степень k:", bg=self.bg_color, 
                               fg=self.text_color, font=("Arial", 11))
        self.k_label.grid(row=4, column=1, sticky="w", pady=(8, 3))
        
        self.k_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=12, 
                              font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.k_entry.grid(row=5, column=1, pady=3, sticky="w")

        # Подсказка для формата ввода (ОБНОВЛЕНА)
        hint_label = tk.Label(self.input_frame, 
                             text="Формат: 2*x^3 + 3*x^2 - x + 5  или  x^2 + 1  или  1/2*x^4 - 1/3*x^2 + 2", 
                             bg=self.bg_color, fg=self.backlight, font=("Arial", 9, "italic"),
                             wraplength=500)
        hint_label.grid(row=6, column=0, columnspan=2, pady=(8, 3))

        # Примеры ввода
        examples_label = tk.Label(self.input_frame, 
                                text="Примеры: '2*x^3 + x - 5', '1/2*x^2 + 3*x', '5' (константа), '0' (нулевой)",
                                bg=self.bg_color, fg=self.text_color, font=("Arial", 8),
                                wraplength=500)
        examples_label.grid(row=7, column=0, columnspan=2, pady=(2, 5))

        # Настройка весов колонок для правильного растягивания
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(1, weight=1)

        # Изначально скрываем ненужные поля
        self.hide_all_extra_fields()

        # Метка для результата с увеличенным шрифтом
        result_frame = tk.Frame(main_frame, bg=self.window_color, bd=2, relief=tk.GROOVE)
        result_frame.pack(pady=10, fill=tk.X)
        
        result_title = tk.Label(result_frame, text="🎯 Результат:", bg=self.window_color, fg="white", 
                               font=("Arial", 12, "bold"))
        result_title.pack(pady=(5, 0))
        
        self.result_label = tk.Label(result_frame, text="Банана! Здесь появится результат...", 
                                    bg="white", fg="black", font=("Arial", 11),  # Увеличил шрифт
                                    wraplength=580, justify=tk.LEFT, height=6)  # Увеличил высоту и ширину
        self.result_label.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

        # Кнопка выполнения (теперь в основном фрейме)
        self.calculate_button = tk.Button(main_frame, text="🚀 Выполнить!", command=self.calculate, 
                                         bg=self.button_color, fg="white", font=("Arial", 12, "bold"), 
                                         height=1, width=14, relief=tk.RAISED, bd=2,
                                         cursor="hand2")
        self.calculate_button.pack(pady=8)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))

        # Футер
        footer_label = tk.Label(main_frame, text="Сделано с 💙 для миньонов-математиков", 
                               bg=self.bg_color, fg=self.text_color, font=("Arial", 9))
        footer_label.pack(pady=5)

    def format_polynomial_reversed(self, poly):
        """Форматирует полином в порядке от старшей степени к младшей"""
        if poly.is_zero():
            return "0"
        
        terms_list = []
        # Получаем все степени и сортируем по убыванию
        sorted_powers = sorted(poly.terms.keys(), reverse=True)
        
        for power in sorted_powers:
            coeff = poly.terms[power]
            if coeff.is_zero():
                continue
            
            coeff_str = str(coeff)
            
            if power == 0:
                terms_list.append(coeff_str)
            elif power == 1:
                if coeff_str == "1":
                    terms_list.append("x")
                elif coeff_str == "-1":
                    terms_list.append("-x")
                else:
                    terms_list.append(f"{coeff_str}*x")
            else:
                if coeff_str == "1":
                    terms_list.append(f"x^{power}")
                elif coeff_str == "-1":
                    terms_list.append(f"-x^{power}")
                else:
                    terms_list.append(f"{coeff_str}*x^{power}")
        
        # Собираем строку, обрабатывая знаки
        result = ""
        for i, term in enumerate(terms_list):
            if i == 0:
                result = term
            else:
                if term.startswith('-'):
                    result += f" - {term[1:]}"
                else:
                    result += f" + {term}"
        
        return result

    def hide_all_extra_fields(self):
        """Скрывает все дополнительные поля ввода"""
        self.second_poly_label.grid_remove()
        self.second_poly_entry.grid_remove()
        self.rational_label.grid_remove()
        self.rational_entry.grid_remove()
        self.k_label.grid_remove()
        self.k_entry.grid_remove()

    def on_option_change(self, value):
        method_name = self.method_var.get()
        
        # Сбрасываем все поля
        self.hide_all_extra_fields()
        self.first_poly_label.config(fg=self.text_color, text="😎 Первый многочлен:")
        
        # Показываем только нужные поля с соответствующими эмодзи
        if method_name in ["Сложение многочленов", "Вычитание многочленов", "Умножение многочленов", 
                          "Деление многочленов", "Остаток от деления", "НОД многочленов"]:
            self.second_poly_label.config(fg=self.text_color, text="🤓 Второй многочлен:")
            self.second_poly_label.grid()
            self.second_poly_entry.grid()
            
        elif method_name == "Умножение на рациональное число":
            self.rational_label.config(fg=self.text_color, text="🍌 Рациональное число:")
            self.rational_label.grid()
            self.rational_entry.grid()
            
        elif method_name == "Умножение на x^k":
            self.k_label.config(fg=self.text_color, text="👓 Степень k:")
            self.k_label.grid()
            self.k_entry.grid()

        # Для методов с одним многочленом скрываем все дополнительные поля
        elif method_name in ["Старший коэффициент", "Степень многочлена", 
                           "НОК знаменателей и НОД числителей", "Производная многочлена", 
                           "Кратные корни в простые"]:
            pass  # Только первый многочлен

    def get_Polynomial(self, poly_str):
        """Преобразует строку в Polynomial с проверкой"""
        if not poly_str:
            raise ValueError("Пустая строка")
        
        # Убираем лишние пробелы
        poly_str = poly_str.strip()
        if not poly_str:
            raise ValueError("Пустая строка")
        
        # Проверяем базовую структуру
        if any(char.isalpha() and char != 'x' for char in poly_str):
            raise ValueError("Недопустимые символы в полиноме")
        
        try:
            return Polynomial(poly_str)
        except Exception as e:
            raise ValueError(f"Неверный формат полинома: {str(e)}")

    def get_Rational(self, rational_str):
        """Преобразует строку в рациональное число с проверкой"""
        if not rational_str:
            raise ValueError("Пустая строка")
        
        rational_str = rational_str.strip()
        
        # Проверяем формат рационального числа
        if '/' in rational_str:
            parts = rational_str.split('/')
            if len(parts) != 2:
                raise ValueError("Неверный формат рационального числа (должен быть a/b)")
            num_str, den_str = parts
            if not num_str.lstrip('-').replace('.', '').isdigit() or not den_str.replace('.', '').isdigit():
                raise ValueError("Числитель и знаменатель должны быть числами")
        else:
            # Целое число
            if not rational_str.lstrip('-').replace('.', '').isdigit():
                raise ValueError("Не числовое значение")
        
        from Rational import Rational
        try:
            return Rational(rational_str)
        except Exception as e:
            raise ValueError(f"Неверный формат рационального числа: {str(e)}")

    def get_Natural(self, k_str):
        """Преобразует строку в натуральное число с проверкой"""
        if not k_str:
            raise ValueError("Пустая строка")
        
        if not k_str.isdigit():
            raise ValueError("Степень должна быть натуральным числом")
        
        k = int(k_str)
        if k < 0:
            raise ValueError("Степень должна быть неотрицательной")
        
        from Natural import Natural
        return Natural(str(k))

    def calculate(self):
        self.result_label.config(text='Вычисляю... Ба-на-на! 🍌', fg="black")
        method_name = self.method_var.get()
        first_poly_str = self.first_poly_entry.get().strip()

        try:
            first_poly = self.get_Polynomial(first_poly_str)
        except ValueError as e:
            if not first_poly_str:
                messagebox.showerror("Ошибка", "😢 Банана! Введите первый многочлен")
            else:
                messagebox.showerror("Ошибка", f"😠 Неверный формат полинома: {str(e)}")
            return

        if method_name in ["Сложение многочленов", "Вычитание многочленов", "Умножение многочленов", 
                          "Деление многочленов", "Остаток от деления", "НОД многочленов"]:

            second_poly_str = self.second_poly_entry.get().strip()

            try:
                second_poly = self.get_Polynomial(second_poly_str)
            except ValueError as e:
                if not second_poly_str:
                    messagebox.showerror("Ошибка", "😢 Банана! Введите второй многочлен")
                else:
                    messagebox.showerror("Ошибка", f"😠 Неверный формат полинома: {str(e)}")
                return

            try:
                if method_name == "Сложение многочленов":
                    result = first_poly.ADD_PP_P(second_poly)
                    formatted_result = self.format_polynomial_reversed(result)
                    self.result_label.config(text=f"🎉 Сумма:\n({self.format_polynomial_reversed(first_poly)}) + ({self.format_polynomial_reversed(second_poly)}) = {formatted_result}")

                elif method_name == "Вычитание многочленов":
                    result = first_poly.SUB_PP_P(second_poly)
                    formatted_result = self.format_polynomial_reversed(result)
                    self.result_label.config(text=f"🎉 Разность:\n({self.format_polynomial_reversed(first_poly)}) - ({self.format_polynomial_reversed(second_poly)}) = {formatted_result}")

                elif method_name == "Умножение многочленов":
                    result = first_poly.MUL_PP_P(second_poly)
                    formatted_result = self.format_polynomial_reversed(result)
                    self.result_label.config(text=f"🎉 Произведение:\n({self.format_polynomial_reversed(first_poly)}) × ({self.format_polynomial_reversed(second_poly)}) = {formatted_result}")

                elif method_name == "Деление многочленов":
                    result = first_poly.DIV_PP_P(second_poly)
                    formatted_result = self.format_polynomial_reversed(result)
                    self.result_label.config(text=f"🎉 Частное:\n({self.format_polynomial_reversed(first_poly)}) ÷ ({self.format_polynomial_reversed(second_poly)}) = {formatted_result}")

                elif method_name == "Остаток от деления":
                    result = first_poly.MOD_PP_P(second_poly)
                    formatted_result = self.format_polynomial_reversed(result)
                    self.result_label.config(text=f"🎉 Остаток:\n({self.format_polynomial_reversed(first_poly)}) mod ({self.format_polynomial_reversed(second_poly)}) = {formatted_result}")

                elif method_name == "НОД многочленов":
                    result = first_poly.GCF_PP_P(second_poly)
                    formatted_result = self.format_polynomial_reversed(result)
                    self.result_label.config(text=f"🎉 НОД:\nНОД(({self.format_polynomial_reversed(first_poly)}), ({self.format_polynomial_reversed(second_poly)})) = {formatted_result}")

            except ZeroDivisionError:
                messagebox.showerror("Ошибка", "😠 Ой-ой! Деление на нулевой многочлен!")
                return
            except Exception as e:
                messagebox.showerror("Ошибка", f"😠 Математическая ошибка: {str(e)}")
                return

        elif method_name == "Умножение на рациональное число":
            rational_str = self.rational_entry.get().strip()
            try:
                rational_num = self.get_Rational(rational_str)
                result = first_poly.MUL_PQ_P(rational_num)
                formatted_result = self.format_polynomial_reversed(result)
                self.result_label.config(text=f"🎉 Умножение на число:\n({self.format_polynomial_reversed(first_poly)}) × {rational_num} = {formatted_result}")
            except ValueError as e:
                if not rational_str:
                    messagebox.showerror("Ошибка", "🍌 Банана! Введите рациональное число")
                else:
                    messagebox.showerror("Ошибка", f"🍌 Неверный формат числа: {str(e)}")
                return

        elif method_name == "Умножение на x^k":
            k_str = self.k_entry.get().strip()
            try:
                k = self.get_Natural(k_str)
                result = first_poly.MUL_Pxk_P(k)
                formatted_result = self.format_polynomial_reversed(result)
                self.result_label.config(text=f"🎉 Умножение на x^k:\n({self.format_polynomial_reversed(first_poly)}) × x^{k} = {formatted_result}")
            except ValueError as e:
                if not k_str:
                    messagebox.showerror("Ошибка", "👓 Банана! Введите степень k")
                else:
                    messagebox.showerror("Ошибка", f"👓 {str(e)}")
                return

        else:
            try:
                if method_name == "Старший коэффициент":
                    result = first_poly.LED_P_Q()
                    self.result_label.config(text=f"🎉 Старший коэффициент:\nПолином: {self.format_polynomial_reversed(first_poly)}\nСтарший коэффициент = {result}")

                elif method_name == "Степень многочлена":
                    result = first_poly.DEG_P_N()
                    self.result_label.config(text=f"🎉 Степень полинома:\nПолином: {self.format_polynomial_reversed(first_poly)}\nСтепень = {result}")

                elif method_name == "НОК знаменателей и НОД числителей":
                    result = first_poly.FAC_P_Q()
                    self.result_label.config(text=f"🎉 НОК знаменателей и НОД числителей:\nПолином: {self.format_polynomial_reversed(first_poly)}\nРезультат = {result}")

                elif method_name == "Производная многочлена":
                    result = first_poly.DER_P_P()
                    formatted_result = self.format_polynomial_reversed(result)
                    self.result_label.config(text=f"🎉 Производная:\nПолином: {self.format_polynomial_reversed(first_poly)}\nПроизводная = {formatted_result}")

                elif method_name == "Кратные корни в простые":
                    result = first_poly.NMR_P_P()
                    formatted_result = self.format_polynomial_reversed(result)
                    self.result_label.config(text=f"🎉 Упрощение (кратные корни → простые):\nИсходный: {self.format_polynomial_reversed(first_poly)}\nУпрощенный = {formatted_result}")

            except Exception as e:
                messagebox.showerror("Ошибка", f"😠 Математическая ошибка: {str(e)}")
                return


def create_PolynomialApp(root):
    new_root = tk.Toplevel(root)
    app = PolynomialApp(new_root)
    return app