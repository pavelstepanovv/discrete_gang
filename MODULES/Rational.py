# выполнили Сморыго Ю., гр. 4384 и Зайченко Е., гр. 4384

from .Natural import Natural
from .Integer import Integer

'''
Рациональное число — пара (числитель: целое, знаменатель: натуральное ≥ 1).
Знак хранится только в числителе.
'''

class Rational:
    def __init__(self, number: str):
        # Приведение записи дроби к единому разделителю
        s = number.replace('|', '/').replace(':', '/')
        if '/' in s:
            num_str, den_str = s.split('/', 1)
        else:
            num_str, den_str = s, '1'

        self.numerator = Integer(num_str)

        # Если числитель не равен 0, оставляем знаменатель
        if self.numerator.POZ_Z_D() != 0:  
            self.denominator = Natural(den_str)
        # Иначе приравниваем знаменатель к 1
        else:
            self.denominator = Natural('1')

    # Представление числа в виде строки
    def __str__(self):
        if Natural.COM_NN_D(self.denominator, Natural('1')) == 0:
            return str(self.numerator)
        return f'{self.numerator}/{self.denominator}'
    
    # Проверка дроби на 0
    def is_zero(self):
        return self.numerator.POZ_Z_D() == 0

    #1. Сокращение дроби
    def RED_Q_Q(self):
        # Если числитель равен нулю, то вся дробь равна нулю
        # В этом случае возвращаем каноническое представление нуля
        if self.numerator.POZ_Z_D() == 0:
            return Rational('0')
        
        # Вычисляем абсолютное значение числителя (модуль),
        # это необходимо, так как НОД вычисляется для натуральных чисел
        abs_num = self.numerator.ABS_Z_N()
        
        # Находим НОД знаменателя и модуля числителя
        nod = self.denominator.GCF_NN_N(abs_num)
        
        # Делим числитель на НОД (новый числитель - целое число)
        new_num = self.numerator.DIV_ZZ_Z(Integer.TRANS_N_Z(nod))
        
        # Делим знаменатель на НОД (новый знаменатель - натуральное число)
        new_den = self.denominator.DIV_NN_N(nod)
        
        # Возвращаем новую сокращенную дробь
        # Знак сохраняется в числителе, знаменатель всегда положительный
        return Rational(f'{new_num}/{new_den}')

    #2. Проверка сокращенного дробного на целое, если рациональное число является целым, то «да», иначе «нет»
    def INT_Q_B(self):
        # Находим НОД знаменателя и модуля числителя
        # Это позволяет определить, можно ли сократить дробь до целого числа
        p = self.denominator.GCF_NN_N(self.numerator.ABS_Z_N())

        # Число является целым в двух случаях:
        # 1. Если числитель равен нулю (дробь равна нулю, что является целым числом)
        # 2. Если знаменатель равен НОДу (это означает, что знаменатель полностью делит числитель)
        if self.numerator.POZ_Z_D() == 0 or self.denominator.COM_NN_D(p) == 0:
            return 'да'
        else:
            return 'нет'

    #3. Преобразование целого в дробное
    @staticmethod
    def TRANS_Z_Q(number: Integer):
        # Любое целое число можно представить как дробь со знаменателем 1
        # Например: 5 = 5/1, -3 = -3/1, 0 = 0/1
        # Это каноническое представление целого числа в виде рационального
        return Rational(f'{number}/1')

    #4. Преобразование сокращенного дробного в целое (если знаменатель равен 1)
    def TRANS_Q_Z(self):
        # Если знаменатель равен 1, то дробь представляет собой целое число
        if Natural.COM_NN_D(self.denominator, Natural('1')) == 0:            
            # Возвращаем числитель как целое число (знак сохраняется в числителе)
            return Integer(str(self.numerator))
        # Иначе дробь не является целым числом
        else:
            # Преобразование невозможно, так как получилось бы дробное значение
            raise ValueError("Невозможно преобразовать: знаменатель не равен 1")

    #5. Сложение дробей
    def ADD_QQ_Q(self, other):
        # Находим НОК знаменателей обеих дробей
        # Это будет общий знаменатель для сложения дробей
        nok = self.denominator.LCM_NN_N(other.denominator)
        
        # Вычисляем множители для приведения дробей к общему знаменателю
        # Каждая дробь умножается на дополнительный множитель: НОК/знаменатель своей дроби
        val1 = nok.DIV_NN_N(self.denominator)  # множитель для первой дроби
        val2 = nok.DIV_NN_N(other.denominator)  # множитель для второй дроби
        
        # Умножаем каждый числитель на соответствующий множитель
        num1 = Integer.MUL_ZZ_Z(self.numerator, Integer.TRANS_N_Z(val1))
        num2 = Integer.MUL_ZZ_Z(other.numerator, Integer.TRANS_N_Z(val2))
        
        # Складываем числители приведенных дробей
        new_numerator = Integer.ADD_ZZ_Z(num1, num2)
        
        # Создаем новую дробь с общим знаменателем
        result = Rational(f'{new_numerator}/{nok}')
        
        # Сокращаем полученную дробь для канонического представления
        return result.RED_Q_Q()

    #6. Вычитание дробей
    def SUB_QQ_Q(self, other):
        # Находим НОК знаменателей обеих дробей
        # Это будет общий знаменатель для вычитания дробей
        common_den = self.denominator.LCM_NN_N(other.denominator)
        
        # Вычисляем множители для приведения дробей к общему знаменателю
        # Каждая дробь умножается на дополнительный множитель: НОК/знаменатель своей дроби
        k1 = common_den.DIV_NN_N(self.denominator)  # множитель для первой дроби (уменьшаемого)
        k2 = common_den.DIV_NN_N(other.denominator)  # множитель для второй дроби (вычитаемого)

        # Умножаем каждый числитель на соответствующий множитель
        num1_scaled = Integer.MUL_ZZ_Z(self.numerator, Integer.TRANS_N_Z(k1))
        num2_scaled = Integer.MUL_ZZ_Z(other.numerator, Integer.TRANS_N_Z(k2))
        
        # Вычитаем числители приведенных дробей
        # Из числителя первой дроби вычитаем числитель второй дроби
        new_num = Integer.SUB_ZZ_Z(num1_scaled, num2_scaled)
        
        # Создаем новую дробь с общим знаменателем
        result = Rational(f'{new_num}/{common_den}')
        
        # Сокращаем полученную дробь для канонического представления
        return result.RED_Q_Q()

    #7. Умножение дробей
    def MUL_QQ_Q(self, other):
        # Умножаем числители обеих дробей (результат - целое число)
        num = Integer.MUL_ZZ_Z(self.numerator, other.numerator)
        
        # Умножаем знаменатели обеих дробей (результат - натуральное число)
        det = Natural.MUL_NN_N(self.denominator, other.denominator)
        
        # Создаем новую дробь из произведения числителей и произведения знаменателей
        result = Rational(f'{num}/{det}')
        
        # Сокращаем полученную дробь для канонического представления
        return result.RED_Q_Q()

    #8. Деление дробей (делитель отличен от нуля)
    def DIV_QQ_Q(self, other):
        # Проверяем, что вторая дробь (делитель) не равна нулю
        if other.numerator.POZ_Z_D() == 0:
            raise ValueError("Деление на ноль невозможно!")

        # Переворачиваем вторую дробь (делитель): меняем местами числитель и знаменатель
        # Знаменатель второй дроби (делителя) становится числителем (преобразуем в целое число)
        new_num = Integer.TRANS_N_Z(other.denominator)
        # Модуль числителя делителя становится знаменателем (натуральное число)
        new_den = other.numerator.ABS_Z_N()
        new_den_int = Integer.TRANS_N_Z(new_den)
        # Если числитель второй дроби (делителя) был отрицательным, переносим знак
        # Это необходимо для сохранения правильного знака перевернутой дроби
        if other.numerator.POZ_Z_D() == 1:
            new_num = Integer.MUL_ZM_Z(new_num)

        # Создаём перевёрнутую дробь (обратную делителю)
        reciprocal = Rational(f'{new_num}/{new_den_int}')

        # Деление заменяем умножением на обратную дробь
        # Возвращаем произведение исходной дроби и перевёрнутой, 
        # Результат - сокращённая дробь (метод MUL_QQ_Q в конце сокращает дробь)
        return self.MUL_QQ_Q(reciprocal)

# Тестирование
def tests_for_rationals():
    # Создаем тестовые рациональные числа
    rat1 = Rational("1/2")           # 1/2
    rat2 = Rational("3/4")           # 3/4
    rat3 = Rational("-2/3")          # -2/3
    rat4 = Rational("5")             # 5/1
    rat5 = Rational("0")             # 0/1
    rat6 = Rational("6/8")           # 6/8 (несокращенная)
    rat7 = Rational("-9/3")          # -9/3 (несокращенная)
    rat8 = Rational("7/5")           # 7/5

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА RATIONAL")
    print("=" * 60)

    # Тест 1: RED_Q_Q - сокращение дроби
    print("\n1. ТЕСТИРОВАНИЕ СОКРАЩЕНИЯ ДРОБИ (RED_Q_Q):")
    print(f"   {rat1} = {rat1.RED_Q_Q()}")                    # 1/2 (без изменений)
    print(f"   {rat6} = {rat6.RED_Q_Q()}")                    # 3/4
    print(f"   {rat7} = {rat7.RED_Q_Q()}")                    # -3/1
    print(f"   {rat5} = {rat5.RED_Q_Q()}")                    # 0/1

    # Тест 2: INT_Q_B - проверка на целое число
    print("\n2. ТЕСТИРОВАНИЕ ПРОВЕРКИ НА ЦЕЛОЕ ЧИСЛО (INT_Q_B):")
    print(f"   {rat1} является целым? {rat1.INT_Q_B()}")      # нет
    print(f"   {rat4} является целым? {rat4.INT_Q_B()}")      # да
    print(f"   {rat5} является целым? {rat5.INT_Q_B()}")      # да
    print(f"   {rat7.RED_Q_Q()} является целым? {rat7.RED_Q_Q().INT_Q_B()}")  # да

    # Тест 3: TRANS_Z_Q - преобразование целого в дробное
    print("\n3. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ ЦЕЛОГО В ДРОБНОЕ (TRANS_Z_Q):")
    int1 = Integer("7")
    int2 = Integer("-4")
    int3 = Integer("0")
    print(f"   Integer({int1}) → Rational({Rational.TRANS_Z_Q(int1)})")  # 7/1
    print(f"   Integer({int2}) → Rational({Rational.TRANS_Z_Q(int2)})")  # -4/1
    print(f"   Integer({int3}) → Rational({Rational.TRANS_Z_Q(int3)})")  # 0/1

    # Тест 4: TRANS_Q_Z - преобразование дробного в целое
    print("\n4. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ ДРОБНОГО В ЦЕЛОЕ (TRANS_Q_Z):")
    print(f"   Rational({rat4}) → Integer({rat4.TRANS_Q_Z()})")          # 5
    print(f"   Rational({rat7.RED_Q_Q()}) → Integer({rat7.RED_Q_Q().TRANS_Q_Z()})")  # -3
    try:
        print(f"   Rational({rat1}) → Integer({rat1.TRANS_Q_Z()})")      # Ошибка
    except ValueError as e:
        print(f"   Rational({rat1}) → Ошибка: {e}")

    # Тест 5: ADD_QQ_Q - сложение дробей
    print("\n5. ТЕСТИРОВАНИЕ СЛОЖЕНИЯ ДРОБЕЙ (ADD_QQ_Q):")
    print(f"   {rat1} + {rat2} = {rat1.ADD_QQ_Q(rat2)}")      # 5/4
    print(f"   {rat1} + {rat3} = {rat1.ADD_QQ_Q(rat3)}")      # -1/6
    print(f"   {rat4} + {rat2} = {rat4.ADD_QQ_Q(rat2)}")      # 23/4
    print(f"   {rat5} + {rat1} = {rat5.ADD_QQ_Q(rat1)}")      # 1/2

    # Тест 6: SUB_QQ_Q - вычитание дробей
    print("\n6. ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ ДРОБЕЙ (SUB_QQ_Q):")
    print(f"   {rat2} - {rat1} = {rat2.SUB_QQ_Q(rat1)}")      # 1/4
    print(f"   {rat1} - {rat3} = {rat1.SUB_QQ_Q(rat3)}")      # 7/6
    print(f"   {rat4} - {rat2} = {rat4.SUB_QQ_Q(rat2)}")      # 17/4
    print(f"   {rat5} - {rat1} = {rat5.SUB_QQ_Q(rat1)}")      # -1/2

    # Тест 7: MUL_QQ_Q - умножение дробей
    print("\n7. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ ДРОБЕЙ (MUL_QQ_Q):")
    print(f"   {rat1} * {rat2} = {rat1.MUL_QQ_Q(rat2)}")      # 3/8
    print(f"   {rat1} * {rat3} = {rat1.MUL_QQ_Q(rat3)}")      # -1/3
    print(f"   {rat4} * {rat2} = {rat4.MUL_QQ_Q(rat2)}")      # 15/4
    print(f"   {rat5} * {rat1} = {rat5.MUL_QQ_Q(rat1)}")      # 0/1

    # Тест 8: DIV_QQ_Q - деление дробей
    print("\n8. ТЕСТИРОВАНИЕ ДЕЛЕНИЯ ДРОБЕЙ (DIV_QQ_Q):")
    print(f"   {rat1} / {rat2} = {rat1.DIV_QQ_Q(rat2)}")      # 2/3
    print(f"   {rat2} / {rat3} = {rat2.DIV_QQ_Q(rat3)}")      # -9/8
    print(f"   {rat4} / {rat1} = {rat4.DIV_QQ_Q(rat1)}")      # 10/1
    try:
        print(f"   {rat1} / {rat5} = {rat1.DIV_QQ_Q(rat5)}")  # Ошибка
    except ValueError as e:
        print(f"   {rat1} / {rat5} → Ошибка: {e}")

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ РАЦИОНАЛЬНЫХ ЧИСЕЛ ЗАВЕРШЕНО!")
    print("=" * 60)

tests_for_rationals()

