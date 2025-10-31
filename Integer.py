from Natural import Natural


class Integer:
    def __init__(self, number: str):
        # Инициализация целого числа из строки
        # Обрабатываем знак: если первый символ '-', то число отрицательное
        if number[0] == '-':
            # Сохраняем цифры числа (все символы после минуса)
            self.number = list(map(int, number[1:]))
            self.sign = 1  # 1 означает отрицательное число
        else:
            # Сохраняем все цифры числа
            self.number = list(map(int, number[0:]))
            self.sign = 0  # 0 означает неотрицательное число
        
        # Особый случай: если все цифры нули, то число неотрицательное
        if all(digit == 0 for digit in self.number):
            self.sign = 0
    
    def __str__(self):
        # Строковое представление числа
        # Добавляем знак минус только для отрицательных ненулевых чисел
        if self.sign == 1 and not all(digit == 0 for digit in self.number):
            sign_prefix = '-'
        else:
            sign_prefix = ''
        # Объединяем цифры в строку и добавляем знак
        number_str = ''.join(map(str, self.number))
        return sign_prefix + number_str
    
    def ABS_Z_N(self):
        # Возвращает модуль числа как натуральное число
        # Просто преобразуем цифры в натуральное число без учета знака
        return Natural(''.join(map(str, self.number)))
    
    def POZ_Z_D(self):
        # Определяет знак числа:
        # 0 - если число равно нулю
        # 1 - если число отрицательное
        # 2 - если число положительное
        if all(digit == 0 for digit in self.number):
            return 0
        elif self.sign == 1:
            return 1
        else:
            return 2
    
    def MUL_ZM_Z(self):
        # Умножение числа на -1 (изменение знака)
        # Ноль остается нулем при любом изменении знака
        if all(digit == 0 for digit in self.number):
            return Integer('0')
        # Создаем копию числа и меняем знак на противоположный
        result = Integer(str(self))
        result.sign = 1 - result.sign
        return result
    
    @staticmethod
    def TRANS_N_Z(number: Natural):
        # Статический метод преобразования натурального числа в целое
        # Натуральное число всегда преобразуется в неотрицательное целое
        result = Integer(str(number))
        return result
    
    def TRANS_Z_N(self):
        # Преобразование целого числа в натуральное
        # Можно преобразовывать только неотрицательные числа
        if self.sign == 1:
            raise ValueError("Отрицательное число нельзя преобразовать в натуральное")
        return Natural(''.join(map(str, self.number)))
    
    def ADD_ZZ_Z(self, per):
        # Сложение двух целых чисел
        # Определяем знаки обоих чисел
        sign1 = self.POZ_Z_D()
        sign2 = per.POZ_Z_D()
        
        # Если одно из чисел равно нулю, возвращаем другое
        if sign1 == 0:
            return per
        if sign2 == 0:
            return self
            
        # Случай: оба числа положительные
        if sign1 == 2 and sign2 == 2:
            # Складываем модули и возвращаем положительное число
            result = self.ABS_Z_N().ADD_NN_N(per.ABS_Z_N())
            return Integer.TRANS_N_Z(result)
            
        # Случай: оба числа отрицательные
        if sign1 == 1 and sign2 == 1:
            # Складываем модули и возвращаем отрицательное число
            result = self.ABS_Z_N().ADD_NN_N(per.ABS_Z_N())
            return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            
        # Случаи с разными знаками: сравниваем модули
        compare = Natural.COM_NN_D(self.ABS_Z_N(), per.ABS_Z_N())
        if compare == 0:  # Модули равны - результат ноль
            return Integer('0')
            
        # Случай: положительное + отрицательное
        if sign1 == 2 and sign2 == 1:
            if compare == 2:  # Модуль первого больше
                # Вычитаем из большего меньшее, результат положительный
                result = self.ABS_Z_N().SUB_NN_N(per.ABS_Z_N())
                return Integer.TRANS_N_Z(result)
            else:  # Модуль второго больше
                # Вычитаем из большего меньшее, результат отрицательный
                result = per.ABS_Z_N().SUB_NN_N(self.ABS_Z_N())
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
                
        # Случай: отрицательное + положительное
        if sign1 == 1 and sign2 == 2:
            if compare == 2:  # Модуль первого больше
                # Вычитаем из большего меньшее, результат отрицательный
                result = self.ABS_Z_N().SUB_NN_N(per.ABS_Z_N())
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            else:  # Модуль второго больше
                # Вычитаем из большего меньшее, результат положительный
                result = per.ABS_Z_N().SUB_NN_N(self.ABS_Z_N())
                return Integer.TRANS_N_Z(result)
    
    def SUB_ZZ_Z(self, per):
        # Вычитание целых чисел: a - b = a + (-b)
        # Если уменьшаемое равно нулю, возвращаем -b
        if self.POZ_Z_D() == 0:
            return per.MUL_ZM_Z()
        
        # Если вычитаемое равно нулю, возвращаем a
        if per.POZ_Z_D() == 0:
            return self
        
        # Получаем знаки и модули чисел
        sign1 = self.POZ_Z_D()
        sign2 = per.POZ_Z_D()
        
        abs_self = self.ABS_Z_N()
        abs_per = per.ABS_Z_N()
        
        # Случай: оба числа положительные
        if sign1 == 2 and sign2 == 2:
            compare = Natural.COM_NN_D(abs_self, abs_per)
            if compare == 2:  # Первое число больше
                result = abs_self.SUB_NN_N(abs_per)
                return Integer.TRANS_N_Z(result)
            elif compare == 1:  # Второе число больше
                result = abs_per.SUB_NN_N(abs_self)
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            else:  # Числа равны
                return Integer('0')
        
        # Случай: положительное - отрицательное = положительное + положительное
        elif sign1 == 2 and sign2 == 1:
            result = abs_self.ADD_NN_N(abs_per)
            return Integer.TRANS_N_Z(result)
        
        # Случай: отрицательное - положительное = отрицательное + отрицательное
        elif sign1 == 1 and sign2 == 2:
            result = abs_self.ADD_NN_N(abs_per)
            return Integer.TRANS_N_Z(result).MUL_ZM_Z()
        
        # Случай: отрицательное - отрицательное = -(|a| - |b|)
        elif sign1 == 1 and sign2 == 1:
            compare = Natural.COM_NN_D(abs_self, abs_per)
            if compare == 2:  # Модуль первого больше
                result = abs_self.SUB_NN_N(abs_per)
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            elif compare == 1:  # Модуль второго больше
                result = abs_per.SUB_NN_N(abs_self)
                return Integer.TRANS_N_Z(result)
            else:  # Модули равны
                return Integer('0')
    
    def MUL_ZZ_Z(self, per):
        # Умножение целых чисел
        # Если один из множителей ноль, результат ноль
        if self.POZ_Z_D() == 0 or per.POZ_Z_D() == 0:
            return Integer('0')
        
        # Перемножаем модули чисел
        abs_self = self.ABS_Z_N()
        abs_per = per.ABS_Z_N()
        result_abs = Natural.MUL_NN_N(abs_self, abs_per)
        
        # Преобразуем результат в целое число
        result = Integer.TRANS_N_Z(result_abs)
        
        # Определяем знак результата: если знаки разные, результат отрицательный
        if self.POZ_Z_D() != per.POZ_Z_D():
            result = result.MUL_ZM_Z()
        
        return result
    
        def DIV_ZZ_Z(self, per):
        # Z-9: Частное от деления целого на целое (делитель отличен от нуля)
        # Используемые функции: ABS_Z_N, POZ_Z_D, DIV_NN_N, ADD_1N_N

        # Проверка деления на ноль
        if per.POZ_Z_D() == 0:
            print("Ошибка: деление на ноль!")
            return None

        # Деление нуля на любое число дает ноль
        if self.POZ_Z_D() == 0:
            return Integer('0')

        # Получаем модули чисел
        abs_self = self.ABS_Z_N()  # ABS_Z_N
        abs_per = per.ABS_Z_N()  # ABS_Z_N

        # Определяем знаки чисел
        sign_self = self.POZ_Z_D()  # POZ_Z_D
        sign_per = per.POZ_Z_D()  # POZ_Z_D

        # Делим модули натуральных чисел
        quotient_abs = abs_self.DIV_NN_N(abs_per)  # DIV_NN_N
        result = Integer.TRANS_N_Z(quotient_abs)

        # Если знаки разные, результат отрицательный
        if sign_self != sign_per:
            result = result.MUL_ZM_Z()

        # КОРРЕКТИРОВКА: для отрицательного делимого увеличиваем результат на 1
        # чтобы остаток был неотрицательным
        if sign_self == 1:  # Если делимое отрицательное
            # Вычисляем произведение result * per
            product = result.MUL_ZZ_Z(per)

            # Если произведение НЕ равно делимому, нужно корректировать
            if str(product) != str(self):
                # Для отрицательного результата увеличиваем на 1 (делаем менее отрицательным)
                if result.POZ_Z_D() == 1:
                    result_abs = result.ABS_Z_N()
                    result_abs_plus_one = result_abs.ADD_1N_N()  # ADD_1N_N
                    result = Integer.TRANS_N_Z(result_abs_plus_one).MUL_ZM_Z()
                # Для положительного результата увеличиваем на 1
                elif result.POZ_Z_D() == 2:
                    result_abs = result.ABS_Z_N()
                    result_abs_plus_one = result_abs.ADD_1N_N()  # ADD_1N_N
                    result = Integer.TRANS_N_Z(result_abs_plus_one)
                # Для нуля делаем -1
                else:
                    result = Integer('1').MUL_ZM_Z()

        return result

        def MOD_ZZ_Z(self, per):
        # Z-10: Остаток от деления целого на целое (делитель отличен от нуля)
        # Используемые функции: DIV_ZZ_Z, MUL_ZZ_Z, SUB_ZZ_Z, MUL_ZM_Z

        # Проверка деления на ноль
        if per.POZ_Z_D() == 0:
            print("Ошибка: остаток от деления на ноль!")
            return None

        # Остаток от деления нуля на любое число равен нулю
        if self.POZ_Z_D() == 0:
            return Integer('0')

        # Вычисляем частное (целая часть от деления)
        quotient = self.DIV_ZZ_Z(per)

        # Проверяем, что деление было успешным
        if quotient is None:
            return None

        # Вычисляем произведение частного и делителя
        product = quotient.MUL_ZZ_Z(per)

        # Вычисляем остаток: делимое - произведение
        remainder = self.SUB_ZZ_Z(product)

        return remainder


def tests_for_integers():
    # Создаем тестовые данные
    int1 = Integer("123")
    int2 = Integer("-45")
    int3 = Integer("0")
    int4 = Integer("-678")
    int5 = Integer("999")
    int6 = Integer("-1")
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА INTEGER")
    print("=" * 60)

    # Тестирование модуля числа
    print("\n1. ТЕСТИРОВАНИЕ МОДУЛЯ (ABS_Z_N):")
    print(f"   |{int1}| = {int1.ABS_Z_N()}")
    print(f"   |{int2}| = {int2.ABS_Z_N()}")
    print(f"   |{int3}| = {int3.ABS_Z_N()}")
    print(f"   |{int4}| = {int4.ABS_Z_N()}")

    # Тестирование определения знака
    print("\n2. ТЕСТИРОВАНИЕ ОПРЕДЕЛЕНИЯ ЗНАКА (POZ_Z_D):")
    print(f"   Знак числа {int1}: {int1.POZ_Z_D()}")
    print(f"   Знак числа {int2}: {int2.POZ_Z_D()}")
    print(f"   Знак числа {int3}: {int3.POZ_Z_D()}")
    print(f"   Знак числа {int6}: {int6.POZ_Z_D()}")

    # Тестирование умножения на -1
    print("\n3. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ НА -1 (MUL_ZM_Z):")
    print(f"   -({int1}) = {int1.MUL_ZM_Z()}")
    print(f"   -({int2}) = {int2.MUL_ZM_Z()}")
    print(f"   -({int3}) = {int3.MUL_ZM_Z()}")
    print(f"   -({int5}) = {int5.MUL_ZM_Z()}")

    # Тестирование преобразований между натуральными и целыми числами
    print("\n4. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ NATURAL -> INTEGER (TRANS_N_Z):")
    nat1 = Natural("123")
    nat2 = Natural("0")
    nat3 = Natural("789")
    
    int_from_nat1 = Integer.TRANS_N_Z(nat1)
    int_from_nat2 = Integer.TRANS_N_Z(nat2)
    int_from_nat3 = Integer.TRANS_N_Z(nat3)
    
    print(f"   Natural('123') -> Integer: {int_from_nat1}")
    print(f"   Natural('0') -> Integer: {int_from_nat2}")
    print(f"   Natural('789') -> Integer: {int_from_nat3}")

    print("\n5. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ INTEGER -> NATURAL (TRANS_Z_N):")
    print(f"   Integer('123') -> Natural: {int1.TRANS_Z_N()}")
    print(f"   Integer('0') -> Natural: {int3.TRANS_Z_N()}")
    
    # Проверка обработки ошибки при преобразовании отрицательного числа
    try:
        int2.TRANS_Z_N()
        print(f"   Integer('-45') -> Natural: ОШИБКА - исключение не сработало!")
    except ValueError as e:
        print(f"   Integer('-45') -> Natural: {e}")

    # Тестирование строкового представления
    print("\n6. ТЕСТИРОВАНИЕ СТРОКОВОГО ПРЕДСТАВЛЕНИЯ:")
    print(f"   Integer('123'): '{int1}'")
    print(f"   Integer('-45'): '{int2}'")
    print(f"   Integer('0'): '{int3}'")
    print(f"   Integer('-678'): '{int4}'")
    print(f"   Integer('999'): '{int5}'")

    # Тестирование сложения
    print("\n7. ТЕСТИРОВАНИЕ СЛОЖЕНИЯ (ADD_ZZ_Z):")
    print(f"   {int1} + {int5} = {int1.ADD_ZZ_Z(int5)}")
    print(f"   {int2} + {int4} = {int2.ADD_ZZ_Z(int4)}")
    print(f"   {int1} + {int2} = {int1.ADD_ZZ_Z(int2)}")
    print(f"   {int2} + {int1} = {int2.ADD_ZZ_Z(int1)}")
    print(f"   {int1} + {int3} = {int1.ADD_ZZ_Z(int3)}")
    print(f"   {int3} + {int2} = {int3.ADD_ZZ_Z(int2)}")
    int7 = Integer("45")
    print(f"   {int2} + {int7} = {int2.ADD_ZZ_Z(int7)}")

    # Тестирование вычитания
    print("\n8. ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ (SUB_ZZ_Z):")
    print(f"   {int1} - {int5} = {int1.SUB_ZZ_Z(int5)}")
    print(f"   {int2} - {int4} = {int2.SUB_ZZ_Z(int4)}")
    print(f"   {int1} - {int2} = {int1.SUB_ZZ_Z(int2)}")
    print(f"   {int2} - {int1} = {int2.SUB_ZZ_Z(int1)}")
    print(f"   {int1} - {int3} = {int1.SUB_ZZ_Z(int3)}")
    print(f"   {int3} - {int2} = {int3.SUB_ZZ_Z(int2)}")
    print(f"   {int1} - {int1} = {int1.SUB_ZZ_Z(int1)}")

    # Тестирование умножения
    print("\n9. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ (MUL_ZZ_Z):")
    print(f"   {int1} * {int5} = {int1.MUL_ZZ_Z(int5)}")
    print(f"   {int2} * {int4} = {int2.MUL_ZZ_Z(int4)}")
    print(f"   {int1} * {int2} = {int1.MUL_ZZ_Z(int2)}")
    print(f"   {int1} * {int3} = {int1.MUL_ZZ_Z(int3)}")
    print(f"   {int3} * {int2} = {int3.MUL_ZZ_Z(int2)}")
    int8 = Integer("1")
    print(f"   {int1} * {int8} = {int1.MUL_ZZ_Z(int8)}")
    print(f"   {int1} * {int6} = {int1.MUL_ZZ_Z(int6)}")

    # Тестирование целочисленного деления
    print("\n10. ТЕСТИРОВАНИЕ ЦЕЛОЧИСЛЕННОГО ДЕЛЕНИЯ (DIV_ZZ_Z):")
    int9 = Integer("25")
    int10 = Integer("5")
    print(f"   {int9} / {int10} = {int9.DIV_ZZ_Z(int10)}")
    int11 = Integer("-25")
    int12 = Integer("-5")
    print(f"   {int11} / {int12} = {int11.DIV_ZZ_Z(int12)}")
    print(f"   {int9} / {int12} = {int9.DIV_ZZ_Z(int12)}")
    print(f"   {int11} / {int10} = {int11.DIV_ZZ_Z(int10)}")
    print(f"   {int1} / {int8} = {int1.DIV_ZZ_Z(int8)}")
    print(f"   {int1} / {int6} = {int1.DIV_ZZ_Z(int6)}")
    int13 = Integer("7")
    int14 = Integer("3")
    print(f"   {int13} / {int14} = {int13.DIV_ZZ_Z(int14)}")
    int15 = Integer("-7")
    print(f"   {int15} / {int14} = {int15.DIV_ZZ_Z(int14)}")
    print(f"   {int13} / {int14.MUL_ZM_Z()} = {int13.DIV_ZZ_Z(int14.MUL_ZM_Z())}")
    print(f"   {int3} / {int1} = {int3.DIV_ZZ_Z(int1)}")
    # Проверка деления на ноль
    try:
        int1.DIV_ZZ_Z(int3)
        print(f"   {int1} / {int3} = ОШИБКА - исключение не сработало!")
    except ZeroDivisionError as e:
        print(f"   {int1} / {int3} = {e}")

    # Тестирование остатка от деления
    print("\n11. ТЕСТИРОВАНИЕ ОСТАТКА ОТ ДЕЛЕНИЯ (MOD_ZZ_Z):")
    print(f"   {int13} % {int14} = {int13.MOD_ZZ_Z(int14)}")
    print(f"   {int15} % {int14} = {int15.MOD_ZZ_Z(int14)}")
    print(f"   {int13} % {int14.MUL_ZM_Z()} = {int13.MOD_ZZ_Z(int14.MUL_ZM_Z())}")
    print(f"   {int15} % {int14.MUL_ZM_Z()} = {int15.MOD_ZZ_Z(int14.MUL_ZM_Z())}")
    print(f"   {int1} % {int8} = {int1.MOD_ZZ_Z(int8)}")
    print(f"   {int1} % {int6} = {int1.MOD_ZZ_Z(int6)}")
    print(f"   {int3} % {int1} = {int3.MOD_ZZ_Z(int1)}")
    # Проверка деления на ноль
    try:
        int1.MOD_ZZ_Z(int3)
        print(f"   {int1} % {int3} = ОШИБКА - исключение не сработало!")
    except ZeroDivisionError as e:
        print(f"   {int1} % {int3} = {e}")


tests_for_integers()
