#выполнили Мазеев В., гр. 4384, Калинина А., гр. 4384 и Дровнев Д., гр. 4384
from __future__ import annotations
from Rational import Rational
from Integer import Integer
from Natural import Natural



class Polynomial:
    def __init__(self, polynomial: str):
        self.numbers = polynomial.split()
        self.coefficients = [Rational(coefficient) for coefficient in polynomial.split()]
        self._remove_leading_zeros()

    def _remove_leading_zeros(self):
        while len(self.coefficients) > 1 and self.coefficients[-1].is_zero():
            self.coefficients.pop()
    
    def _poly_clone(self):
        """Создать независимую копию полинома self."""
        p = Polynomial('0')
        p.coefficients = [Rational(str(c)) for c in self.coefficients]
        p._remove_leading_zeros()
        return p

    def __str__(self):
        terms = []
        for power, coeff in enumerate(self.coefficients):
            if coeff.numerator.POZ_Z_D() != 0:  # Пропускаем нулевые коэффициенты
                coeff_str = str(coeff.numerator) if coeff.denominator.COM_NN_D(Natural('1')) == 0 else str(coeff)

                if power == 0:
                    terms.append(coeff_str)
                elif power == 1:
                    if coeff_str == "1":
                        terms.append("x")
                    elif coeff_str == "-1":
                        terms.append("-x")
                    else:
                        terms.append(f"{coeff_str}*x")
                else:
                    if coeff_str == "1":
                        terms.append(f"x^{power}")
                    elif coeff_str == "-1":
                        terms.append(f"-x^{power}")
                    else:
                        terms.append(f"{coeff_str}*x^{power}")

        if not terms:
            return "0"

        return " + ".join(terms).replace(" + -", " - ") 



    # P-1: Сложение многочленов
    def ADD_PP_P(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result_coeffs = []

        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else Rational('0')
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else Rational('0')
            result_coeffs.append(coeff1.ADD_QQ_Q(coeff2))

        return Polynomial(' '.join(str(coef) for coef in result_coeffs))

    # P-2: Вычитание многочленов
    def SUB_PP_P(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result_coeffs = []

        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else Rational('0')
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else Rational('0')
            result_coeffs.append(coeff1.SUB_QQ_Q(coeff2))

        return Polynomial(' '.join(str(coef) for coef in result_coeffs))

    # P-3: Умножение многочлена на рациональное число
    def MUL_PQ_P(self, rational_num):
        result_coeffs = [coeff.MUL_QQ_Q(rational_num) for coeff in self.coefficients]
        return Polynomial(' '.join(str(coef) for coef in result_coeffs))

    # P-4: Умножение многочлена на x^k, k-натуральное или 0
    # Умножение многочлена x^k, где k - натуральное или 0
    def MUL_Pxk_P(self, k):
        # Создаем новый список коэффициентов с k нулями в начале
        new_coeffs = [Rational('0') for _ in range(int((str(k))))] + self.coefficients

        result_poly = Polynomial('0')
        result_poly.coefficients = new_coeffs
        result_poly._remove_leading_zeros()
        return result_poly
    # P-5:Старший коэффициент многочлена
    def LED_P_Q(self):
        if not self.coefficients:
            return Rational('0')

        # Возвращаем старший коэффициент
        return self.coefficients[-1]

    # P-6 : Степень многочлена
    def DEG_P_N(self):
        if not self.coefficients:
            return Natural('0')

        # Проверка на нулевой многочлен
        if len(self.coefficients) == 1 and self.coefficients[0].numerator.POZ_Z_D() == 0:
            return Natural('0')

        return Natural(str(len(self.coefficients) - 1))

    # P-7: Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def FAC_P_Q(self):
        """Вынесение из многочлена НОК знаменателей и НОД числителей"""
        # Отфильтруем нулевые коэффициенты
        valid_coefs = [coef for coef in self.coefficients if coef.numerator.POZ_Z_D() != 0]
        if not valid_coefs:
            return Rational('1/1')

        #Получаем натуральные числители и знаменатели
        numerators_N = [Integer(str(coef.numerator.ABS_Z_N())).TRANS_Z_N() for coef in valid_coefs]
        denominators_N = [coef.denominator for coef in valid_coefs]

        #Находим НОД числителей
        gcd_num = numerators_N[0]
        for i in range(1, len(numerators_N)):
            gcd_num = gcd_num.GCF_NN_N(numerators_N[i])

        #Находим НОК знаменателей
        lcm_den = denominators_N[0]
        for i in range(1, len(denominators_N)):
            lcm_den = lcm_den.LCM_NN_N(denominators_N[i])

        #Преобразуем обратно: НОД -> целое, НОК -> целое
        gcd_num_Z = Integer.TRANS_N_Z(gcd_num)
        lcm_den_Z = Integer.TRANS_N_Z(lcm_den)

        remainder_N = gcd_num.MOD_NN_N(lcm_den)
        # Это даст целую часть деления, если g < l — результат будет 0
        quotient_Z = gcd_num_Z.DIV_ZZ_Z(lcm_den_Z)
        if remainder_N.NZER_N_B() == 'да':  # остаток != 0
            # возвращаем честное рациональное число gcd_num / lcm_den
            return Rational(f"{gcd_num_Z}/{lcm_den_Z}")
        else:
            # делится нацело, возвращаем целое, приведённое к рациональному виду
            return Rational(f"{quotient_Z}/1")

    # P-8: Умножение многочленов
    def MUL_PP_P(self, other: Polynomial) -> Polynomial:
        """P-8: Умножение многочленов"""
        # Инициализируем нулевой многочлен
        result_poly = Polynomial('0')
        # Степень второго многочлена
        deg_Q = int(str(other.DEG_P_N()))
        for i in range(deg_Q + 1):
            # Текущий коэффициент из второго многочлена
            coef_i = other.coefficients[i]
            # (1) Умножаем первый многочлен на этот коэффициент (рациональное число)
            temp_poly = self.MUL_PQ_P(coef_i)
            # (2) Умножаем на x^i
            temp_poly = temp_poly.MUL_Pxk_P(Natural(str(i)))
            # (3) Добавляем к общему результату
            result_poly = result_poly.ADD_PP_P(temp_poly)

        return result_poly

    # P-9: Частное от деления многочлена на многочлен при делении с остатком
    def DIV_PP_P(self, other: Polynomial) -> Polynomial:
        """Частное от деления многочлена на многочлен"""
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")

        A = self._poly_clone()
        B = other._poly_clone()
        Q = Polynomial('0')

        while not A.is_zero() and A.DEG_P_N().COM_NN_D(B.DEG_P_N()) != 1:  # deg(A) >= deg(B)
            deg_diff = int(str(A.DEG_P_N().SUB_NN_N(B.DEG_P_N())))
            lead_A = A.coefficients[-1]
            lead_B = B.coefficients[-1]
            q = Rational.DIV_QQ_Q(lead_A, lead_B)

            term = Polynomial(str(q)).MUL_Pxk_P(Natural(str(deg_diff)))
            Q = Q.ADD_PP_P(term)
            A = A.SUB_PP_P(B.MUL_PP_P(term))
            A._remove_leading_zeros()

        return Q
    # P-10: Остаток от деления многочлена на многочлен при делении с остатком.    
    def MOD_PP_P(self, other: Polynomial) -> Polynomial:

        # Проверка делителя на ноль
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")

        # Если делимое меньше делителя — остаток = делимое
        if self.DEG_P_N().COM_NN_D(other.DEG_P_N()) == 1:  # self < other
            return self._poly_clone()

        # Получаем частное
        quotient = self.DIV_PP_P(other)

        # Вычисляем остаток: remainder = self - (other * quotient)
        remainder = self.SUB_PP_P(other.MUL_PP_P(quotient))

        remainder._remove_leading_zeros()

        return remainder


    def is_zero(self):
        self._remove_leading_zeros()
        return all(c.is_zero() for c in self.coefficients)
        
    # P-11: НОД многочленов
    def GCF_PP_P(self, other):
        # Создаем копии
        a = Polynomial('0')
        a.coefficients = self.coefficients.copy()
        b = Polynomial('0')
        b.coefficients = other.coefficients.copy()

        a._remove_leading_zeros()
        b._remove_leading_zeros()

        zero_check = Natural('0')

        # Если b - нулевой многочлен
        if b.is_zero():
            return a

        while not b.is_zero():
            remainder = a.MOD_PP_P(b)
            a, b = b, remainder
            a._remove_leading_zeros()
            b._remove_leading_zeros()

        gcd_poly = a

        # Если степень 0 (константа), просто вернуть 1
        if gcd_poly.DEG_P_N().COM_NN_D(zero_check) == 0:
            one = Polynomial('1')
            return one

        # Нормализация
        lead_coef = gcd_poly.LED_P_Q()
        normalized_coeffs = [coeff.DIV_QQ_Q(lead_coef) for coeff in gcd_poly.coefficients]

        result_poly = Polynomial('0')
        result_poly.coefficients = normalized_coeffs
        result_poly._remove_leading_zeros()
        return result_poly



    # P-12: Производная многочлена
    def DER_P_P(self):
        # Проверяем, является ли многочлен константой или пустым
        # Производная константы всегда равна 0
        if len(self.coefficients) <= 1:
            return Polynomial('0')

        # Создаем пустой список для коэффициентов производной
        derivative_coeffs = []

        # Проходим по всем коэффициентам, начиная с первого (пропускаем свободный член)
        # i = 1 соответствует коэффициенту при x^1, i = 2 при x^2 и т.д.
        for i in range(1, len(self.coefficients)):
            # Создаем рациональное число, равное текущей степени i
            # Это множитель по правилу: (a*x^i)' = i*a*x^(i-1)
            multiplier = Rational(f"{i}/1")

            # Умножаем исходный коэффициент на степень i
            # Получаем новый коэффициент для производной
            new_coeff = self.coefficients[i].MUL_QQ_Q(multiplier)

            # Добавляем полученный коэффициент в список производной
            derivative_coeffs.append(new_coeff)

        # Создаем новый многочлен из вычисленных коэффициентов производной
        return Polynomial(' '.join(str(coef) for coef in derivative_coeffs))

    # P-13: Преобразование многочлена - кратные корни в простые
    def NMR_P_P(self):
        # Шаг 1: Находим производную исходного многочлена
        # Производная нужна для поиска кратных корней
        derivative = self.DER_P_P()

        # Шаг 2: Находим НОД исходного многочлена и его производной
        # Если есть кратные корни, они будут в этом НОДе
        gcd_poly = self.GCF_PP_P(derivative)

        # Шаг 3: Проверяем, является ли НОД константой (многочленом степени 0)
        # Если НОД - константа, значит кратных корней нет
        if gcd_poly.DEG_P_N().COM_NN_D(Natural('0')) == 0:
            # Возвращаем исходный многочлен без изменений
            return Polynomial(' '.join(str(coef) for coef in self.coefficients))

        # Шаг 4: Делим исходный многочлен на найденный НОД
        # Это убирает кратные корни, оставляя только простые
        return self.DIV_PP_P(gcd_poly)

if __name__ == "__main__":
    # Тестики (базовая демонстрация работы)
    print('Базовая проверка многочленов:')
    x = Polynomial('2 1/2 4 -3 1')
    y = Polynomial('1 1 22 2 2 2 -2/5')
    z = Rational('2')
    k = Natural('3')
    print(f'({x}) + ({y})  =  {Polynomial.ADD_PP_P(x, y)}')  # ADD_PP_P
    print(f'({x}) - ({y})  =  {Polynomial.SUB_PP_P(x, y)}')  # SUB_PP_P
    print(f'({x}) ∙ {z}  =  {Polynomial.MUL_PQ_P(x, z)}')  # MUL_PQ_P
    print(f'({x}) ∙ x^{k}  =  {Polynomial.MUL_Pxk_P(x, k)}')  # MUL_Pxk_P
    print(f'Старший коэффициент {x}  =  {Polynomial.LED_P_Q(x)}')  # LED_P_Q
    print(f'DEG {x} = {Polynomial.DEG_P_N(x)}')  # DEG_P_N
    print(f'НОД/НОК {x}  =  {Polynomial.FAC_P_Q(x)}')  # FAC_P_Q
    print(f'({x}) ∙ ({y})  =  {Polynomial.MUL_PP_P(x, y)}')  # MUL_PP_P
    print(f'({x}) // ({y})  =  {Polynomial.DIV_PP_P(x, y)}')  # DIV_PP_P
    print(f'{x}  %  {y}  =  {Polynomial.MOD_PP_P(x, y)}')       # MOD_PP_P
    print(f'НОД  ({x};  {y})  =  {Polynomial.GCF_PP_P(y, x)}')  # GCF_PP_P
    print(f'Производная {x}  =  {Polynomial.DER_P_P(x)}')  # DER_P_P
    print(f'NMP ({x})  =  {Polynomial.NMR_P_P(x)}')             # NMR_P_P
