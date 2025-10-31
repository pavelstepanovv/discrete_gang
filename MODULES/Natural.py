#выполнили Мулюкина Е.В., гр. 4384 и Экажев Р.Х., гр. 4384

class Natural:
    def __init__(self, num: str):
        num = list(map(int, num))
        while len(num) > 1 and num[0] == 0:  # удаление незначащих нулей
            num = num[1:]
        self.num = num
    def __str__(self):
        return ''.join(map(str, self.num))
    
    # 1. Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
    def COM_NN_D(self, other) -> int:
    # Сравнение по длине
        if len(self.num) > len(other.num):
            return 2
        elif len(self.num) < len(other.num):
            return 1
    
        # Если длины равны, сравниваем по цифрам
        for i in range(len(self.num)):
            if self.num[i] > other.num[i]:
                return 2
            elif self.num[i] < other.num[i]:
                return 1
    
        # Все цифры равны
        return 0

    # 2. Проверка на ноль: если число не равно нулю, то «да» иначе «нет»
    def NZER_N_B(self):
        # Упрощенная проверка: если число равно "0"
        if len(self.num) == 1 and self.num[0] == 0:
            return 'нет'
        return 'да'

    # 3. Добавление 1 к натуральному числу
    def ADD_1N_N(self):
        num = self.num[::-1] # работаем с перевернутым числом (с младших разрядов)
        carry = 1 # начинаем с переноса 1

        for i in range(len(num)):
            num[i] += carry
            carry = num[i] // 10  # вычисляем перенос для следующего разряда
            num[i] %= 10  # оставляем только последнюю цифру

        if carry > 0:
            num.append(carry) # если после сложения всех цифр остался перенос, добавляем его как старший разряд

        return Natural(''.join(map(str, num[::-1])))

    #4. Сложение натуральных чисел
    def ADD_NN_N(self, other):
        if self.COM_NN_D(other) == 1:
            smaller = self.num[::-1] # делаем копии чисел и переворачиваем их
            larger = other.num[::-1]

        else:
            smaller = other.num[::-1]
            larger = self.num[::-1]

        smaller += [0] * (len(larger) - len(smaller)) # дополняем меньшее число нулями до размера большего

        result = []
        carry = 0 # хранение переноса разряда

        for i in range(len(larger)):
            digit_sum = smaller[i] + larger[i] + carry
            result.append(digit_sum % 10) # сохраняем в результат только последнюю цифру суммы
            carry = digit_sum // 10

        if carry > 0:
            result.append(carry) # если при сложении всех чисел остался перенос, добавляем старший разряд

        return Natural(''.join(map(str, result[::-1]))) # результат переворачиваем

    # 5. Вычитание из первого большего натурального числа второго меньшего или равного
    def SUB_NN_N(self, other) -> 'Natural':
        compare = self.COM_NN_D(other)

        if compare == 1:
            raise ValueError("Первое число должно быть больше или равно второму")
        elif compare == 0:
            return Natural('0')  

        a = self.num[::-1] # переворачиваем для вычитания с младших разрядов
        b = other.num[::-1]
        b += [0] * (len(a) - len(b)) # дополняем меньшее число нулями до размера большего

        result = []
        borrow = 0 # заём из старшего разряда
        for i in range(len(a)):
            current_digit = a[i] - borrow # вычитаем с учетом заёма

            if current_digit < b[i]:
                current_digit += 10 # нужно занять из старшего разряда
                borrow = 1
            else:
                borrow = 0

            digit_diff = current_digit - b[i] # вычитаем цифру второго числа
            result.append(digit_diff)

        # Убираем ведущие нули
        while len(result) > 1 and result[-1] == 0:
            result.pop()
    
        result.reverse()
        return Natural(''.join(map(str, result)))  # возвращаем Natural

    # 6. Умножение натурального числа на цифру
    def MUL_ND_N(self, digit: int):
        if not (0 <= digit <= 9):
            raise ValueError('Данные не являются цифрой!')
        if digit == 0 or (len(self.num) == 1 and self.num[0] == 0):
            return Natural('0')

        res_digits = []
        carry = 0 #переменная для переноса
        #проходим по числам исходного числа в обратном порядке
        for i in range(len(self.num) - 1, -1, -1):
            current_digit = self.num[i]
            product = current_digit * digit + carry
            res_digits.append(product % 10)
            carry = product // 10 #сохраняем старший разряд для переноса
        #если перенос остался - добавляем его
        if carry > 0:
            res_digits.append(carry)
        res_digits.reverse()
        res_str = ''.join(map(str, res_digits))

        return Natural(res_str)
    # 7. Умножение натурального числа на 10^k, k-натуральное (не длинное)
    def MUL_Nk_N(self, k: int):
        if k < 0:
            raise ValueError('Число k должно быть натуральным!')
        return Natural(str(self) + '0' * k)

    # 8. Умножение натуральных чисел
    def MUL_NN_N(self, other) -> 'Natural':
        if (len(self.num) == 1 and self.num[0] == 0) or (len(other.num) == 1 and other.num[0] == 0): # если хоть одно из чисел равно нулю
            return Natural('0')

        result = Natural('0')

        num_2 = other.num[::-1] # переворачиваем второе число
        for i, digit in enumerate(num_2):
            part_res = self.MUL_ND_N(digit) # умножаем первое число на цифру второго числа начиная с конца
            shifted_res = part_res.MUL_Nk_N(i) # сдвиг числа влево на i разрядов(+i нулей)
            result = result.ADD_NN_N(shifted_res) # суммируем полученное число с результатом

        return result

    #9. Вычитание из натурального, умноженного на цифру для случая с неотрицательным результатом
    def SUB_NDN_N(self, other, digit):
        # Используем MUL_ND_N для умножения other на digit
        product = other.MUL_ND_N(digit)
        
        # Используем COM_NN_D для сравнения self и product
        # Если self < product, выбрасываем ошибку
        if self.COM_NN_D(product) == 1:
            raise ValueError("Первое число должно быть больше или равно второму, умноженному на цифру")
        
        # Используем SUB_NN_N для вычитания
        return self.SUB_NN_N(product)

    #10. Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k, где k - номер позиции этой цифры (номер считается с нуля)
    def DIV_NN_Dk(self, other, k):
        # Проверка: делимое должно быть >= делителя
        if self.COM_NN_D(other) == 1:
            raise ValueError('Нельзя делить меньшее число на большее!')

        # Домножаем делитель на 10^k
        divisor_shifted = other.MUL_Nk_N(k)
        
        # Находим максимальную цифру d (0-9), такую что divisor_shifted * d <= self
        digit = 0
        for d in range(1, 10):
            product = divisor_shifted.MUL_ND_N(d)
            if product.COM_NN_D(self) != 2:  # если product <= self
                digit = d
            else:
                break
        return digit

    #11. Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
    def DIV_NN_N(self, other):
        if other.COM_NN_D(Natural('0')) == 0:
            raise ValueError('Деление на ноль невозможно!')

        comparison = self.COM_NN_D(other)
        if comparison == 1:  # если делимое меньше делителя
            return Natural('0')
        if comparison == 0:  # если числа равны
            return Natural('1')

        # Определяем количество разрядов в частном
        n = len(self.num)
        m = len(other.num)
        k = n - m  # максимальная степень для DIV_NN_Dk
        
        result_digits = []
        current_dividend = Natural(str(self))
        
        # Обрабатываем каждый разряд частного от старшего к младшему
        for i in range(k, -1, -1):
            # Находим цифру для текущего разряда
            digit = current_dividend.DIV_NN_Dk(other, i)
            result_digits.append(digit)
            
            # Вычитаем из текущего делимого other * digit * 10^i
            if digit > 0:
                temp = other.MUL_ND_N(digit)
                temp = temp.MUL_Nk_N(i)
                current_dividend = current_dividend.SUB_NDN_N(temp, 1)
        
        # Создаем результат, убирая ведущие нули
        result_str = ''.join(map(str, result_digits))
        result = Natural(result_str)
        
        # Убираем возможные ведущие нули
        while len(result.num) > 1 and result.num[0] == 0:
            result.num = result.num[1:]
            
        return result

    #12. Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)
    def MOD_NN_N(self, other):
        if other.COM_NN_D(Natural('0')) == 0:
            raise ValueError('Деление на ноль невозможно!')

        # Вычисляем частное
        quotient = self.DIV_NN_N(other)
        
        # Вычисляем произведение quotient * other
        product = Natural('0')
        quotient_str = str(quotient)
        
        # Используем SUB_NDN_N для вычисления product = quotient * other
        for i, digit_char in enumerate(quotient_str):
            digit = int(digit_char)
            if digit > 0:
                temp = other.MUL_ND_N(digit)
                temp = temp.MUL_Nk_N(len(quotient_str) - i - 1)
                product = product.ADD_NN_N(temp)
        
        # Вычисляем остаток: self - product
        remainder = self.SUB_NDN_N(product, 1)
        
        return remainder

    #13. НОД натуральных чисел
    def GCF_NN_N(self, other):
        a = Natural(str(self))
        b = Natural(str(other))

        # Проверка на нули с использованием NZER_N_B
        if a.NZER_N_B() == "нет":
            return b
        if b.NZER_N_B() == "нет":
            return a


        while b.NZER_N_B() == "да": # используем алгоритм Евклида
            comparison = a.COM_NN_D(b) # сравниваем числа с помощью COM_NN_D
            if comparison == 1:  # a < b
                a, b = b, a  # меняем местами
            elif comparison == 0:  # a == b
                return a

            temp = a.MOD_NN_N(b) # вычисляем остаток
            a, b = b, temp

        return a

    #14. НОК натуральных чисел
    def LCM_NN_N(self, other):
        return self.MUL_NN_N(other).DIV_NN_N(self.GCF_NN_N(other))  #возвращаем произведение чисел, деленное на НОД

#Тесты
def tests_for_naturales():
    num1 = Natural("2")
    num2 = Natural("23")
    num3 = Natural("1000")
    num4 = Natural("345")
    num5 = Natural("0")
    num6 = Natural("52")
    num7 = Natural("7")

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА NATURAL")
    print("=" * 60)

    # Тест 1: COM_NN_D - сравнение чисел
    print("\n1. ТЕСТИРОВАНИЕ СРАВНЕНИЯ (COM_NN_D):")
    print(f"   {num1} сравнить с {num2}: {num1.COM_NN_D(num2)}")  # 1 (2 < 23)
    print(f"   {num4} сравнить с {num6}: {num4.COM_NN_D(num6)}")  # 2 (345 > 52)
    print(f"   {num5} сравнить с {num5}: {num5.COM_NN_D(num5)}")  # 0 (0 == 0)

    # Тест 2: NZER_N_B - проверка на ноль
    print("\n2. ТЕСТИРОВАНИЕ ПРОВЕРКИ НА НОЛЬ (NZER_N_B):")
    print(f"   Число {num1} не равно нулю? {num1.NZER_N_B()}")  # да
    print(f"   Число {num5} не равно нулю? {num5.NZER_N_B()}")  # нет
    print(f"   Число {num6} не равно нулю? {num6.NZER_N_B()}")  # да

    # Тест 3: ADD_1N_N - добавление 1
    print("\n3. ТЕСТИРОВАНИЕ ДОБАВЛЕНИЯ 1 (ADD_1N_N):")
    print(f"   {num1} + 1 = {num1.ADD_1N_N()}")  # 3
    print(f"   {num5} + 1 = {num5.ADD_1N_N()}")  # 1
    print(f"   {num4} + 1 = {num4.ADD_1N_N()}")  # 346

    # Тест 4: ADD_NN_N - сложение
    print("\n4. ТЕСТИРОВАНИЕ СЛОЖЕНИЯ (ADD_NN_N):")
    print(f"   {num1} + {num2} = {num1.ADD_NN_N(num2)}")  # 25
    print(f"   {num3} + {num4} = {num3.ADD_NN_N(num4)}")  # 1345

    # Тест 5: SUB_NN_N - вычитание
    print("\n5. ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ (SUB_NN_N):")
    print(f"   {num2} - {num1} = {num2.SUB_NN_N(num1)}")  # 21
    print(f"   {num4} - {num2} = {num4.SUB_NN_N(num2)}")  # 322
    print(f"   {num7} - {num1} = {num7.SUB_NN_N(num1)}")  # 5

    # Тест 6: MUL_ND_N - умножение на цифру
    print("\n6. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ НА ЦИФРУ (MUL_ND_N):")
    print(f"   {num1} * 5 = {num1.MUL_ND_N(5)}")  # 10
    print(f"   {num4} * 3 = {num4.MUL_ND_N(3)}")  # 1035


    # Тест 7: MUL_Nk_N - умножение на 10^k
    print("\n7. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ НА 10^k (MUL_Nk_N):")
    print(f"   {num1} * 10^2 = {num1.MUL_Nk_N(2)}")  # 200
    print(f"   {num7} * 10^3 = {num7.MUL_Nk_N(3)}")  # 7000

    # Тест 8: MUL_NN_N - умножение чисел
    print("\n8. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ ЧИСЕЛ (MUL_NN_N):")
    print(f"   {num6} * {num2} = {num6.MUL_NN_N(num2)}")  # 1196
    print(f"   {num4} * {num4} = {num4.MUL_NN_N(num4)}")  # 119025


    # Тест 9: SUB_NDN_N - вычитание умноженного числа
    print("\n9. ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ УМНОЖЕННОГО ЧИСЛА (SUB_NDN_N):")
    print(f"   {num4} - ({num2} * 2) = {num4.SUB_NDN_N(num2, 2)}")  # 345 - 46 = 299
    print(f"   {num3} - ({num1} * 5) = {num3.SUB_NDN_N(num1, 5)}")  # 1000 - 10 = 990
    print(f"   {num7} - ({num1} * 3) = {num7.SUB_NDN_N(num1, 3)}")  # 7 - 6 = 1

    # Тест 10: DIV_NN_Dk - нахождение цифры частного
    print("\n10. ТЕСТИРОВАНИЕ НАХОЖДЕНИЯ ЦИФРЫ ЧАСТНОГО (DIV_NN_Dk):")
    print(f"   {num4} / {num6}, цифра на позиции 0: {num4.DIV_NN_Dk(num6, 0)}")  
    print(f"   {num3} / {num4}, цифра на позиции 0: {num3.DIV_NN_Dk(num4, 0)}")  

    # Тест 11: DIV_NN_N - деление чисел
    print("\n11. ТЕСТИРОВАНИЕ ДЕЛЕНИЯ ЧИСЕЛ (DIV_NN_N):")
    print(f"   {num3} / {num2} = {num3.DIV_NN_N(num2)}")  # 1000 / 23 = 43
    print(f"   {num4} / {num1} = {num4.DIV_NN_N(num1)}")  # 345 / 2 = 172

    # Тест 12: MOD_NN_N - остаток от деления
    print("\n12. ТЕСТИРОВАНИЕ ОСТАТКА ОТ ДЕЛЕНИЯ (MOD_NN_N):")
    print(f"   {num3} % {num2} = {num3.MOD_NN_N(num2)}")  # 1000 % 23 = 11
    print(f"   {num4} % {num1} = {num4.MOD_NN_N(num1)}")  # 345 % 2 = 1
    # Тест 13: GCF_NN_N - наибольший общий делитель
    print("\n13. ТЕСТИРОВАНИЕ НАИБОЛЬШЕГО ОБЩЕГО ДЕЛИТЕЛЯ (GCF_NN_N):")
    print(f"   НОД({num3}, {num4}) = {num3.GCF_NN_N(num4)}")  # НОД(1000, 345) = 5
    print(f"   НОД({num2}, {num4}) = {num2.GCF_NN_N(num4)}")  # НОД(23, 345) = 23

    # Тест 14: LCM_NN_N - наименьшее общее кратное
    print("\n14. ТЕСТИРОВАНИЕ НАИМЕНЬШЕГО ОБЩЕГО КРАТНОГО (LCM_NN_N):")
    print(f"   НОК({num1}, {num2}) = {num1.LCM_NN_N(num2)}")  # НОК(2, 23) = 46
    print(f"   НОК({num2}, {num4}) = {num2.LCM_NN_N(num4)}")  # НОК(23, 345) = 345


tests_for_naturales()


