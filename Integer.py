from Natural import Natural


class Integer:
    def __init__(self, number: str):
        # Инициализация целого числа из строки
        # Обрабатываем знак числа и его цифровое представление
        if number[0] == '-':
            # Если число начинается с '-', оно отрицательное
            # Сохраняем цифры (все символы кроме первого) как список целых чисел
            self.number = list(map(int, number[1:]))
            # Устанавливаем флаг знака: 1 для отрицательных чисел
            self.sign = 1
        else:
            # Если знака нет или число положительное, сохраняем все цифры
            self.number = list(map(int, number[0:]))
            # Устанавливаем флаг знака: 0 для положительных чисел
            self.sign = 0
        # Специальная обработка нуля: ноль всегда считается положительным
        if all(digit == 0 for digit in self.number):
            self.sign = 0
    
    def __str__(self):
        # Строковое представление числа для вывода
        # Определяем, нужно ли добавлять знак минус
        if self.sign == 1 and not all(digit == 0 for digit in self.number):
            sign_prefix = '-'  # Добавляем минус для отрицательных ненулевых чисел
        else:
            sign_prefix = ''   # Для положительных чисел и нуля знак не добавляем
        # Преобразуем список цифр в строку
        number_str = ''.join(map(str, self.number))
        return sign_prefix + number_str
    
    def ABS_Z_N(self):
        # Возвращает модуль числа как натуральное число
        # Преобразуем цифры в строку и создаем натуральное число
        return Natural(''.join(map(str, self.number)))
    
    def POZ_Z_D(self):
        # Определяет знак числа
        # 0 - если число равно нулю
        # 1 - если число отрицательное  
        # 2 - если число положительное
        if all(digit == 0 for digit in self.number):
            return 0  # Все цифры нули - число равно нулю
        elif self.sign == 1:
            return 1  # Установлен флаг отрицательного числа
        else:
            return 2  # Положительное число
    
    def MUL_ZM_Z(self):
        # Умножение числа на -1 (смена знака)
        # Ноль при смене знака остается нулем
        if all(digit == 0 for digit in self.number):
            return Integer('0')
        # Создаем копию текущего числа
        result = Integer(str(self))
        # Меняем знак: 0 становится 1, 1 становится 0
        result.sign = 1 - result.sign
        return result
    
    @staticmethod
    def TRANS_N_Z(number: Natural):
        # Статический метод для преобразования натурального числа в целое
        # Просто создаем целое число из строкового представления натурального
        result = Integer(str(number))
        return result
    
    def TRANS_Z_N(self):
        # Преобразование целого числа в натуральное
        # Можно преобразовывать только неотрицательные числа
        if self.sign == 1:
            raise ValueError("Отрицательное число нельзя преобразовать в натуральное")
        # Преобразуем цифры в строку и создаем натуральное число
        return Natural(''.join(map(str, self.number)))
    
    def ADD_ZZ_Z(self, per):
        # Сложение двух целых чисел
        # Определяем знаки обоих чисел
        sign1 = self.POZ_Z_D()
        sign2 = per.POZ_Z_D()
        
        # Обработка особых случаев с нулями
        if sign1 == 0:  # Если первое число ноль, возвращаем второе
            return per
        if sign2 == 0:  # Если второе число ноль, возвращаем первое
            return self
            
        # Оба числа положительные - складываем их модули
        if sign1 == 2 and sign2 == 2:
            result = self.ABS_Z_N().ADD_NN_N(per.ABS_Z_N())
            return Integer.TRANS_N_Z(result)
            
        # Оба числа отрицательные - складываем модули и меняем знак результата
        if sign1 == 1 and sign2 == 1:
            result = self.ABS_Z_N().ADD_NN_N(per.ABS_Z_N())
            return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            
        # Числа имеют разные знаки - выполняем вычитание модулей
        compare = Natural.COM_NN_D(self.ABS_Z_N(), per.ABS_Z_N())
        if compare == 0:  # Модули равны - результат ноль
            return Integer('0')
            
        # Первое положительное, второе отрицательное
        if sign1 == 2 and sign2 == 1:
            if compare == 2:  # Модуль первого больше модуля второго
                result = self.ABS_Z_N().SUB_NN_N(per.ABS_Z_N())
                return Integer.TRANS_N_Z(result)
            else:  # Модуль второго больше модуля первого
                result = per.ABS_Z_N().SUB_NN_N(self.ABS_Z_N())
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
                
        # Первое отрицательное, второе положительное  
        if sign1 == 1 and sign2 == 2:
            if compare == 2:  # Модуль первого больше модуля второго
                result = self.ABS_Z_N().SUB_NN_N(per.ABS_Z_N())
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            else:  # Модуль второго больше модуля первого
                result = per.ABS_Z_N().SUB_NN_N(self.ABS_Z_N())
                return Integer.TRANS_N_Z(result)
    
    def SUB_ZZ_Z(self, per):
        # Вычитание целых чисел: a - b = a + (-b)
        # Вычитание реализуется через сложение с противоположным числом
        result = self.ADD_ZZ_Z(per.MUL_ZM_Z())
        return result
    
    def MUL_ZZ_Z(self, per):
        # Умножение целых чисел
        # Проверяем, является ли одно из чисел нулем
        condition1 = all(digit == 0 for digit in self.number)
        condition2 = all(digit == 0 for digit in per.number)
        if condition1 or condition2:
            result = Integer('0')
            return result
            
        # Умножаем модули чисел
        first = self.ABS_Z_N()
        second = per.ABS_Z_N()
        result = Integer.TRANS_N_Z(Natural.MUL_NN_N(first, second))
        
        # Знак результата определяется по правилу знаков:
        # Если знаки одинаковые - результат положительный (0)
        # Если знаки разные - результат отрицательный (1)
        result.sign = (self.sign != per.sign)
        return result
    
    def DIV_ZZ_Z(self, per):
        # Целочисленное деление целых чисел
        # Проверка деления на ноль
        if all(digit == 0 for digit in per.number):
            raise ZeroDivisionError("Division by zero")
            
        # Работаем с модулями чисел
        abs_self = self.ABS_Z_N()
        abs_per = per.ABS_Z_N()
        
        # Выполняем деление модулей как натуральных чисел
        result = Integer.TRANS_N_Z(Natural.DIV_NN_N(abs_self, abs_per))
        
        # Особенная обработка для отрицательного делимого:
        # Если делимое отрицательное и деление было не точным,
        # нужно скорректировать частное
        if self.sign == 1:
            product = result.MUL_ZZ_Z(per)
            abs_product = product.ABS_Z_N()
            # Если произведение частного на делитель не равно делимому,
            # увеличиваем частное на 1
            if Natural.COM_NN_D(abs_product, abs_self) != 0:
                result = result.ADD_ZZ_Z(Integer('1'))
                
        # Устанавливаем знак результата по правилу знаков
        # (только для ненулевого результата)
        if not all(digit == 0 for digit in result.number):
            result.sign = (self.sign != per.sign)
        return result
    
    def MOD_ZZ_Z(self, per):
        # Остаток от деления целых чисел
        # Проверка деления на ноль
        if all(digit == 0 for digit in per.number):
            raise ZeroDivisionError(f"{self.__str__()} % {per.__str__()}")
            
        # Вычисляем частное
        quotient = self.DIV_ZZ_Z(per)
        # Вычисляем произведение частного на делитель
        product = quotient.MUL_ZZ_Z(per)
        # Остаток = делимое - частное × делитель
        result = self.SUB_ZZ_Z(product)
        
        # Корректировка остатка для неотрицательного результата
        # (в математике принято, что остаток должен быть неотрицательным)
        if result.sign == -1:
            absPer = per.ABS_ZZ_Z()
            result = result.ADD_ZZ_Z(absPer)
        return result

def tests_for_integers():
    # Создание тестовых целых чисел для проверки всех функций
    int1 = Integer("123")    # Положительное число
    int2 = Integer("-45")    # Отрицательное число  
    int3 = Integer("0")      # Ноль
    int4 = Integer("-678")   # Отрицательное число
    int5 = Integer("999")    # Положительное число
    int6 = Integer("-1")     # Отрицательная единица
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА INTEGER")
    print("=" * 60)

    print("\n1. ТЕСТИРОВАНИЕ МОДУЛЯ (ABS_Z_N):")
    print(f"   |{int1}| = {int1.ABS_Z_N()}")  # Должно быть 123
    print(f"   |{int2}| = {int2.ABS_Z_N()}")  # Должно быть 45
    print(f"   |{int3}| = {int3.ABS_Z_N()}")  # Должно быть 0
    print(f"   |{int4}| = {int4.ABS_Z_N()}")  # Должно быть 678

    print("\n2. ТЕСТИРОВАНИЕ ОПРЕДЕЛЕНИЯ ЗНАКА (POZ_Z_D):")
    print(f"   Знак числа {int1}: {int1.POZ_Z_D()}")  # Должно быть 2 (положительное)
    print(f"   Знак числа {int2}: {int2.POZ_Z_D()}")  # Должно быть 1 (отрицательное)
    print(f"   Знак числа {int3}: {int3.POZ_Z_D()}")  # Должно быть 0 (ноль)
    print(f"   Знак числа {int6}: {int6.POZ_Z_D()}")  # Должно быть 1 (отрицательное)

    print("\n3. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ НА -1 (MUL_ZM_Z):")
    print(f"   -({int1}) = {int1.MUL_ZM_Z()}")  # Должно быть -123
    print(f"   -({int2}) = {int2.MUL_ZM_Z()}")  # Должно быть 45
    print(f"   -({int3}) = {int3.MUL_ZM_Z()}")  # Должно быть 0
    print(f"   -({int5}) = {int5.MUL_ZM_Z()}")  # Должно быть -999

    print("\n4. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ NATURAL -> INTEGER (TRANS_N_Z):")
    nat1 = Natural("123")
    nat2 = Natural("0")
    nat3 = Natural("789")
    
    int_from_nat1 = Integer.TRANS_N_Z(nat1)
    int_from_nat2 = Integer.TRANS_N_Z(nat2)
    int_from_nat3 = Integer.TRANS_N_Z(nat3)
    
    print(f"   Natural('123') -> Integer: {int_from_nat1}")  # Должно быть 123
    print(f"   Natural('0') -> Integer: {int_from_nat2}")    # Должно быть 0
    print(f"   Natural('789') -> Integer: {int_from_nat3}")  # Должно быть 789

    print("\n5. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ INTEGER -> NATURAL (TRANS_Z_N):")
    print(f"   Integer('123') -> Natural: {int1.TRANS_Z_N()}")  # Должно быть 123
    print(f"   Integer('0') -> Natural: {int3.TRANS_Z_N()}")    # Должно быть 0
    
    try:
        int2.TRANS_Z_N()
        print(f"   Integer('-45') -> Natural: ОШИБКА - исключение не сработало!")
    except ValueError as e:
        print(f"   Integer('-45') -> Natural: {e}")  # Должно вызвать исключение

    print("\n6. ТЕСТИРОВАНИЕ СТРОКОВОГО ПРЕДСТАВЛЕНИЯ:")
    print(f"   Integer('123'): '{int1}'")    # Должно быть '123'
    print(f"   Integer('-45'): '{int2}'")    # Должно быть '-45'
    print(f"   Integer('0'): '{int3}'")      # Должно быть '0'
    print(f"   Integer('-678'): '{int4}'")   # Должно быть '-678'
    print(f"   Integer('999'): '{int5}'")    # Должно быть '999'

    print("\n7. ТЕСТИРОВАНИЕ СЛОЖЕНИЯ (ADD_ZZ_Z):")
    print(f"   {int1} + {int5} = {int1.ADD_ZZ_Z(int5)}")  # 123 + 999 = 1122
    print(f"   {int2} + {int4} = {int2.ADD_ZZ_Z(int4)}")  # -45 + (-678) = -723
    print(f"   {int1} + {int2} = {int1.ADD_ZZ_Z(int2)}")  # 123 + (-45) = 78
    print(f"   {int2} + {int1} = {int2.ADD_ZZ_Z(int1)}")  # -45 + 123 = 78
    print(f"   {int1} + {int3} = {int1.ADD_ZZ_Z(int3)}")  # 123 + 0 = 123
    print(f"   {int3} + {int2} = {int3.ADD_ZZ_Z(int2)}")  # 0 + (-45) = -45
    int7 = Integer("45")
    print(f"   {int2} + {int7} = {int2.ADD_ZZ_Z(int7)}")  # -45 + 45 = 0

    print("\n8. ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ (SUB_ZZ_Z):")
    print(f"   {int1} - {int5} = {int1.SUB_ZZ_Z(int5)}")  # 123 - 999 = -876
    print(f"   {int2} - {int4} = {int2.SUB_ZZ_Z(int4)}")  # -45 - (-678) = 633
    print(f"   {int1} - {int2} = {int1.SUB_ZZ_Z(int2)}")  # 123 - (-45) = 168
    print(f"   {int2} - {int1} = {int2.SUB_ZZ_Z(int1)}")  # -45 - 123 = -168
    print(f"   {int1} - {int3} = {int1.SUB_ZZ_Z(int3)}")  # 123 - 0 = 123
    print(f"   {int3} - {int2} = {int3.SUB_ZZ_Z(int2)}")  # 0 - (-45) = 45
    print(f"   {int1} - {int1} = {int1.SUB_ZZ_Z(int1)}")  # 123 - 123 = 0

    print("\n9. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ (MUL_ZZ_Z):")
    print(f"   {int1} * {int5} = {int1.MUL_ZZ_Z(int5)}")  # 123 * 999 = 122877
    print(f"   {int2} * {int4} = {int2.MUL_ZZ_Z(int4)}")  # -45 * (-678) = 30510
    print(f"   {int1} * {int2} = {int1.MUL_ZZ_Z(int2)}")  # 123 * (-45) = -5535
    print(f"   {int1} * {int3} = {int1.MUL_ZZ_Z(int3)}")  # 123 * 0 = 0
    print(f"   {int3} * {int2} = {int3.MUL_ZZ_Z(int2)}")  # 0 * (-45) = 0
    int8 = Integer("1")
    print(f"   {int1} * {int8} = {int1.MUL_ZZ_Z(int8)}")  # 123 * 1 = 123
    print(f"   {int1} * {int6} = {int1.MUL_ZZ_Z(int6)}")  # 123 * (-1) = -123

    print("\n10. ТЕСТИРОВАНИЕ ЦЕЛОЧИСЛЕННОГО ДЕЛЕНИЯ (DIV_ZZ_Z):")
    int9 = Integer("25")
    int10 = Integer("5")
    print(f"   {int9} / {int10} = {int9.DIV_ZZ_Z(int10)}")  # 25 / 5 = 5
    int11 = Integer("-25")
    int12 = Integer("-5")
    print(f"   {int11} / {int12} = {int11.DIV_ZZ_Z(int12)}")  # -25 / -5 = 5
    print(f"   {int9} / {int12} = {int9.DIV_ZZ_Z(int12)}")    # 25 / -5 = -5
    print(f"   {int11} / {int10} = {int11.DIV_ZZ_Z(int10)}")  # -25 / 5 = -5
    print(f"   {int1} / {int8} = {int1.DIV_ZZ_Z(int8)}")      # 123 / 1 = 123
    print(f"   {int1} / {int6} = {int1.DIV_ZZ_Z(int6)}")      # 123 / -1 = -123
    int13 = Integer("7")
    int14 = Integer("3")
    print(f"   {int13} / {int14} = {int13.DIV_ZZ_Z(int14)}")  # 7 / 3 = 2
    int15 = Integer("-7")
    print(f"   {int15} / {int14} = {int15.DIV_ZZ_Z(int14)}")  # -7 / 3 = -3
    print(f"   {int13} / {int14.MUL_ZM_Z()} = {int13.DIV_ZZ_Z(int14.MUL_ZM_Z())}")  # 7 / -3 = -2
    print(f"   {int3} / {int1} = {int3.DIV_ZZ_Z(int1)}")      # 0 / 123 = 0
    try:
        int1.DIV_ZZ_Z(int3)
        print(f"   {int1} / {int3} = ОШИБКА - исключение не сработало!")
    except ZeroDivisionError as e:
        print(f"   {int1} / {int3} = {e}")  # Должно вызвать исключение

    print("\n11. ТЕСТИРОВАНИЕ ОСТАТКА ОТ ДЕЛЕНИЯ (MOD_ZZ_Z):")
    print(f"   {int13} % {int14} = {int13.MOD_ZZ_Z(int14)}")  # 7 % 3 = 1
    print(f"   {int15} % {int14.MUL_ZM_Z()} = {int15.MOD_ZZ_Z(int14.MUL_ZM_Z())}")  # -7 % -3 = 2
    print(f"   {int13} % {int14.MUL_ZM_Z()} = {int13.MOD_ZZ_Z(int14.MUL_ZM_Z())}")  # 7 % -3 = 1
    print(f"   {int15} % {int14} = {int15.MOD_ZZ_Z(int14)}")  # -7 % 3 = 2
    print(f"   {int1} % {int8} = {int1.MOD_ZZ_Z(int8)}")      # 123 % 1 = 0
    print(f"   {int1} % {int6} = {int1.MOD_ZZ_Z(int6)}")      # 123 % -1 = 0
    print(f"   {int3} % {int1} = {int3.MOD_ZZ_Z(int1)}")      # 0 % 123 = 0
    try:
        int1.MOD_ZZ_Z(int3)
        print(f"   {int1} % {int3} = ОШИБКА - исключение не сработало!")
    except ZeroDivisionError as e:
        print(f"   {int1} % {int3} = {e}")  # Должно вызвать исключение

tests_for_integers()