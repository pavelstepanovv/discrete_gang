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
        self.root.geometry("550x650")  # Увеличил размер окна
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 0.97)

        self.method_var = tk.StringVar(value="Сложение многочленов")

        # Заголовок
        title_label = tk.Label(root, text="😎 Калькулятор многочленов", 
                              bg=self.bg_color, fg=self.text_color, font=("Arial", 16, "bold"))
        title_label.pack(pady=15)

        # Подзаголовок
        subtitle_label = tk.Label(root, text="Ба-на-на! Математика с миньонами! 🍌", 
                                 bg=self.bg_color, fg=self.backlight, font=("Arial", 11, "italic"))
        subtitle_label.pack(pady=5)

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

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=15)

        tk.Label(method_frame, text="Выберите задание:", bg=self.bg_color, fg=self.text_color, 
                font=("Arial", 11)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.window_color, fg="white",
                               activebackground=self.hover_color, activeforeground="white",
                               font=("Arial", 10), width=22, relief=tk.RAISED, bd=2)
        self.method_menu["menu"].config(bg=self.window_color, fg="white")
        self.method_menu.pack(side=tk.LEFT, padx=10)

        # Контейнер для полей ввода
        self.input_frame = tk.Frame(root, bg=self.bg_color)
        self.input_frame.pack(pady=15)

        # Первый многочлен (всегда видно)
        self.first_poly_label = tk.Label(self.input_frame, text="😎 Первый многочлен:", bg=self.bg_color, 
                                        fg=self.text_color, font=("Arial", 10, "bold"))
        self.first_poly_label.grid(row=0, column=0, sticky="w", pady=5)
        
        self.first_poly_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=30, 
                                       font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.first_poly_entry.grid(row=1, column=0, pady=5)

        # Второй многочлен (изначально скрыто)
        self.second_poly_label = tk.Label(self.input_frame, text="🤓 Второй многочлен:", bg=self.bg_color, 
                                         fg=self.text_color, font=("Arial", 10))
        self.second_poly_label.grid(row=0, column=1, sticky="w", pady=5, padx=(20, 0))
        
        self.second_poly_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=30, 
                                        font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.second_poly_entry.grid(row=1, column=1, pady=5, padx=(20, 0))

        # Рациональное число (специальное поле)
        self.rational_label = tk.Label(self.input_frame, text="🍌 Рациональное число:", bg=self.bg_color, 
                                      fg=self.text_color, font=("Arial", 10))
        self.rational_label.grid(row=2, column=0, sticky="w", pady=(15, 5))
        
        self.rational_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=25, 
                                     font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.rational_entry.grid(row=3, column=0, pady=5)

        # Степень k (специальное поле)
        self.k_label = tk.Label(self.input_frame, text="👓 Степень k:", bg=self.bg_color, 
                               fg=self.text_color, font=("Arial", 10))
        self.k_label.grid(row=2, column=1, sticky="w", pady=(15, 5), padx=(20, 0))
        
        self.k_entry = tk.Entry(self.input_frame, bg="white", fg="black", width=15, 
                              font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.k_entry.grid(row=3, column=1, pady=5, padx=(20, 0))

        # Подсказка для формата ввода
        hint_label = tk.Label(self.input_frame, text="Формат: коэффициенты через пробел (например: 1 2 -3 4)", 
                             bg=self.bg_color, fg=self.backlight, font=("Arial", 9, "italic"))
        hint_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

        # Изначально скрываем ненужные поля
        self.hide_all_extra_fields()

        # Метка для результата с увеличенной высотой
        result_frame = tk.Frame(root, bg=self.window_color, bd=3, relief=tk.GROOVE)
        result_frame.pack(pady=20, padx=25, fill=tk.X)
        
        result_title = tk.Label(result_frame, text="🎯 Результат:", bg=self.window_color, fg="white", 
                               font=("Arial", 11, "bold"))
        result_title.pack(pady=(8, 0))
        
        self.result_label = tk.Label(result_frame, text="Банана! Здесь появится результат...", 
                                    bg="white", fg="black", font=("Arial", 11),  # Уменьшил шрифт
                                    wraplength=500, justify=tk.CENTER, height=6)  # Увеличил высоту и ширину
        self.result_label.pack(pady=8, padx=8, fill=tk.BOTH, expand=True)

        # Кнопка выполнения
        self.calculate_button = tk.Button(root, text="🚀 Выполнить!", command=self.calculate, 
                                         bg=self.button_color, fg="white", font=("Arial", 12, "bold"), 
                                         height=1, width=15, relief=tk.RAISED, bd=3,
                                         cursor="hand2")
        self.calculate_button.pack(pady=15)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))

        # Футер
        footer_label = tk.Label(root, text="Сделано с 💙 для миньонов-математиков", 
                               bg=self.bg_color, fg=self.text_color, font=("Arial", 9))
        footer_label.pack(pady=10)

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
        
        # Разделяем коэффициенты по пробелам
        coefficients = poly_str.strip().split()
        if not coefficients:
            raise ValueError("Нет коэффициентов")
        
        # Проверяем, что все коэффициенты - числа
        for coeff in coefficients:
            if '/' in coeff:
                # Рациональное число формата a/b
                parts = coeff.split('/')
                if len(parts) != 2:
                    raise ValueError(f"Неверный формат рационального числа: {coeff}")
                num, den = parts
                if not num.lstrip('-').isdigit() or not den.isdigit():
                    raise ValueError(f"Неверный формат рационального числа: {coeff}")
            else:
                # Целое число
                if not coeff.lstrip('-').isdigit():
                    raise ValueError(f"Нечисловой коэффициент: {coeff}")
        
        return Polynomial(poly_str)

    def get_Rational(self, rational_str):
        """Преобразует строку в рациональное число с проверкой"""
        if not rational_str:
            raise ValueError("Пустая строка")
        
        if '/' in rational_str:
            parts = rational_str.split('/')
            if len(parts) != 2:
                raise ValueError("Неверный формат рационального числа")
            num_str, den_str = parts
            if not num_str.lstrip('-').isdigit() or not den_str.isdigit():
                raise ValueError("Неверный формат рационального числа")
        else:
            if not rational_str.lstrip('-').isdigit():
                raise ValueError("Не числовое значение")
        
        from Rational import Rational
        return Rational(rational_str)

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
                messagebox.showerror("Ошибка", f"😠 Неверный формат: {str(e)}")
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
                    messagebox.showerror("Ошибка", f"😠 Неверный формат: {str(e)}")
                return

            if method_name == "Сложение многочленов":
                result = first_poly.ADD_PP_P(second_poly)
                # Более компактное отображение
                self.result_label.config(text=f"🎉 ({first_poly}) + ({second_poly}) = {result}")

            elif method_name == "Вычитание многочленов":
                result = first_poly.SUB_PP_P(second_poly)
                self.result_label.config(text=f"🎉 ({first_poly}) - ({second_poly}) = {result}")

            elif method_name == "Умножение многочленов":
                result = first_poly.MUL_PP_P(second_poly)
                self.result_label.config(text=f"🎉 ({first_poly}) × ({second_poly}) = {result}")

            elif method_name == "Деление многочленов":
                try:
                    result = first_poly.DIV_PP_P(second_poly)
                    self.result_label.config(text=f"🎉 ({first_poly}) ÷ ({second_poly}) = {result}")
                except ZeroDivisionError:
                    messagebox.showerror("Ошибка", "😠 Ой-ой! Деление на нулевой многочлен!")
                    return

            elif method_name == "Остаток от деления":
                try:
                    result = first_poly.MOD_PP_P(second_poly)
                    self.result_label.config(text=f"🎉 ({first_poly}) mod ({second_poly}) = {result}")
                except ZeroDivisionError:
                    messagebox.showerror("Ошибка", "😠 Ой-ой! Деление на нулевой многочлен!")
                    return

            elif method_name == "НОД многочленов":
                result = first_poly.GCF_PP_P(second_poly)
                self.result_label.config(text=f"🎉 НОД(({first_poly}), ({second_poly})) = {result}")

        elif method_name == "Умножение на рациональное число":
            rational_str = self.rational_entry.get().strip()
            try:
                rational_num = self.get_Rational(rational_str)
                result = first_poly.MUL_PQ_P(rational_num)
                self.result_label.config(text=f"🎉 ({first_poly}) × {rational_num} = {result}")
            except ValueError as e:
                if not rational_str:
                    messagebox.showerror("Ошибка", "🍌 Банана! Введите рациональное число")
                else:
                    messagebox.showerror("Ошибка", f"🍌 Неверный формат: {str(e)}")
                return

        elif method_name == "Умножение на x^k":
            k_str = self.k_entry.get().strip()
            if not k_str or not k_str.isdigit():
                messagebox.showerror("Ошибка", "👓 Степень k должна быть натуральным числом")
                return
            k = int(k_str)
            try:
                result = first_poly.MUL_Pxk_P(k)
                self.result_label.config(text=f"🎉 ({first_poly}) × x^{k} = {result}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"👓 Ошибка: {str(e)}")
                return

        else:
            if method_name == "Старший коэффициент":
                result = first_poly.LED_P_Q()
                self.result_label.config(text=f"🎉 Старший коэффициент ({first_poly}) = {result}")

            elif method_name == "Степень многочлена":
                result = first_poly.DEG_P_N()
                self.result_label.config(text=f"🎉 Степень ({first_poly}) = {result}")

            elif method_name == "НОК знаменателей и НОД числителей":
                result = first_poly.FAC_P_Q()
                self.result_label.config(text=f"🎉 НОК/НОД ({first_poly}) = {result}")

            elif method_name == "Производная многочлена":
                result = first_poly.DER_P_P()
                self.result_label.config(text=f"🎉 Производная ({first_poly}) = {result}")

            elif method_name == "Кратные корни в простые":
                result = first_poly.NMR_P_P()
                self.result_label.config(text=f"🎉 Упрощенный ({first_poly}) = {result}")


def create_PolynomialApp(root):
    new_root = tk.Toplevel(root)
    app = PolynomialApp(new_root)
    return app