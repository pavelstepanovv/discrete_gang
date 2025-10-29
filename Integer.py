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


def tests_for_integers():
    # Создание тестовых целых чисел
    int1 = Integer("123")
    int2 = Integer("-45")
    int3 = Integer("0")
    int4 = Integer("-678")
    int5 = Integer("999")
    int6 = Integer("-1")
    
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

    print("\n6. ТЕСТИРОВАНИЕ СТРОКОВОГО ПРЕДСТАВЛЕНИЯ:")
    print(f"   Integer('123'): '{int1}'")
    print(f"   Integer('-45'): '{int2}'")
    print(f"   Integer('0'): '{int3}'")
    print(f"   Integer('-678'): '{int4}'")
    print(f"   Integer('999'): '{int5}'")

tests_for_integers()