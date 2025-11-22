import tkinter as tk
from tkinter import messagebox
from Natural import Natural
import argparse


class NaturalApp:
    def __init__(self, root):
        # Единая цветовая схема с персиковым фоном
        self.bg_color = "#FFE4C9"  # Нежный персиковый фон
        self.window_color = "#FFF5E6"  # Светло-персиковый для окон
        self.text_color = "#8B4513"  # Коричневый (контрастный с фоном)
        self.backlight = "#D2691E"  # Шоколадный для выделения
        self.accent_color = "#FF6B35"  # Оранжево-красный для акцентов
        self.hover_color = "#FFA500"  # Оранжевый при наведении
        self.button_color = self.accent_color

        self.root = root
        self.root.title("🐾 Калькулятор натуральных чисел")
        self.root.geometry("450x550")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 0.97)

        self.method_var = tk.StringVar(value="Сложение двух чисел")

        # Заголовок
        title_label = tk.Label(root, text="🐱 Калькулятор натуральных чисел", 
                              bg=self.bg_color, fg=self.text_color, font=("Arial", 16, "bold"))
        title_label.pack(pady=15)

        # Подзаголовок
        subtitle_label = tk.Label(root, text="Мяу-математика для умных котиков! ✨", 
                                 bg=self.bg_color, fg=self.backlight, font=("Arial", 11, "italic"))
        subtitle_label.pack(pady=5)

        # Выбор метода
        methods = [
            "Сравнение чисел",
            "Проверка на ноль", 
            "Прибавление единицы",
            "Сложение двух чисел",
            "Вычитание двух чисел",
            "Умножение на цифру",
            "Умножение на 10ⁿ",
            "Умножение двух чисел",
            "Вычитание умноженного на цифру",
            "DIV_NN_Dk",
            "Деление целочисленное",
            "Деление с остатком",
            "НОД",
            "НОК"
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=15)

        tk.Label(method_frame, text="Выберите операцию:", bg=self.bg_color, fg=self.text_color, 
                font=("Arial", 11)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.window_color, fg=self.text_color, 
                               activebackground=self.hover_color, activeforeground=self.text_color,
                               font=("Arial", 10), width=18, relief=tk.RAISED, bd=2)
        self.method_menu["menu"].config(bg=self.window_color, fg=self.text_color)
        self.method_menu.pack(side=tk.LEFT, padx=10)

        # Контейнер для полей ввода
        self.input_frame = tk.Frame(root, bg=self.bg_color)
        self.input_frame.pack(pady=15)

        # Первое число (всегда видно)
        self.first_number_label = tk.Label(self.input_frame, text="🐭 Первое число:", bg=self.bg_color, 
                                          fg=self.backlight, font=("Arial", 10, "bold"))
        self.first_number_label.grid(row=0, column=0, sticky="w", pady=5)
        
        self.first_number_entry = tk.Entry(self.input_frame, bg=self.window_color, fg=self.text_color, width=25, 
                                          font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.first_number_entry.grid(row=1, column=0, pady=5)

        # Второе число (изначально скрыто)
        self.second_number_label = tk.Label(self.input_frame, text="🧶 Второе число:", bg=self.bg_color, 
                                           fg=self.text_color, font=("Arial", 10))
        self.second_number_label.grid(row=0, column=1, sticky="w", pady=5, padx=(20, 0))
        
        self.second_number_entry = tk.Entry(self.input_frame, bg=self.window_color, fg=self.text_color, width=25, 
                                           font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.second_number_entry.grid(row=1, column=1, pady=5, padx=(20, 0))
        
        # Цифра (изначально скрыто)
        self.digit_label = tk.Label(self.input_frame, text="🔢 Цифра:", bg=self.bg_color, 
                                   fg=self.text_color, font=("Arial", 10))
        self.digit_label.grid(row=2, column=0, sticky="w", pady=(15, 5))
        
        self.digit_entry = tk.Entry(self.input_frame, bg=self.window_color, fg=self.text_color, width=15, 
                                   font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.digit_entry.grid(row=3, column=0, pady=5)

        # Степень k (специально для DIV_NN_Dk)
        self.k_label = tk.Label(self.input_frame, text="📏 Степень k:", bg=self.bg_color, 
                               fg=self.text_color, font=("Arial", 10))
        self.k_label.grid(row=2, column=1, sticky="w", pady=(15, 5), padx=(20, 0))
        
        self.k_entry = tk.Entry(self.input_frame, bg=self.window_color, fg=self.text_color, width=15, 
                               font=("Arial", 11), relief=tk.SUNKEN, bd=2)
        self.k_entry.grid(row=3, column=1, pady=5, padx=(20, 0))

        # Изначально скрываем ненужные поля
        self.hide_all_extra_fields()

        # Окно результата (заменил Label на Text с прокруткой колесиком)
        result_frame = tk.Frame(root, bg=self.backlight, bd=3, relief=tk.GROOVE)
        result_frame.pack(pady=10, padx=25, fill=tk.BOTH, expand=False)

        result_title = tk.Label(result_frame, text="🎯 Результат:", bg=self.backlight, fg="white", 
                               font=("Arial", 11, "bold"))
        result_title.pack(pady=(8, 0))

        text_container = tk.Frame(result_frame, bg=self.backlight)
        text_container.pack(pady=8, padx=8, fill=tk.BOTH, expand=True)

        self.result_text = tk.Text(text_container, bg=self.window_color, fg=self.text_color, font=("Arial", 12),
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

        def set_result(text, fg=self.text_color):
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, text)
            self.result_text.config(fg=fg)
            self.result_text.config(state=tk.DISABLED)

        self.set_result = set_result

        # Кнопка выполнения с кошачьей темой
        self.calculate_button = tk.Button(root, text="🐾 Вычислить!", command=self.calculate, 
                                         bg=self.button_color, fg="white", font=("Arial", 12, "bold"), 
                                         height=1, width=15, relief=tk.RAISED, bd=3,
                                         cursor="hand2")
        self.calculate_button.pack(pady=15)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))

        # Футер с кошачьей темой
        footer_label = tk.Label(root, text="Сделано с 💖 для математических котиков", 
                               bg=self.bg_color, fg=self.text_color, font=("Arial", 9))
        footer_label.pack(pady=10)

    def hide_all_extra_fields(self):
        """Скрывает все дополнительные поля ввода"""
        self.second_number_label.grid_remove()
        self.second_number_entry.grid_remove()
        self.digit_label.grid_remove()
        self.digit_entry.grid_remove()
        self.k_label.grid_remove()
        self.k_entry.grid_remove()

    def on_option_change(self, value):
        method_name = self.method_var.get()
        
        # Сбрасываем все поля
        self.hide_all_extra_fields()
        self.first_number_label.config(fg=self.backlight, text="🐭 Первое число:")
        
        # Показываем только нужные поля с соответствующими смайликами
        if method_name in ["Сравнение чисел", "Сложение двух чисел", "Вычитание двух чисел",
                          "Умножение двух чисел", "Деление целочисленное", "Деление с остатком", 
                          "НОД", "НОК"]:
            self.second_number_label.config(fg=self.backlight, text="🧶 Второе число:")
            self.second_number_label.grid()
            self.second_number_entry.grid()
            
        elif method_name in ["Умножение на цифру", "Умножение на 10ⁿ"]:
            self.digit_label.config(fg=self.backlight, text="🔢 Цифра:")
            self.digit_label.grid()
            self.digit_entry.grid()
            
        elif method_name == "Вычитание умноженного на цифру":
            self.second_number_label.config(fg=self.backlight, text="🧶 Второе число:")
            self.second_number_label.grid()
            self.second_number_entry.grid()
            self.digit_label.config(fg=self.backlight, text="🔢 Цифра:")
            self.digit_label.grid()
            self.digit_entry.grid()
            
        elif method_name == "DIV_NN_Dk":
            self.second_number_label.config(fg=self.backlight, text="🧶 Второе число:")
            self.second_number_label.grid()
            self.second_number_entry.grid()
            self.k_label.config(fg=self.backlight, text="📏 Степень k:")
            self.k_label.grid()
            self.k_entry.grid()

        # Для методов с одним числом скрываем все дополнительные поля
        elif method_name in ["Проверка на ноль", "Прибавление единицы"]:
            pass  # Только первое число

    def to_superscript(self, n):
        superscripts = {
            '0': '⁰', '1': '¹', '2': '²', '3': '³',
            '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷',
            '8': '⁸', '9': '⁹'
        }
        return ''.join(superscripts[digit] for digit in str(n))

    def get_Natural(self, number_str):
        """Преобразует строку в Natural с проверкой"""
        if not number_str:
            raise ValueError("Пустая строка")
        if not all(c.isdigit() for c in number_str):
            raise ValueError("Не натуральное число")
        return Natural(number_str)

    def calculate(self):
        self.set_result('Вычисляю... 🐱', fg=self.text_color)
        method_name = self.method_var.get()
        first_number_str = self.first_number_entry.get().strip()

        try:
            first_number = self.get_Natural(first_number_str)
        except ValueError:
            if not first_number_str:
                messagebox.showerror("Ошибка", "😿 Пожалуйста, введите первое число")
            else:
                messagebox.showerror("Ошибка", "😾 Первое число должно содержать только цифры")
            return

        if method_name in ["Сравнение чисел", "Сложение двух чисел", "Вычитание двух чисел",
                          "Умножение двух чисел", "Вычитание умноженного на цифру", "DIV_NN_Dk",
                          "Деление целочисленное", "Деление с остатком", "НОД", "НОК"]:

            second_number_str = self.second_number_entry.get().strip()

            try:
                second_number = self.get_Natural(second_number_str)
            except ValueError:
                if not second_number_str:
                    messagebox.showerror("Ошибка", "😿 Пожалуйста, введите второе число")
                else:
                    messagebox.showerror("Ошибка", "😾 Второе число должно содержать только цифры")
                return

            if method_name == "Сравнение чисел":
                comparison_result = first_number.COM_NN_D(second_number)
                comparison_texts = {
                    2: f"🐱 {first_number} > {second_number}",
                    1: f"🐭 {first_number} < {second_number}", 
                    0: f"💖 {first_number} = {second_number}"
                }
                self.set_result(comparison_texts[comparison_result])

            elif method_name == "Сложение двух чисел":
                result = first_number.ADD_NN_N(second_number)
                self.set_result(f"🎀 {first_number} + {second_number} = {result}")

            elif method_name == "Вычитание двух чисел":
                try:
                    result = first_number.SUB_NN_N(second_number)
                    self.set_result(f"🎀 {first_number} - {second_number} = {result}")
                except ValueError:
                    messagebox.showerror("Ошибка", "😿 Результат вычитания должен быть натуральным числом")
                    return

            elif method_name == "Умножение двух чисел":
                result = first_number.MUL_NN_N(second_number)
                self.set_result(f"🎀 {first_number} × {second_number} = {result}")

            elif method_name == "Вычитание умноженного на цифру":
                digit_str = self.digit_entry.get().strip()
                if not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "😾 Цифра должна быть от 0 до 9")
                    return
                digit = int(digit_str)
                try:
                    result = first_number.SUB_NDN_N(second_number, digit)
                    self.set_result(f"🎀 {first_number} - ({second_number} × {digit}) = {result}")
                except ValueError:
                    messagebox.showerror("Ошибка", "😿 Результат должен быть натуральным числом")
                    return

            elif method_name == "DIV_NN_Dk":
                k_str = self.k_entry.get().strip()
                if not k_str or not all(c.isdigit() for c in k_str):
                    messagebox.showerror("Ошибка", "😾 Степень k должна быть натуральным числом")
                    return
                k = int(k_str)
                try:
                    result = first_number.DIV_NN_Dk(second_number, k)
                    self.set_result(f"🔢 Цифра частного: {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"😿 {str(e)}")
                    return

            elif method_name == "Деление целочисленное":
                try:
                    result = first_number.DIV_NN_N(second_number)
                    self.set_result(f"🎀 {first_number} ÷ {second_number} = {result}")
                except:
                    messagebox.showerror("Ошибка", "😾 Деление на ноль невозможно")
                    return

            elif method_name == "Деление с остатком":
                try:
                    result = first_number.MOD_NN_N(second_number)
                    self.set_result(f"🎀 {first_number} mod {second_number} = {result}")
                except:
                    messagebox.showerror("Ошибка", "😾 Деление на ноль невозможно")
                    return

            elif method_name == "НОД":
                if str(first_number) == "0" and str(second_number) == "0":
                    messagebox.showerror("Ошибка", "😾 НОД(0;0) неопределён!")
                    return
                result = first_number.GCF_NN_N(second_number)
                self.set_result(f"💝 НОД({first_number}, {second_number}) = {result}")

            elif method_name == "НОК":
                if str(first_number) == "0" or str(second_number) == "0":
                    messagebox.showerror("Ошибка", f"😾 НОК({first_number};{second_number}) неопределён!")
                    return
                result = first_number.LCM_NN_N(second_number)
                self.set_result(f"💝 НОК({first_number}, {second_number}) = {result}")

        else:
            if method_name == "Прибавление единицы":
                result = first_number.ADD_1N_N()
                self.set_result(f"🎀 {first_number} + 1 = {result}")

            elif method_name == "Проверка на ноль":
                is_non_zero = first_number.NZER_N_B()
                if is_non_zero == 'да':
                    self.set_result(f"✅ {first_number} ≠ 0")
                else:
                    self.set_result(f"❌ {first_number} = 0")

            elif method_name == "Умножение на цифру":
                digit_str = self.digit_entry.get().strip()
                if not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "😾 Цифра должна быть от 0 до 9")
                    return
                digit = int(digit_str)
                try:
                    result = first_number.MUL_ND_N(digit)
                    self.set_result(f"🎀 {first_number} × {digit} = {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"😿 {str(e)}")
                    return

            elif method_name == "Умножение на 10ⁿ":
                digit_str = self.digit_entry.get().strip()
                try:
                    self.get_Natural(digit_str)
                    digit = int(digit_str)
                except ValueError:
                    messagebox.showerror("Ошибка", "😾 Степень должна быть натуральным числом")
                    return
                try:
                    result = first_number.MUL_Nk_N(digit)
                    self.set_result(f"🎀 {first_number} × 10{self.to_superscript(digit)} = {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"😿 {str(e)}")
                    return


def create_NaturalApp(root):
    new_root = tk.Toplevel(root)
    app = NaturalApp(new_root)
    return app