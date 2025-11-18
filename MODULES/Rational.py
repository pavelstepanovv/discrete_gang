# выполнили Сморыго Ю., гр. 4384 и Зайченко Е., гр. 4384

from Natural import Natural
from Integer import Integer


class Rational:

    '''
    Рациональное число — пара (числитель: целое, знаменатель: натуральное ≥ 1).
    Знак хранится только в числителе.
    '''

    def __init__(self, number: str):
        s = number.replace('|', '/').replace(':', '/') # единое оформление числа

        # приведение к единому разделителю
        if '/' in s:
            num_str, den_str = s.split('/', 1)
        else:
            num_str, den_str = s, '1'

        self.numerator = Integer(num_str)

        if self.numerator.POZ_Z_D() != 0:  # если числитель не равен 0, оставляем знаменатель
            self.denominator = Natural(den_str)
        else:                               # если числитель равен 0, приравниваем знаменатель к 1
            self.denominator = Natural('1')

    # представление числа в виде строки
    def __str__(self):
        if Natural.COM_NN_D(self.denominator, Natural('1')) == 0:
            return str(self.numerator)
        return f'{self.numerator}/{self.denominator}'
        
    def is_zero(self):
        return self.numerator.POZ_Z_D() == 0

    #1. Сокращение дроби
    def RED_Q_Q(self):
        if self.numerator.POZ_Z_D() == 0: # если числитель равен нулю - всё число равно нулю
            return Rational('0')
        abs_num = self.numerator.ABS_Z_N() # модуль числителя
        nod = self.denominator.GCF_NN_N(abs_num) # НОД натурального(!) числителя и знаменателя

        # новый числитель - целое число
        new_num = self.numerator.DIV_ZZ_Z(Integer.TRANS_N_Z(nod))
        # новый знаменатель - натуральное число
        new_den = self.denominator.DIV_NN_N(nod)

        return Rational(f'{new_num}/{new_den}')

    #2. Проверка сокращенного дробного на целое, если рациональное число является целым, то «да», иначе «нет»
    def INT_Q_B(self):
        # Находим НОД модуля числителя и знаменателя
        p = self.denominator.GCF_NN_N(self.numerator.ABS_Z_N())

        # Число целое, если числитель равен нулю
        # или если знаменатель и НОД равны (знаменатель полностью делится на числитель)
        if self.numerator.POZ_Z_D() == 0 or self.denominator.COM_NN_D(p) == 0:
            return 'да'
        else:
            return 'нет'

    #3. Преобразование целого в дробное
    @staticmethod
    def TRANS_Z_Q(number: Integer):
        return Rational(f'{number}/1')

    #4. Преобразование сокращенного дробного в целое (если знаменатель равен 1)
    def TRANS_Q_Z(self):
        # Проверяем, равен ли знаменатель 1
        if Natural.COM_NN_D(self.denominator, Natural('1')) == 0:
            # Возвращаем числитель как целое число
            return Integer(str(self.numerator))
        else:
            # Если знаменатель не равен 1 — преобразование невозможно
            raise ValueError("Невозможно преобразовать: знаменатель не равен 1")

    #5. Сложение дробей
    def ADD_QQ_Q(self, other):

        nok = self.denominator.LCM_NN_N(other.denominator) # НОК знаменателей двух дробей

        # значение на которое нужно домножить числитель
        val1 = nok.DIV_NN_N(self.denominator)
        val2 = nok.DIV_NN_N(other.denominator)

        # новый числитель - целое число = числитель изначальной дроби умножить на val1/val2
        num1 = Integer.MUL_ZZ_Z(self.numerator, Integer.TRANS_N_Z(val1))
        num2 = Integer.MUL_ZZ_Z(other.numerator, Integer.TRANS_N_Z(val2))

        new_numerator = Integer.ADD_ZZ_Z(num1, num2)

        # новый знаменатель = нок
        result = Rational(f'{new_numerator}/{nok}')

        # сокращение полученной дроби
        return result.RED_Q_Q()

    #6. Вычитание дробей
    def SUB_QQ_Q(self, other):
        # Находим НОК знаменателей
        common_den = self.denominator.LCM_NN_N(other.denominator)
        # Приводим обе дроби к общему знаменателю:
        k1 = common_den.DIV_NN_N(self.denominator)
        k2 = common_den.DIV_NN_N(other.denominator)

        num1_scaled = Integer.MUL_ZZ_Z(self.numerator, Integer.TRANS_N_Z(k1))
        num2_scaled = Integer.MUL_ZZ_Z(other.numerator, Integer.TRANS_N_Z(k2))

        # Вычитаем числители
        new_num = Integer.SUB_ZZ_Z(num1_scaled, num2_scaled)

        # Создаем новую дробь
        result = Rational(f'{new_num}/{common_den}')
        
        # Сокращаем полученную дробь
        return result.RED_Q_Q()

    #7. Умножение дробей
    def MUL_QQ_Q(self, other):

        # получение нового числителя и знаменателя
        num = Integer.MUL_ZZ_Z(self.numerator, other.numerator)
        det = Natural.MUL_NN_N(self.denominator, other.denominator)

        result = Rational(f'{num}/{det}')

        # сокращение полученной дроби
        return result.RED_Q_Q()

    #8. Деление дробей (делитель отличен от нуля)
    def DIV_QQ_Q(self, other):
        # Проверяем, что делитель не равен нулю
        if other.numerator.POZ_Z_D() == 0:
            raise ValueError("Деление на ноль невозможно!")

        # Переворачиваем делитель (меняем местами числитель и знаменатель)
        new_num = Integer.TRANS_N_Z(other.denominator)  # знаменатель -> числитель
        new_den = other.numerator.ABS_Z_N()             # модуль числителя -> знаменатель (натуральное)
        new_den_int = Integer.TRANS_N_Z(new_den)

        # Если числитель делителя отрицательный, переносим знак
        if other.numerator.POZ_Z_D() == 1:
            new_num = Integer.MUL_ZM_Z(new_num)

        # Создаём перевёрнутую дробь
        reciprocal = Rational(f'{new_num}/{new_den_int}')

        # Возвращаем произведение исходной дроби и перевёрнутой (через MUL_ZZ_Z внутри MUL_QQ_Q)
        return self.MUL_QQ_Q(reciprocal)

# Тестирование
if __name__ == "__main__":
    print('Базовая проверка рациональных:')
    x = Rational('8/6')      # = 4/3 после сокращения
    y = Rational('-9/3')     # = -3 (целое!)
    z = Integer('12')
    q = Rational('-9/1')
    
    print(f'{x} = {x.RED_Q_Q()}')          # RED_Q_Q = 4/3
    print(f'{y} = {y.RED_Q_Q()}')          # RED_Q_Q = -3

    print(f'{x} is int = {x.INT_Q_B()}')   # False
    print(f'{y} is int = {y.INT_Q_B()}')   # True

    print(f'Integer({z}) → Rational({Rational.TRANS_Z_Q(z)})')  # 12 = 12/1

    print(f'Rational({q}) → Integer({q.TRANS_Q_Z()})')  # -9 = -9

    a = Rational('1/2')
    b = Rational('1/3')

    print(f'{a} + {b} = {a.ADD_QQ_Q(b)}')  # 5/6
    print(f'{a} - {b} = {a.SUB_QQ_Q(b)}')  # 1/6
    print(f'{a} ∙ {b} = {a.MUL_QQ_Q(b)}')  # 1/6

    print(f'{a} / {b} = {a.DIV_QQ_Q(b)}')  # 3/2
