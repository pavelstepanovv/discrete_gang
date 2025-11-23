#выполнили Кяримов А., гр. 4381 и Серженко Д., гр. 4384

from Natural import Natural
class Integer:
    def __init__(self, number: str):
        # Инициализация целого числа из строки
        # Обрабатываем знак: если первый символ '-', то число отрицательное
        if number[0] == '-':
            # Сохраняем цифры числа (все символы после минуса)
            self.number = list(map(int, number[1:]))
            self.sign = 1  # 1 означает "отрицательное число"
        else:
            # Сохраняем все цифры числа
            self.number = list(map(int, number[0:]))
            self.sign = 0  # 0 означает "неотрицательное число"
        
        # Особый случай: если все цифры нули, то число неотрицательное
        if all(digit == 0 for digit in self.number):
            self.sign = 0
    
    def __str__(self):
        # Строковое представление числа
        # Добавляем знак "-" только для отрицательных ненулевых чисел
        if self.sign == 1 and not all(digit == 0 for digit in self.number):
            sign_prefix = '-'
        else:
            sign_prefix = ''
        # Объединяем цифры в строку и добавляем знак
        number_str = ''.join(map(str, self.number))
        return sign_prefix + number_str

    #1. Абсолютная величина числа, результат - натуральное
    def ABS_Z_N(self):
        # Абсолютная величина целого числа - это его модуль (значение без учета знака)
        # Поскольку в натуральных числах нет отрицательных значений,
        # просто преобразуем цифры в натуральное число без учета знака
        return Natural(''.join(map(str, self.number)))

    #2. Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    def POZ_Z_D(self):
        # Если все цифры числа равны нулю, то это ноль
        if all(digit == 0 for digit in self.number):
            return 0
        # Проверяем знак числа
        # Если знак отрицательный (sign == 1), возвращаем 1 (отрицательное)
        elif self.sign == 1:
            return 1
        # Если число не ноль и знак не отрицательный, то число положительное, возвращаем 2
        else:
            return 2

    #3. Умножение целого на (-1)
    def MUL_ZM_Z(self):
        # Ноль остается нулем при умножении на (-1), так как -0 = 0
        if all(digit == 0 for digit in self.number):
            return Integer('0')
        
        # Создаем копию исходного числа для безопасного изменения
        result = Integer(str(self))
        
        # Меняем знак на противоположный
        # Если был положительный (0), становится отрицательный (1)
        # 0 → 1-0 = 1
        # Если был отрицательный (1), становится положительный (0)
        # 1 → 1-1 = 0
        result.sign = 1 - result.sign
        
        return result
    
    @staticmethod
    #4. Преобразование натурального в целое
    def TRANS_N_Z(number: Natural):
        # Натуральное число всегда преобразуется в неотрицательное целое,
        # поскольку натуральные числа по определению неотрицательны
        result = Integer(str(number))
        return result

    #5. Преобразование целого неотрицательного в натуральное
    def TRANS_Z_N(self):
        # Отрицательные числа не могут быть преобразованы в натуральные
        if self.sign == 1:
            raise ValueError("Отрицательное число нельзя преобразовать в натуральное")
        
        # Преобразуем целое неотрицательное число в натуральное
        # Просто создаем натуральное число из цифр исходного числа
        return Natural(''.join(map(str, self.number)))

    #6. Сложение целых чисел
    def ADD_ZZ_Z(self, other):
        # Определяем знаки обоих чисел с помощью метода POZ_Z_D
        # 0 - ноль, 1 - отрицательное, 2 - положительное
        sign1 = self.POZ_Z_D()
        sign2 = other.POZ_Z_D()
        
        # Проверяем особые случаи с нулевыми слагаемыми
        # Если первое число равно нулю, возвращаем второе число
        if sign1 == 0:
            return other
        # Если второе число равно нулю, возвращаем первое число
        if sign2 == 0:
            return self
                
        # Случай: оба числа положительные
        # Сумма положительных чисел - положительное число
        if sign1 == 2 and sign2 == 2:
            # Складываем модули чисел и возвращаем положительный результат
            result = self.ABS_Z_N().ADD_NN_N(other.ABS_Z_N())
            return Integer.TRANS_N_Z(result)
                
        # Случай: оба числа отрицательные  
        # Сумма отрицательных чисел - отрицательное число
        if sign1 == 1 and sign2 == 1:
            # Складываем модули чисел и меняем знак на отрицательный
            result = self.ABS_Z_N().ADD_NN_N(other.ABS_Z_N())
            return Integer.TRANS_N_Z(result).MUL_ZM_Z()
                
        # Случаи с разными знаками (положительное + отрицательное или наоборот)
        # Сравниваем модули чисел для определения большего по абсолютной величине
        compare = Natural.COM_NN_D(self.ABS_Z_N(), other.ABS_Z_N())
        
        # Если модули равны, сумма равна нулю (a + (-a) = 0)
        if compare == 0:
            return Integer('0')
                
        # Случай: положительное + отрицательное
        if sign1 == 2 and sign2 == 1:
            if compare == 2:  # Модуль первого числа больше
                # Вычитаем из большего модуля меньший, результат положительный
                result = self.ABS_Z_N().SUB_NN_N(other.ABS_Z_N())
                return Integer.TRANS_N_Z(result)
            else:  # Модуль второго числа больше
                # Вычитаем из большего модуля меньший, результат отрицательный
                result = other.ABS_Z_N().SUB_NN_N(self.ABS_Z_N())
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
                    
        # Случай: отрицательное + положительное  
        if sign1 == 1 and sign2 == 2:
            if compare == 2:  # Модуль первого числа больше
                # Вычитаем из большего модуля меньший, результат отрицательный
                result = self.ABS_Z_N().SUB_NN_N(other.ABS_Z_N())
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            else:  # Модуль второго числа больше
                # Вычитаем из большего модуля меньший, результат положительный
                result = other.ABS_Z_N().SUB_NN_N(self.ABS_Z_N())
                return Integer.TRANS_N_Z(result)

    #7. Вычитание целых чисел
    def SUB_ZZ_Z(self, other):
        # Проверяем особый случай, когда уменьшаемое равно нулю
        # 0 - b = -b (противоположное число)
        if self.POZ_Z_D() == 0:
            return other.MUL_ZM_Z()
        
        # Проверяем особый случай, когда вычитаемое равно нулю
        # a - 0 = a (исходное число без изменений)
        if other.POZ_Z_D() == 0:
            return self
        
        # Определяем знаки обоих чисел для анализа случаев
        # 0 - ноль, 1 - отрицательное, 2 - положительное
        sign1 = self.POZ_Z_D()
        sign2 = other.POZ_Z_D()
        
        # Вычисляем абсолютные значения (модули) чисел
        # для работы с натуральными числами в операциях сравнения и вычитания
        abs_self = self.ABS_Z_N()
        abs_other = other.ABS_Z_N()
        
        # Случай: оба числа положительные (a - b, где a>0, b>0)
        if sign1 == 2 and sign2 == 2:
            # Сравниваем модули чисел для определения большего
            compare = abs_self.COM_NN_D(abs_other)
            if compare == 2:  # Первое число больше второго
                # Вычитаем из большего меньшее, результат положительный
                result = abs_self.SUB_NN_N(abs_other)
                return Integer.TRANS_N_Z(result)
            elif compare == 1:  # Второе число больше первого
                # Вычитаем из большего меньшее, результат отрицательный
                result = abs_other.SUB_NN_N(abs_self)
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            else:  # Числа равны, разность равна нулю
                return Integer('0')
        
        # Случай: положительное минус отрицательное (a - (-b) = a + b)
        # Преобразуется в сложение положительных чисел
        elif sign1 == 2 and sign2 == 1:
            result = abs_self.ADD_NN_N(abs_other)
            return Integer.TRANS_N_Z(result)
        
        # Случай: отрицательное минус положительное (-a - b = -(a + b))
        # Преобразуется в сложение модулей с отрицательным знаком
        elif sign1 == 1 and sign2 == 2:
            result = abs_self.ADD_NN_N(abs_other)
            return Integer.TRANS_N_Z(result).MUL_ZM_Z()
        
        # Случай: отрицательное минус отрицательное (-a - (-b) = -a + b = b - a)
        # Сравниваем модули для определения знака результата
        elif sign1 == 1 and sign2 == 1:
            compare = abs_self.COM_NN_D(abs_other)
            if compare == 2:  # Модуль первого больше
                # |a| > |b|, результат отрицательный: -(|a| - |b|)
                result = abs_self.SUB_NN_N(abs_other)
                return Integer.TRANS_N_Z(result).MUL_ZM_Z()
            elif compare == 1:  # Модуль второго больше
                # |b| > |a|, результат положительный: |b| - |a|
                result = abs_other.SUB_NN_N(abs_self)
                return Integer.TRANS_N_Z(result)
            else:  # Модули равны, результат ноль
                return Integer('0')

    #8. Умножение целых чисел
    def MUL_ZZ_Z(self, other):
        # Если один из множителей равен нулю, результат всегда ноль
        if self.POZ_Z_D() == 0 or other.POZ_Z_D() == 0:
            return Integer('0')
        
        # Вычисляем абсолютные значения (модули) чисел
        # для выполнения умножения натуральных чисел
        abs_self = self.ABS_Z_N()
        abs_other = other.ABS_Z_N()
        
        # Перемножаем модули чисел, используя умножение натуральных чисел
        # Получаем абсолютное значение результата
        result_abs = abs_self.MUL_NN_N(abs_other)
        
        # Преобразуем результат из натурального в целое число
        result = Integer.TRANS_N_Z(result_abs)
        
        # Определяем знак результата по правилу знаков:
        # Если знаки множителей одинаковые, результат положительный
        # Если знаки множителей разные, результат отрицательный
        if self.POZ_Z_D() != other.POZ_Z_D():
            result = result.MUL_ZM_Z()
        
        return result

    #9. Частное от деления целого на целое (делитель отличен от нуля)
    def DIV_ZZ_Z(self, other):
        # Проверяем, что делитель не равен нулю
        if other.POZ_Z_D() == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        
        # Если делимое равно нулю, результат деления всегда ноль
        if self.POZ_Z_D() == 0:
            return Integer('0')
        
        # Вычисляем абсолютные значения (модули) чисел для выполнения деления натуральных чисел
        abs_self = self.ABS_Z_N()
        abs_other = other.ABS_Z_N()
        
        # Вычисляем частное от деления модулей (целая часть результата без учета знаков)
        abs_quotient = abs_self.DIV_NN_N(abs_other)
        
        # Определяем знаки делимого и делителя (если sign = 1, то отрицательное, если sign = 2, то положительное)
        sign_self = self.POZ_Z_D()
        sign_other = other.POZ_Z_D()
        
        # Определяем знак результата по правилу знаков:
        # Если знаки одинаковые - результат положительный
        if sign_self == sign_other:
            result_sign = 2  # положительный
        # Иначе знаки разные - результат отрицательный
        else:
            result_sign = 1  # отрицательный
        
        # Создаем результат с вычисленным знаком
        result = Integer(str(abs_quotient))
        result.sign = result_sign
        
        # Корректировка для обеспечения неотрицательного остатка
        # В целочисленном делении принято, что остаток должен удовлетворять: 0 ≤ остаток < |делитель|
        
        # Находим абсолютное значение остатка (либо 0, либо >0)
        remainder = abs_self.MOD_NN_N(abs_other)
        
        # Если есть ненулевой остаток, может потребоваться корректировка частного
        if remainder.NZER_N_B() == 'да':  # если остаток не равен нулю
            # Увеличиваем частное на 1 в следующих случаях:
            # 1. Оба числа отрицательные: (-a) ÷ (-b) должно давать округление вверх
            # 2. Делимое отрицательное, делитель положительный: (-a) ÷ b должно давать округление вверх
            # Это обеспечивает неотрицательный остаток при восстановлении: делимое = частное × делитель + остаток
            if (sign_self == 1 and sign_other == 1) or (sign_self == 1 and sign_other == 2):
                # Увеличиваем абсолютное значение частного на 1
                abs_result_plus_one = abs_quotient.ADD_1N_N()
                result = Integer(str(abs_result_plus_one))
                result.sign = result_sign
        
        return result

    #10. Остаток от деления целого на целое (делитель отличен от нуля)
    def MOD_ZZ_Z(self, other):
        # Проверяем, что делитель не равен нулю
        if other.POZ_Z_D() == 0:
            raise ZeroDivisionError("Остаток от деления на ноль невозможен!")
        
        # Если делимое равно нулю, остаток от деления всегда ноль
        if self.POZ_Z_D() == 0:
            return Integer('0')
        
        # Вычисляем неполное частное от деления (целая часть результата деления)
        quotient = self.DIV_ZZ_Z(other)
        
        # Вычисляем произведение частного и делителя (та часть делимого, которая делится нацело)
        product = quotient.MUL_ZZ_Z(other)
        
        # Вычисляем остаток по формуле: остаток = делимое - (неполное частное * делитель)
        remainder = self.SUB_ZZ_Z(product)
        
        # Корректировка остатка для выполнения условий:
        # Стандартное математическое определение: a = b × q + r, где 0 ≤ r < |b|
        # (остаток должен быть неотрицательным и меньше модуля делителя)

        # Находим модуль делителя как натуральное число для сравнения
        # и преобразуем его обратно в целое для выполнения арифметических операций
        # (это необходимо, так как операции ADD_ZZ_Z и SUB_ZZ_Z работают только с целыми числами)
        abs_other = other.ABS_Z_N()
        abs_other_int = Integer.TRANS_N_Z(abs_other)
        
        if remainder.POZ_Z_D() == 1:  # если остаток отрицательный
            # Добавляем к остатку модуль делителя, чтобы сделать остаток неотрицательным
            remainder = remainder.ADD_ZZ_Z(abs_other_int)
        else:  # если остаток неотрицательный
            # Проверяем, что остаток меньше модуля делителя
            remainder_natur = remainder.ABS_Z_N()  # преобразуем в натуральное для сравнения
            # Если остаток ≥ |делителя|
            if remainder_natur.COM_NN_D(abs_other) != 1:
                # Вычитаем модуль делителя, чтобы остаток стал меньше делителя
                remainder = remainder.SUB_ZZ_Z(abs_other_int)
        
        return remainder

def tests_for_integers():
    # Создаем тестовые целые числа
    int1 = Integer("123")      # положительное
    int2 = Integer("-45")      # отрицательное  
    int3 = Integer("0")        # ноль
    int4 = Integer("-678")     # отрицательное
    int5 = Integer("999")      # положительное
    int6 = Integer("-1")       # отрицательное
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА INTEGER")
    print("=" * 60)

    # Тест 1: ABS_Z_N - модуль числа
    print("\n1. ТЕСТИРОВАНИЕ МОДУЛЯ ЧИСЛА (ABS_Z_N):")
    print(f"   |{int1}| = {int1.ABS_Z_N()}")      # 123
    print(f"   |{int2}| = {int2.ABS_Z_N()}")      # 45
    print(f"   |{int3}| = {int3.ABS_Z_N()}")      # 0
    print(f"   |{int4}| = {int4.ABS_Z_N()}")      # 678

    # Тест 2: POZ_Z_D - определение знака
    print("\n2. ТЕСТИРОВАНИЕ ОПРЕДЕЛЕНИЯ ЗНАКА (POZ_Z_D):")
    print(f"   Знак числа {int1} = {int1.POZ_Z_D()}")  # 2 (положительное)
    print(f"   Знак числа {int2} = {int2.POZ_Z_D()}")  # 1 (отрицательное)
    print(f"   Знак числа {int3} = {int3.POZ_Z_D()}")  # 0 (ноль)
    print(f"   Знак числа {int6} = {int6.POZ_Z_D()}")  # 1 (отрицательное)

    # Тест 3: MUL_ZM_Z - умножение на -1
    print("\n3. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ НА -1 (MUL_ZM_Z):")
    print(f"   -({int1}) = {int1.MUL_ZM_Z()}")    # -123
    print(f"   -({int2}) = {int2.MUL_ZM_Z()}")    # 45
    print(f"   -({int3}) = {int3.MUL_ZM_Z()}")    # 0
    print(f"   -({int5}) = {int5.MUL_ZM_Z()}")    # -999

    # Тест 4: TRANS_N_Z - преобразование натурального в целое
    print("\n4. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ NATURAL -> INTEGER (TRANS_N_Z):")
    nat1 = Natural("123")
    nat2 = Natural("0") 
    nat3 = Natural("789")
    
    print(f"   Natural({nat1}) → Integer({Integer.TRANS_N_Z(nat1)})")  # 123
    print(f"   Natural({nat2}) → Integer({Integer.TRANS_N_Z(nat2)})")  # 0
    print(f"   Natural({nat3}) → Integer({Integer.TRANS_N_Z(nat3)})")  # 789

    # Тест 5: TRANS_Z_N - преобразование целого в натуральное
    print("\n5. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ INTEGER -> NATURAL (TRANS_Z_N):")
    print(f"   Integer({int1}) → Natural({int1.TRANS_Z_N()})")  # 123
    print(f"   Integer({int3}) → Natural({int3.TRANS_Z_N()})")  # 0
    try:
        print(f"   Integer({int2}) → Natural({int2.TRANS_Z_N()})")  # Ошибка
    except ValueError as e:
        print(f"   Integer({int2}) → Ошибка: {e}")

    # Тест 6: ADD_ZZ_Z - сложение целых чисел
    print("\n6. ТЕСТИРОВАНИЕ СЛОЖЕНИЯ ЦЕЛЫХ ЧИСЕЛ (ADD_ZZ_Z):")
    print(f"   {int1} + {int5} = {int1.ADD_ZZ_Z(int5)}")      # 1122
    print(f"   {int2} + {int4} = {int2.ADD_ZZ_Z(int4)}")      # -723
    print(f"   {int1} + {int2} = {int1.ADD_ZZ_Z(int2)}")      # 78
    print(f"   {int2} + {int1} = {int2.ADD_ZZ_Z(int1)}")      # 78
    print(f"   {int1} + {int3} = {int1.ADD_ZZ_Z(int3)}")      # 123
    print(f"   {int3} + {int2} = {int3.ADD_ZZ_Z(int2)}")      # -45
    int7 = Integer("45")
    print(f"   {int2} + {int7} = {int2.ADD_ZZ_Z(int7)}")      # 0

    # Тест 7: SUB_ZZ_Z - вычитание целых чисел
    print("\n7. ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ ЦЕЛЫХ ЧИСЕЛ (SUB_ZZ_Z):")
    print(f"   {int1} - {int5} = {int1.SUB_ZZ_Z(int5)}")      # -876
    print(f"   {int2} - {int4} = {int2.SUB_ZZ_Z(int4)}")      # 633
    print(f"   {int1} - {int2} = {int1.SUB_ZZ_Z(int2)}")      # 168
    print(f"   {int2} - {int1} = {int2.SUB_ZZ_Z(int1)}")      # -168
    print(f"   {int1} - {int3} = {int1.SUB_ZZ_Z(int3)}")      # 123
    print(f"   {int3} - {int2} = {int3.SUB_ZZ_Z(int2)}")      # 45
    print(f"   {int1} - {int1} = {int1.SUB_ZZ_Z(int1)}")      # 0

    # Тест 8: MUL_ZZ_Z - умножение целых чисел
    print("\n8. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ ЦЕЛЫХ ЧИСЕЛ (MUL_ZZ_Z):")
    print(f"   {int1} * {int5} = {int1.MUL_ZZ_Z(int5)}")      # 122877
    print(f"   {int2} * {int4} = {int2.MUL_ZZ_Z(int4)}")      # 30510
    print(f"   {int1} * {int2} = {int1.MUL_ZZ_Z(int2)}")      # -5535
    print(f"   {int1} * {int3} = {int1.MUL_ZZ_Z(int3)}")      # 0
    print(f"   {int3} * {int2} = {int3.MUL_ZZ_Z(int2)}")      # 0
    int8 = Integer("1")
    print(f"   {int1} * {int8} = {int1.MUL_ZZ_Z(int8)}")      # 123
    print(f"   {int1} * {int6} = {int1.MUL_ZZ_Z(int6)}")      # -123

    # Тест 9: DIV_ZZ_Z - целочисленное деление
    print("\n9. ТЕСТИРОВАНИЕ ЦЕЛОЧИСЛЕННОГО ДЕЛЕНИЯ (DIV_ZZ_Z):")
    int9 = Integer("25")
    int10 = Integer("5")
    print(f"   {int9} / {int10} = {int9.DIV_ZZ_Z(int10)}")    # 5
    int11 = Integer("-25")
    int12 = Integer("-5")
    print(f"   {int11} / {int12} = {int11.DIV_ZZ_Z(int12)}")  # 5
    print(f"   {int9} / {int12} = {int9.DIV_ZZ_Z(int12)}")    # -5
    print(f"   {int11} / {int10} = {int11.DIV_ZZ_Z(int10)}")  # -5
    print(f"   {int1} / {int8} = {int1.DIV_ZZ_Z(int8)}")      # 123
    print(f"   {int1} / {int6} = {int1.DIV_ZZ_Z(int6)}")      # -123
    int13 = Integer("7")
    int14 = Integer("3")
    print(f"   {int13} / {int14} = {int13.DIV_ZZ_Z(int14)}")  # 2
    int15 = Integer("-7")
    print(f"   {int15} / {int14} = {int15.DIV_ZZ_Z(int14)}")  # -3
    print(f"   {int13} / {int14.MUL_ZM_Z()} = {int13.DIV_ZZ_Z(int14.MUL_ZM_Z())}")  # -2
    print(f"   {int3} / {int1} = {int3.DIV_ZZ_Z(int1)}")      # 0
    try:
        print(f"   {int1} / {int3} = {int1.DIV_ZZ_Z(int3)}")  # Ошибка
    except ZeroDivisionError as e:
        print(f"   {int1} / {int3} → Ошибка: {e}")

    # Тест 10: MOD_ZZ_Z - остаток от деления
    print("\n10. ТЕСТИРОВАНИЕ ОСТАТКА ОТ ДЕЛЕНИЯ (MOD_ZZ_Z):")
    print(f"   {int13} % {int14} = {int13.MOD_ZZ_Z(int14)}")  # 1
    print(f"   {int15} % {int14} = {int15.MOD_ZZ_Z(int14)}")  # 2
    print(f"   {int13} % {int14.MUL_ZM_Z()} = {int13.MOD_ZZ_Z(int14.MUL_ZM_Z())}")  # 1
    print(f"   {int15} % {int14.MUL_ZM_Z()} = {int15.MOD_ZZ_Z(int14.MUL_ZM_Z())}")  # 2
    print(f"   {int1} % {int8} = {int1.MOD_ZZ_Z(int8)}")      # 0
    print(f"   {int1} % {int6} = {int1.MOD_ZZ_Z(int6)}")      # 0
    print(f"   {int3} % {int1} = {int3.MOD_ZZ_Z(int1)}")      # 0
    try:
        print(f"   {int1} % {int3} = {int1.MOD_ZZ_Z(int3)}")  # Ошибка
    except ZeroDivisionError as e:
        print(f"   {int1} % {int3} → Ошибка: {e}")

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЦЕЛЫХ ЧИСЕЛ ЗАВЕРШЕНО!")
    print("=" * 60)
    
tests_for_integers()
