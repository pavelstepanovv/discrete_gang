from __future__ import annotations
from MODULES.Rational import Rational
from MODULES.Integer import Integer
from MODULES.Natural import Natural



class Polynomial:
    def __init__(self, polynomial: str):
        self.numbers = polynomial.split()
        self.coefficients = [Rational(coefficient) for coefficient in polynomial.split()]
        self._remove_leading_zeros()

    def _remove_leading_zeros(self):
        while len(self.coefficients) > 1 and self.coefficients[-1].numerator.POZ_Z_D() == 0:
            self.coefficients = self.coefficients[:-1]

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
        """Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей"""
        numerators = [coef.numerator.ABS_Z_N() for coef in self.coefficients if coef.numerator.POZ_Z_D()]
        denominators = [coef.denominator for coef in self.coefficients if coef.numerator.POZ_Z_D()]
        if len(numerators) == 0: return Rational('1/1')

        for i in range(1,len(numerators)):
            for j in range(len(numerators) - i):
                numerators[j] = numerators[j].GCF_NN_N(numerators[j + 1])
                denominators[j] = denominators[j].LCM_NN_N(denominators[j + 1])
        return Rational(f'{numerators[0]}/{denominators[0]}')

    # P-8: Умножение многочленов
    def MUL_PP_P(self, other : Polynomial) -> Polynomial:
        """Умножение многочленов"""
        n = len(self.coefficients)
        m = len(other.coefficients)
        result = [Rational('0') for _ in range(n + m - 1)]
        for i in range(n):
            for j in range(m):
                result[i + j] = Rational.ADD_QQ_Q(result[i + j],Rational.MUL_QQ_Q(self.coefficients[i], other.coefficients[j]))
        new_poly = Polynomial(" ".join(str(c) for c in result))
        return new_poly

    # P-9: Частное от деления многочлена на многочлен при делении с остатком
    def DIV_PP_P(self, other : Polynomial) -> Polynomial:
        """Частное от деления многочлена на многочлен при делении с остатком"""
        dividend = self.coefficients.copy()
        divisor = other.coefficients.copy()

        if len(dividend) < len(divisor):
            return Polynomial("0")

        quotient = [Rational('0') for _ in range(len(dividend) - len(divisor) + 1)]

        while len(dividend) >= len(divisor):
            deg_diff = len(dividend) - len(divisor)
            lead_dividend = dividend[-1]
            lead_divisor = divisor[-1]
            q = Rational.DIV_QQ_Q(lead_dividend, lead_divisor)
            quotient[deg_diff] = q

            for i in range(len(divisor)):
                pos = i + deg_diff
                prod = Rational.MUL_QQ_Q(divisor[i], q)
                dividend[pos] = Rational.SUB_QQ_Q(dividend[pos], prod)

            while len(dividend) > 1 and dividend[-1].numerator.POZ_Z_D() == 0:
                dividend.pop()

            if len(dividend) < len(divisor):
                break

        return Polynomial(" ".join(str(c) for c in quotient))
    
    # P-10: Остаток от деления многочлена на многочлен при делении с остатком
    def MOD_PP_P(self, other):
        """Остаток от деления многочлена на многочлен."""
        dividend = self.coefficients.copy()
        divisor = other.coefficients.copy()

        # Если степень делимого меньше делителя
        if len(dividend) < len(divisor):
            result = Polynomial('0')
            result.coefficients = dividend
            result._remove_leading_zeros()
            return result

        # Основной цикл деления
        while len(dividend) >= len(divisor):
            deg_diff = len(dividend) - len(divisor)
            lead_dividend = dividend[-1]
            lead_divisor = divisor[-1]

            # Частное от деления старших коэффициентов
            q = Rational.DIV_QQ_Q(lead_dividend, lead_divisor)

            # Вычитаем q * (divisor * x^deg_diff) из dividend
            for i in range(len(divisor)):
                pos = i + deg_diff
                prod = Rational.MUL_QQ_Q(divisor[i], q)
                dividend[pos] = Rational.SUB_QQ_Q(dividend[pos], prod)

            # Удаляем "нулевые" коэффициенты с конца (с нормализацией)
            while len(dividend) > 0 and dividend[-1].is_zero():
                dividend.pop()

            if len(dividend) < len(divisor):
                break

        # Создаём результат
        remainder = Polynomial('0')
        remainder.coefficients = dividend if dividend else [Rational('0')]
        remainder._remove_leading_zeros()
        return remainder

    def is_zero(self):
        self._remove_leading_zeros()
        return all(c.is_zero() for c in self.coefficients)
    # P-11: НОД многочленов
    # НОД многочленов
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