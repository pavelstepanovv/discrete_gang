# выполнили Мазеев В., гр. 4384, Калинина А., гр. 4384 и Дровнев Д., гр. 4384

from __future__ import annotations
from Rational import Rational
from Integer import Integer
from Natural import Natural


class Polynomial:
    
    '''
    Многочлен — представлен в виде словаря {степень: коэффициент},
    где коэффициент — рациональное число.
    '''

    def __init__(self, polynomial: str):
        # Инициализация многочлена из строкового представления
        self.terms = self._parse_polynomial(polynomial)
        self._remove_leading_zeros()  # Удаляем нулевые старшие коэффициенты
    
    def _parse_polynomial(self, poly_str: str) -> dict[int, Rational]:
        """Парсит строковое представление полинома в словарь {степень: коэффициент}"""
        terms = {}
        
        # Если полином нулевой
        if poly_str.strip() == '0':
            return {0: Rational('0')}
        
        import re
        # Регулярное выражение для поиска мономов (разделители + и -)
        monomials = re.findall(r'([+-]?[^-+]+)', poly_str.replace(' ', ''))
        
        for monomial in monomials:
            if not monomial or monomial == '+':
                continue
                
            # Обрабатываем знак
            if monomial.startswith('+'):
                monomial = monomial[1:]
            sign = 1
            if monomial.startswith('-'):
                sign = -1
                monomial = monomial[1:]
            
            # Парсим коэффициент и степень
            if 'x' not in monomial:
                # Свободный член (без x)
                coeff = Rational(monomial) if monomial else Rational('1')
                terms[0] = coeff.MUL_QQ_Q(Rational(f"{sign}/1"))
            else:
                # Есть переменная x
                parts = monomial.split('x')
                coeff_str = parts[0].replace('*', '') if parts[0] else '1'
                
                # Обрабатываем коэффициент
                if coeff_str == '' or coeff_str == '+':
                    coeff = Rational('1')
                elif coeff_str == '-':
                    coeff = Rational('-1')
                else:
                    coeff = Rational(coeff_str)
                
                coeff = coeff.MUL_QQ_Q(Rational(f"{sign}/1"))
                
                # Обрабатываем степень
                if len(parts) > 1 and parts[1]:
                    # Есть степень вида ^n
                    power = int(parts[1].replace('^', ''))
                else:
                    # Нет степени - значит степень 1
                    power = 1
                
                terms[power] = coeff
        
        return terms
    
    def _remove_leading_zeros(self):
        """Удаляет нулевые старшие коэффициенты"""
        zero_powers = []
        for power, coeff in self.terms.items():
            if coeff.is_zero():
                zero_powers.append(power)
        
        for power in zero_powers:
            del self.terms[power]
        
        # Если все коэффициенты нулевые, оставляем только нулевой полином
        if not self.terms:
            self.terms[0] = Rational('0')
    
    def _get_max_degree(self) -> int:
        """Возвращает максимальную степень полинома"""
        if not self.terms:
            return 0
        return max(self.terms.keys())
    
    def _poly_clone(self) -> Polynomial:
        """Создает независимую копию полинома"""
        p = Polynomial('0')
        p.terms = {power: Rational(str(coeff)) for power, coeff in self.terms.items()}
        p._remove_leading_zeros()
        return p
    
    def is_zero(self) -> bool:
        """Проверка, является ли полином нулевым"""
        self._remove_leading_zeros()
        return len(self.terms) == 1 and 0 in self.terms and self.terms[0].is_zero()
    
    def __str__(self):
        """Строковое представление полинома"""
        if self.is_zero():
            return "0"
        
        terms_list = []
        sorted_powers = sorted(self.terms.keys())
        
        for power in sorted_powers:
            coeff = self.terms[power]
            if coeff.is_zero():
                continue
            
            coeff_str = str(coeff)
            
            if power == 0:
                terms_list.append(coeff_str)
            elif power == 1:
                if coeff_str == "1":
                    terms_list.append("x")
                elif coeff_str == "-1":
                    terms_list.append("-x")
                else:
                    terms_list.append(f"{coeff_str}*x")
            else:
                if coeff_str == "1":
                    terms_list.append(f"x^{power}")
                elif coeff_str == "-1":
                    terms_list.append(f"-x^{power}")
                else:
                    terms_list.append(f"{coeff_str}*x^{power}")
        
        # Собираем строку, обрабатывая знаки
        result = ""
        for i, term in enumerate(terms_list):
            if i == 0:
                result = term
            else:
                if term.startswith('-'):
                    result += f" - {term[1:]}"
                else:
                    result += f" + {term}"
        
        return result
    
    def get_coeff(self, power: int) -> Rational:
        """Возвращает коэффициент при заданной степени"""
        return self.terms.get(power, Rational('0'))
    
    # P-1: Сложение многочленов
    def ADD_PP_P(self, other: Polynomial) -> Polynomial:
        result_terms = {}
        # Объединяем все степени из обоих многочленов
        all_powers = set(self.terms.keys()) | set(other.terms.keys())
        
        for power in all_powers:
            coeff1 = self.get_coeff(power)
            coeff2 = other.get_coeff(power)
            # Складываем коэффициенты при одинаковых степенях
            result_terms[power] = coeff1.ADD_QQ_Q(coeff2)
        
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-2: Вычитание многочленов
    def SUB_PP_P(self, other: Polynomial) -> Polynomial:
        result_terms = {}
        # Объединяем все степени из обоих многочленов
        all_powers = set(self.terms.keys()) | set(other.terms.keys())
        
        for power in all_powers:
            coeff1 = self.get_coeff(power)
            coeff2 = other.get_coeff(power)
            # Вычитаем коэффициенты при одинаковых степенях
            result_terms[power] = coeff1.SUB_QQ_Q(coeff2)
        
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-3: Умножение многочлена на рациональное число
    def MUL_PQ_P(self, rational_num: Rational) -> Polynomial:
        result_terms = {}
        
        for power, coeff in self.terms.items():
            # Умножаем каждый коэффициент на заданное число
            result_terms[power] = coeff.MUL_QQ_Q(rational_num)
        
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-4: Умножение многочлена на x^k
    def MUL_Pxk_P(self, k: Natural) -> Polynomial:
        shift = int(str(k))
        result_terms = {}
        
        for power, coeff in self.terms.items():
            if not coeff.is_zero():
                # Сдвигаем все степени на k
                result_terms[power + shift] = coeff
        
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-5: Старший коэффициент многочлена
    def LED_P_Q(self) -> Rational:
        if self.is_zero():
            return Rational('0')
        
        # Находим максимальную степень и возвращаем соответствующий коэффициент
        max_power = self._get_max_degree()
        return self.terms[max_power]
    
    # P-6: Степень многочлена
    def DEG_P_N(self) -> Natural:
        if self.is_zero():
            return Natural('0')
        
        # Возвращаем максимальную степень как натуральное число
        return Natural(str(self._get_max_degree()))
    
    # P-7: Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def FAC_P_Q(self) -> Rational:
        # Отфильтруем ненулевые коэффициенты
        valid_coefs = [coef for coef in self.terms.values() if not coef.is_zero()]
        if not valid_coefs:
            return Rational('1/1')
        
        # Получаем натуральные числители и знаменатели
        numerators_N = [Integer(str(coef.numerator.ABS_Z_N())).TRANS_Z_N() for coef in valid_coefs]
        denominators_N = [coef.denominator for coef in valid_coefs]
        
        # Находим НОД числителей
        gcd_num = numerators_N[0]
        for i in range(1, len(numerators_N)):
            gcd_num = gcd_num.GCF_NN_N(numerators_N[i])
        
        # Находим НОК знаменателей
        lcm_den = denominators_N[0]
        for i in range(1, len(denominators_N)):
            lcm_den = lcm_den.LCM_NN_N(denominators_N[i])
        
        # Преобразуем обратно в целые числа
        gcd_num_Z = Integer.TRANS_N_Z(gcd_num)
        lcm_den_Z = Integer.TRANS_N_Z(lcm_den)
        
        # Проверяем делимость
        remainder_N = gcd_num.MOD_NN_N(lcm_den)
        if remainder_N.NZER_N_B() == 'да':  # остаток ≠ 0
            return Rational(f"{gcd_num_Z}/{lcm_den_Z}")
        else:
            quotient_Z = gcd_num_Z.DIV_ZZ_Z(lcm_den_Z)
            return Rational(f"{quotient_Z}/1")
    
    # P-8: Умножение многочленов
    def MUL_PP_P(self, other: Polynomial) -> Polynomial:
        # Используем стратегию: умножаем каждый член первого на второй и складываем
        result = Polynomial('0')
        
        for power1, coeff1 in self.terms.items():
            # Умножаем второй полином на коэффициент (MUL_PQ_P)
            temp_poly = other.MUL_PQ_P(coeff1)
            
            # Умножаем на x^power1 (MUL_Pxk_P)
            temp_poly = temp_poly.MUL_Pxk_P(Natural(str(power1)))
            
            # Добавляем к результату (ADD_PP_P)
            result = result.ADD_PP_P(temp_poly)
        
        return result
    
    # P-9: Частное от деления многочлена на многочлен при делении с остатком
    def DIV_PP_P(self, other: Polynomial) -> Polynomial:
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
        # Создаем копии делимого и делителя
        A = self._poly_clone()  # Делимое
        B = other._poly_clone()  # Делитель
        
        # Если степень делимого меньше степени делителя, возвращаем 0
        if A.DEG_P_N().COM_NN_D(B.DEG_P_N()) == 1:
            return Polynomial('0')
        
        Q = Polynomial('0')  # Частное
        
        while not A.is_zero():
            deg_A = A.DEG_P_N()
            deg_B = B.DEG_P_N()
            
            # Если степень A меньше степени B - выходим
            if deg_A.COM_NN_D(deg_B) == 1:
                break
                
            # Вычисляем разность степеней
            deg_diff = deg_A.SUB_NN_N(deg_B)
            
            # Получаем старшие коэффициенты
            lead_A = A.LED_P_Q()
            lead_B = B.LED_P_Q()
            
            # Делим старшие коэффициенты
            q_coeff = Rational.DIV_QQ_Q(lead_A, lead_B)
            
            # Создаем моном: q_coeff * x^deg_diff
            term_poly = Polynomial(str(q_coeff)).MUL_Pxk_P(deg_diff)
            
            # Добавляем моном к частному
            Q = Q.ADD_PP_P(term_poly)
            
            # Вычитаем B * term_poly из A
            product = B.MUL_PP_P(term_poly)
            A = A.SUB_PP_P(product)
            
            # Удаляем нулевые старшие коэффициенты
            A._remove_leading_zeros()
        
        return Q

    # P-10: Остаток от деления многочлена на многочлен при делении с остатком
    def MOD_PP_P(self, other: Polynomial) -> Polynomial:
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
        # Вычисляем частное
        quotient = self.DIV_PP_P(other)
        
        # Вычисляем произведение делителя на частное
        product = other.MUL_PP_P(quotient)
        
        # Вычисляем остаток: self - product
        remainder = self.SUB_PP_P(product)
        
        remainder._remove_leading_zeros()
        return remainder
    
    # P-11: НОД многочленов
    def GCF_PP_P(self, other: Polynomial) -> Polynomial:
        a = self._poly_clone()
        b = other._poly_clone()
        
        if b.is_zero():
            return a
        
        # Алгоритм Евклида для многочленов
        while not b.is_zero():
            remainder = a.MOD_PP_P(b)
            a, b = b, remainder
        
        # Нормализация - делаем старший коэффициент равным 1
        if not a.is_zero():
            lead_coeff = a.LED_P_Q()
            normalized_terms = {}
            for power, coeff in a.terms.items():
                normalized_terms[power] = coeff.DIV_QQ_Q(lead_coeff)
            
            result = Polynomial('0')
            result.terms = normalized_terms
            return result
        
        return a
    
    # P-12: Производная многочлена
    def DER_P_P(self) -> Polynomial:
        result_terms = {}
        
        for power, coeff in self.terms.items():
            if power > 0:
                # Умножаем коэффициент на степень
                multiplier = Rational(f"{power}/1")
                new_coeff = coeff.MUL_QQ_Q(multiplier)
                # Уменьшаем степень на 1
                result_terms[power - 1] = new_coeff
        
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-13: Преобразование многочлена - кратные корни в простые
    def NMR_P_P(self) -> Polynomial:
        # Находим производную
        derivative = self.DER_P_P()
        
        # Находим НОД исходного многочлена и его производной
        gcd_poly = self.GCF_PP_P(derivative)
        
        # Если НОД - константа, кратных корней нет
        if gcd_poly.DEG_P_N().COM_NN_D(Natural('0')) == 0:
            return self._poly_clone()
        
        # Делим исходный многочлен на НОД
        return self.DIV_PP_P(gcd_poly)


# Тестирование
if __name__ == "__main__":
    print('Базовая проверка многочленов:')
    
    # Примеры полиномов
    poly1 = Polynomial("2*x^3 + 3*x^2 - x + 5")
    poly2 = Polynomial("x^2 + 1")
    poly3 = Polynomial("1/2*x^4 - 1/3*x^2 + 2")
    
    print(f"poly1 = {poly1}")
    print(f"poly2 = {poly2}")
    print(f"poly3 = {poly3}")
    print()
    
    print("Операции:")
    print(f"poly1 + poly2 = {poly1.ADD_PP_P(poly2)}")
    print(f"poly1 - poly2 = {poly1.SUB_PP_P(poly2)}")
    print(f"poly1 * poly2 = {poly1.MUL_PP_P(poly2)}")
    print(f"Степень poly1: {poly1.DEG_P_N()}")
    print(f"Старший коэффициент poly1: {poly1.LED_P_Q()}")
    print(f"Производная poly1: {poly1.DER_P_P()}")