# выполнили Сморыго Ю., гр. 4384 и Зайченко Е., гр. 4384

from Natural import Natural
from Integer import Integer

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

# Тесты
def Rational_tests():
    print('БАЗОВАЯ ПРОВЕРКА РАЦИОНАЛЬНЫХ ЧИСЕЛ:')
    x = Rational('8/6')      # = 4/3 после сокращения
    y = Rational('-9/3')     # = -3 (целое!)
    z = Integer('12')
    q = Rational('-9/1')
    
    # 1. Сокращение дроби
    print("ПРОВЕРКА СОКРАЩЕНИЯ ДРОБИ")
    print(f'{x} = {x.RED_Q_Q()}')          # RED_Q_Q = 4/3
    print(f'{y} = {y.RED_Q_Q()}')          # RED_Q_Q = -3
    print(f'{Rational("15/25")} = {Rational("15/25").RED_Q_Q()}')  # 3/5
    print(f'{Rational("-18/12")} = {Rational("-18/12").RED_Q_Q()}\n')  # -3/2

    # 2. Проверка сокращенного дробного на целое
    print("ПРОВЕРКА ДРОБИ НА ЦЕЛОЕ")
    print(f'{x} целое? {x.INT_Q_B()}')   # False
    print(f'{y} целое? {y.INT_Q_B()}')   # True
    print(f'{Rational("7/1")} целое? {Rational("7/1").INT_Q_B()}')  # True
    print(f'{Rational("5/2")} целое? {Rational("5/2").INT_Q_B()}\n')  # False

    # 3. Преобразование целого в дробное
    print("ПРЕОБРАЗОВАНИЕ ЦЕЛОГО В ДРОБНОЕ")
    print(f'Integer({z}) → Rational({Rational.TRANS_Z_Q(z)})')  # 12 = 12/1
    print(f'Integer(-5) → Rational({Rational.TRANS_Z_Q(Integer("-5"))})')  # -5 = -5/1
    print(f'Integer(0) → Rational({Rational.TRANS_Z_Q(Integer("0"))})')  # 0 = 0/1
    print(f'Integer(100) → Rational({Rational.TRANS_Z_Q(Integer("100"))})\n')  # 100 = 100/1
          
    # 4. Преобразование сокращенного дробного в целое
    print("ПРЕОБРАЗОВАНИЕ ДРОБНОГО В ЦЕЛОЕ")
    print(f'Rational({q}) → Integer({q.TRANS_Q_Z()})')  # -9 = -9
    print(f'Rational("7/1") → Integer({Rational("7/1").TRANS_Q_Z()})')  # 7
    print(f'Rational("0/1") → Integer({Rational("0/1").TRANS_Q_Z()})')  # 0
    try:
        print(f'4.4 Rational("3/2") → Integer({Rational("3/2").TRANS_Q_Z()})\n')  # Ошибка
    except ValueError as e:
        print(f'4.4 Rational("3/2") → Ошибка: {e}\n')

    a = Rational('1/2')
    b = Rational('1/3')
    c = Rational('-2/5')
    d = Rational('3/4')

    # 5. Сложение дробей
    print("СЛОЖЕНИЕ ДРОБЕЙ")
    print(f'{a} + {b} = {a.ADD_QQ_Q(b)}')  # 5/6
    print(f'{a} + {c} = {a.ADD_QQ_Q(c)}')  # 1/10
    print(f'{c} + {d} = {c.ADD_QQ_Q(d)}')  # 7/20
    print(f'{Rational("2/6")} + {Rational("1/6")} = {Rational("2/6").ADD_QQ_Q(Rational("1/6"))}\n')  # 5/6
          
    # 6. Вычитание дробей
    print("ВЫЧИТАНИЕ ДРОБЕЙ")
    print(f'{a} - {b} = {a.SUB_QQ_Q(b)}')  # 1/6
    print(f'{a} - {c} = {a.SUB_QQ_Q(c)}')  # 9/10
    print(f'{c} - {d} = {c.SUB_QQ_Q(d)}')  # -23/20
    print(f'{Rational("5/8")} - {Rational("1/8")} = {Rational("5/8").SUB_QQ_Q(Rational("1/8"))}\n')  # 3/8
    
    # 7. Умножение дробей
    print("УМНОЖЕНИЕ ДРОБЕЙ")
    print(f'{a} ∙ {b} = {a.MUL_QQ_Q(b)}')  # 1/6
    print(f'{a} ∙ {c} = {a.MUL_QQ_Q(c)}')  # -1/5
    print(f'{c} ∙ {d} = {c.MUL_QQ_Q(d)}')  # -3/10
    print(f'{Rational("3/4")} ∙ {Rational("2/3")} = {Rational("3/4").MUL_QQ_Q(Rational("2/3"))}\n')  # 1/2

    # 8. Деление дробей (вторая дробь не равна 0)
    print("ДЕЛЕНИЕ ДРОБЕЙ")
    print(f'{a} / {b} = {a.DIV_QQ_Q(b)}')  # 3/2
    print(f'{a} / {c} = {a.DIV_QQ_Q(c)}')  # -5/4
    print(f'{c} / {d} = {c.DIV_QQ_Q(d)}')  # -8/15
    print(f'{Rational("14/16")} / {Rational("1/4")} = {Rational("14/16").DIV_QQ_Q(Rational("1/4"))}')  # 3/2

Rational_tests()
