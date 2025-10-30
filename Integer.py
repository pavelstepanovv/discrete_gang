from Natural import Natural


class Integer:
    def __init__(self, number: str):
        # Инициализация целого числа из строки
        if number[0] == '-':
            # Если число отрицательное, сохраняем цифры и устанавливаем знак 1
            self.number = list(map(int, number[1:]))
            self.sign = 1
        else:
            # Если число положительное, сохраняем все цифры и устанавливаем знак 0
            self.number = list(map(int, number[0:]))
            self.sign = 0
        # Если все цифры нули, устанавливаем знак 0 (положительное)
        if all(digit == 0 for digit in self.number):
            self.sign = 0

    def __str__(self):
        # Строковое представление числа
        if self.sign == 1 and not all(digit == 0 for digit in self.number):
            sign_prefix = '-'  # Добавляем минус для отрицательных чисел
        else:
            sign_prefix = ''
        number_str = ''.join(map(str, self.number))
        return sign_prefix + number_str

    def ABS_Z_N(self):
        # Возвращает модуль числа как натуральное число
        return Natural(''.join(map(str, self.number)))

    def POZ_Z_D(self):
        # Определение знака числа: 0 - ноль, 1 - отрицательное, 2 - положительное
        if all(digit == 0 for digit in self.number):
            return 0
        elif self.sign == 1:
            return 1
        else:
            return 2

    def MUL_ZM_Z(self):
        # Умножение числа на -1 (смена знака)
        if all(digit == 0 for digit in self.number):
            return Integer('0')  # Ноль остается нулем
        result = Integer(str(self))
        result.sign = 1 - result.sign  # Меняем знак: 0->1, 1->0
        return result

    @staticmethod
    def TRANS_N_Z(number: Natural):
        # Преобразование натурального числа в целое
        result = Integer(str(number))
        return result

    def TRANS_Z_N(self):
        # Преобразование целого числа в натуральное (только для неотрицательных)
        if self.sign == 1:
            raise ValueError("Отрицательное число нельзя преобразовать в натуральное")
        return Natural(''.join(map(str, self.number)))


    # Сложение целых чисел
    def ADD_ZZ_Z(self, other):
        # Если знаки одинаковые - складываем модули и сохраняем знак
        if self.POZ_Z_D() == other.POZ_Z_D():
            abs_sum = self.ABS_Z_N().ADD_NN_N(other.ABS_Z_N())
            result = Integer.TRANS_N_Z(abs_sum)
            if self.POZ_Z_D() == 1:  # Оба отрицательные
                result.sign = 1
            return result

        # Если знаки разные - вычитаем модули
        abs_self = self.ABS_Z_N()
        abs_other = other.ABS_Z_N()

        comparison = abs_self.COM_NN_D(abs_other)

        if comparison == 2:  # |self| > |other|
            abs_result = abs_self.SUB_NN_N(abs_other)
            result = Integer.TRANS_N_Z(abs_result)
            result.sign = self.sign
        elif comparison == 1:  # |self| < |other|
            abs_result = abs_other.SUB_NN_N(abs_self)
            result = Integer.TRANS_N_Z(abs_result)
            result.sign = other.sign
        else:  # |self| == |other|
            return Integer('0')

        return result

    # Вычитание целых чисел: self - other
    def SUB_ZZ_Z(self, other):
        # Преобразуем вычитание в сложение: a - b = a + (-b)
        neg_other = other.MUL_ZM_Z()
        return self.ADD_ZZ_Z(neg_other)

    # Умножение целых чисел
    def MUL_ZZ_Z(self, other):
        # Умножаем модули
        abs_product = self.ABS_Z_N().MUL_NN_N(other.ABS_Z_N())
        result = Integer.TRANS_N_Z(abs_product)

        # Определяем знак результата
        if self.POZ_Z_D() == 0 or other.POZ_Z_D() == 0:  # Если один из множителей ноль
            result.sign = 0
        elif self.POZ_Z_D() == other.POZ_Z_D():  # Одинаковые знаки
            result.sign = 0  # Положительный
        else:  # Разные знаки
            result.sign = 1  # Отрицательный

        return result

    # Частное от деления целого на целое (делитель отличен от нуля)
    def DIV_ZZ_Z(self, other):
        if other.POZ_Z_D() == 0:
            raise ValueError("Деление на ноль невозможно")

        # Делим модули
        abs_dividend = self.ABS_Z_N()
        abs_divisor = other.ABS_Z_N()

        # Проверяем, что делимое >= делителя по модулю
        if abs_dividend.COM_NN_D(abs_divisor) == 1:
            quotient = Natural('0')
        else:
            quotient = abs_dividend.DIV_NN_N(abs_divisor)

        result = Integer.TRANS_N_Z(quotient)

        # Определяем знак результата
        if self.POZ_Z_D() == 0:  # Делимое равно нулю
            result.sign = 0
        elif self.POZ_Z_D() == other.POZ_Z_D():  # Одинаковые знаки
            result.sign = 0  # Положительный
        else:  # Разные знаки
            result.sign = 1  # Отрицательный

        return result

    # Остаток от деления целого на целое (делитель отличен от нуля)
    def MOD_ZZ_Z(self, other):
        if other.POZ_Z_D() == 0:
            raise ValueError("Деление на ноль невозможно")

        # Вычисляем частное
        quotient = self.DIV_ZZ_Z(other)
        # Вычисляем произведение частного и делителя
        product = quotient.MUL_ZZ_Z(other)
        # Вычисляем остаток: self - product
        remainder = self.SUB_ZZ_Z(product)

        return remainder


def tests_for_new_functions():
    int1 = Integer("123")
    int2 = Integer("-45")
    int3 = Integer("0")
    int4 = Integer("-678")
    int5 = Integer("999")
    int6 = Integer("-1")
    int7 = Integer("5")
    int8 = Integer("-10")
    int9 = Integer("15")
    int10 = Integer("-3")

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА INTEGER")
    print("=" * 60)

    print("\n1. ТЕСТИРОВАНИЕ МОДУЛЯ (ABS_Z_N):")
    print(f"   |{int1}| = {int1.ABS_Z_N()}")
    print(f"   |{int2}| = {int2.ABS_Z_N()}")
    print(f"   |{int3}| = {int3.ABS_Z_N()}")
    print(f"   |{int4}| = {int4.ABS_Z_N()}")

    print("\n2. ТЕСТИРОВАНИЕ ОПРЕДЕЛЕНИЯ ЗНАКА (POZ_Z_D):")
    print(f"   Знак числа {int1}: {int1.POZ_Z_D()}")
    print(f"   Знак числа {int2}: {int2.POZ_Z_D()}")
    print(f"   Знак числа {int3}: {int3.POZ_Z_D()}")
    print(f"   Знак числа {int6}: {int6.POZ_Z_D()}")

    print("\n3. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ НА -1 (MUL_ZM_Z):")
    print(f"   -({int1}) = {int1.MUL_ZM_Z()}")
    print(f"   -({int2}) = {int2.MUL_ZM_Z()}")
    print(f"   -({int3}) = {int3.MUL_ZM_Z()}")
    print(f"   -({int5}) = {int5.MUL_ZM_Z()}")

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

    try:
        int2.TRANS_Z_N()
        print(f"   Integer('-45') -> Natural: ОШИБКА - исключение не сработало!")
    except ValueError as e:
        print(f"   Integer('-45') -> Natural: {e}")

    print("\n ТЕСТИРОВАНИЕ СТРОКОВОГО ПРЕДСТАВЛЕНИЯ:")
    print(f"   Integer('123'): '{int1}'")
    print(f"   Integer('-45'): '{int2}'")
    print(f"   Integer('0'): '{int3}'")
    print(f"   Integer('-678'): '{int4}'")
    print(f"   Integer('999'): '{int5}'")


    print("\n6. ТЕСТИРОВАНИЕ СЛОЖЕНИЯ ЦЕЛЫХ ЧИСЕЛ (ADD_ZZ_Z):")
    print(f"   {int1} + {int2} = {int1.ADD_ZZ_Z(int2)}")
    print(f"   {int2} + {int1} = {int2.ADD_ZZ_Z(int1)}")
    print(f"   {int1} + {int3} = {int1.ADD_ZZ_Z(int3)}")
    print(f"   {int4} + {int5} = {int4.ADD_ZZ_Z(int5)}")
    print(f"   {int6} + {int7} = {int6.ADD_ZZ_Z(int7)}")
    print(f"   {int4} + {int6} = {int4.ADD_ZZ_Z(int6)}")

    print("\n7. ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ ЦЕЛЫХ ЧИСЕЛ (SUB_ZZ_Z):")
    print(f"   {int1} - {int2} = {int1.SUB_ZZ_Z(int2)}")
    print(f"   {int2} - {int1} = {int2.SUB_ZZ_Z(int1)}")
    print(f"   {int5} - {int1} = {int5.SUB_ZZ_Z(int1)}")
    print(f"   {int3} - {int6} = {int3.SUB_ZZ_Z(int6)}")
    print(f"   {int6} - {int3} = {int6.SUB_ZZ_Z(int3)}")
    print(f"   {int4} - {int4} = {int4.SUB_ZZ_Z(int4)}")

    print("\n8. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ ЦЕЛЫХ ЧИСЕЛ (MUL_ZZ_Z):")
    print(f"   {int1} * {int2} = {int1.MUL_ZZ_Z(int2)}")
    print(f"   {int2} * {int1} = {int2.MUL_ZZ_Z(int1)}")
    print(f"   {int1} * {int3} = {int1.MUL_ZZ_Z(int3)}")
    print(f"   {int5} * {int6} = {int5.MUL_ZZ_Z(int6)}")
    print(f"   {int7} * {int8} = {int7.MUL_ZZ_Z(int8)}")
    print(f"   {int9} * {int10} = {int9.MUL_ZZ_Z(int10)}")

    print("\n9. ТЕСТИРОВАНИЕ ЧАСТНОГО ОТ ДЕЛЕНИЯ (DIV_ZZ_Z):")
    print(f"   {int1} / {int7} = {int1.DIV_ZZ_Z(int7)}")
    print(f"   {int9} / {int10} = {int9.DIV_ZZ_Z(int10)}")
    print(f"   {int4} / {int10} = {int4.DIV_ZZ_Z(int10)}")
    print(f"   {int5} / {int1} = {int5.DIV_ZZ_Z(int1)}")
    print(f"   {int6} / {int7} = {int6.DIV_ZZ_Z(int7)}")
    print(f"   {int3} / {int7} = {int3.DIV_ZZ_Z(int7)}")

    # Тест деления на ноль
    try:
        int1.DIV_ZZ_Z(int3)
        print(f"   {int1} / {int3} = ОШИБКА - исключение не сработало!")
    except ValueError as e:
        print(f"   {int1} / {int3} = {e}")

    print("\n10. ТЕСТИРОВАНИЕ ОСТАТКА ОТ ДЕЛЕНИЯ (MOD_ZZ_Z):")
    print(f"   {int1} % {int7} = {int1.MOD_ZZ_Z(int7)}")
    print(f"   {int9} % {int10} = {int9.MOD_ZZ_Z(int10)}")
    print(f"   {int4} % {int10} = {int4.MOD_ZZ_Z(int10)}")
    print(f"   {int5} % {int1} = {int5.MOD_ZZ_Z(int1)}")
    print(f"   {int6} % {int7} = {int6.MOD_ZZ_Z(int7)}")
    print(f"   {int3} % {int7} = {int3.MOD_ZZ_Z(int7)}")

    # Тест деления на ноль
    try:
        int1.MOD_ZZ_Z(int3)
        print(f"   {int1} % {int3} = ОШИБКА - исключение не сработало!")
    except ValueError as e:
        print(f"   {int1} % {int3} = {e}")

    print("\n11. КОМПЛЕКСНЫЕ ТЕСТЫ:")
    # Тест: (a + b) * c = a*c + b*c
    a = Integer("10")
    b = Integer("-5")
    c = Integer("3")

    left_side = a.ADD_ZZ_Z(b).MUL_ZZ_Z(c)
    right_side = a.MUL_ZZ_Z(c).ADD_ZZ_Z(b.MUL_ZZ_Z(c))
    print(f"   ({a} + {b}) * {c} = {left_side}")
    print(f"   {a}*{c} + {b}*{c} = {right_side}")
    print(f"   Дистрибутивность: {'ВЫПОЛНЯЕТСЯ' if str(left_side) == str(right_side) else 'НЕ ВЫПОЛНЯЕТСЯ'}")

    # Тест: a / b * b + a % b = a
    a = Integer("17")
    b = Integer("5")
    quotient = a.DIV_ZZ_Z(b)
    remainder = a.MOD_ZZ_Z(b)
    reconstruction = quotient.MUL_ZZ_Z(b).ADD_ZZ_Z(remainder)
    print(f"   {a} / {b} = {quotient}, остаток = {remainder}")
    print(f"   {quotient} * {b} + {remainder} = {reconstruction}")
    print(f"   Реконструкция: {'ВЫПОЛНЯЕТСЯ' if str(a) == str(reconstruction) else 'НЕ ВЫПОЛНЯЕТСЯ'}")


tests_for_new_functions()
