# выполнили Мазеев В., гр. 4384, Калинина А., гр. 4384 и Дровнев Д., гр. 4384

from __future__ import annotations
from .Rational import Rational
from .Integer import Integer
from .Natural import Natural

'''
Многочлен — представлен в виде словаря {степень: коэффициент},
где коэффициент — рациональное число.
'''

class Polynomial:
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
        # Создаем словарь для хранения коэффициентов результирующего многочлена
        result_terms = {}
        
        # Объединяем все степени из обоих многочленов
        # Используем множество для получения уникальных степеней
        all_powers = set(self.terms.keys()) | set(other.terms.keys())
        
        # Проходим по всем степеням, присутствующим в обоих многочленах
        for power in all_powers:
            # Получаем коэффициенты при текущей степени из обоих многочленов
            # Если степень отсутствует в многочлене, возвращается нулевой коэффициент
            coeff1 = self.get_coeff(power)
            coeff2 = other.get_coeff(power)
            
            # Складываем коэффициенты при одинаковых степенях
            # Результат - новая дробь, представляющая сумму коэффициентов
            result_terms[power] = coeff1.ADD_QQ_Q(coeff2)
        
        # Создаем новый многочлен-результат на основе вычисленных коэффициентов
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        
        # Удаляем нулевые старшие коэффициенты для канонического представления
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-2: Вычитание многочленов
    def SUB_PP_P(self, other: Polynomial) -> Polynomial:
        # Создаем словарь для хранения коэффициентов результирующего многочлена
        result_terms = {}
        
        # Объединяем все степени из обоих многочленов
        # Используем множество для получения уникальных степеней
        all_powers = set(self.terms.keys()) | set(other.terms.keys())
        
        # Проходим по всем степеням, присутствующим в обоих многочленах
        for power in all_powers:
            # Получаем коэффициенты при текущей степени из обоих многочленов
            # Если степень отсутствует в многочлене, возвращается нулевой коэффициент
            coeff1 = self.get_coeff(power)  # коэффициент уменьшаемого
            coeff2 = other.get_coeff(power) # коэффициент вычитаемого
            
            # Вычитаем коэффициенты при одинаковых степенях
            # Из коэффициента первого многочлена вычитаем коэффициент второго многочлена
            result_terms[power] = coeff1.SUB_QQ_Q(coeff2)
        
        # Создаем новый многочлен-результат на основе вычисленных коэффициентов
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        
        # Удаляем нулевые старшие коэффициенты для канонического представления
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-3: Умножение многочлена на рациональное число
    def MUL_PQ_P(self, rational_num: Rational) -> Polynomial:
        # Создаем словарь для хранения коэффициентов результирующего многочлена
        result_terms = {}
        
        # Проходим по всем членам исходного многочлена
        for power, coeff in self.terms.items():
            # Умножаем каждый рациональный коэффициент на заданное рациональное число
            # Результат остается рациональным числом, сохраняя тип данных
            result_terms[power] = coeff.MUL_QQ_Q(rational_num)
        
        # Создаем новый многочлен-результат на основе вычисленных коэффициентов
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        
        # Удаляем нулевые старшие коэффициенты для канонического представления
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-4: Умножение многочлена на x^k
    def MUL_Pxk_P(self, k: Natural) -> Polynomial:
        # Преобразуем натуральное число k в целое число для арифметических операций
        shift = int(str(k))
        
        # Создаем словарь для хранения коэффициентов результирующего многочлена
        result_terms = {}
        
        # Проходим по всем членам исходного многочлена
        for power, coeff in self.terms.items():
            # Если встретили нулевой коэффициент, пропускаем и идём дальше
            if not coeff.is_zero():
                # Сдвигаем степень текущего члена на k позиций вправо
                # Новая степень = старая степень + k
                result_terms[power + shift] = coeff
        
        # Создаем новый многочлен-результат на основе сдвинутых коэффициентов
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        
        # Удаляем нулевые старшие коэффициенты для канонического представления
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-5: Старший коэффициент многочлена
    def LED_P_Q(self) -> Rational:
        # Проверяем, является ли многочлен нулевым
        # Для нулевого многочлена старший коэффициент считается равным 0
        if self.is_zero():
            return Rational('0')
        
        # Находим максимальную степень многочлена - это степень старшего члена
        max_power = self._get_max_degree()
        
        # Возвращаем коэффициент при старшей степени
        return self.terms[max_power]
    
    # P-6: Степень многочлена
    def DEG_P_N(self) -> Natural:
        # Проверяем, является ли многочлен нулевым
        # Степень нулевого многочлена в математике обычно считается равной -∞,
        # но в нашей системе для согласованности с натуральными числами возвращаем 0
        if self.is_zero():
            return Natural('0')
        
        # Находим максимальную степень среди всех ненулевых членов многочлена
        # и возвращаем её как натуральное число
        # Это соответствует математическому определению степени многочлена
        return Natural(str(self._get_max_degree()))
    
    # P-7: Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def FAC_P_Q(self) -> Rational:
        # Отфильтруем ненулевые коэффициенты, так как нулевые коэффициенты
        # не влияют на вычисление НОД числителей и НОК знаменателей
        valid_coefs = [coef for coef in self.terms.values() if not coef.is_zero()]
        
        # Если все коэффициенты нулевые (нулевой многочлен), возвращаем 1
        # так как вынесение множителя не изменяет нулевой многочлен
        if not valid_coefs:
            return Rational('1/1')
        
        # Получаем натуральные числители и знаменатели из рациональных коэффициентов
        # (для числителей берем модуль, так как НОД вычисляется для натуральных чисел)
        numerators_N = [Integer(str(coef.numerator.ABS_Z_N())).TRANS_Z_N() for coef in valid_coefs]
        denominators_N = [coef.denominator for coef in valid_coefs]
        
        # Находим НОД всех числителей коэффициентов
        # Начинаем с первого числителя и последовательно находим НОД с остальными
        gcd_num = numerators_N[0]
        for i in range(1, len(numerators_N)):
            gcd_num = gcd_num.GCF_NN_N(numerators_N[i])
        
        # Находим НОК всех знаменателей коэффициентов
        # Начинаем с первого знаменателя и последовательно находим НОК с остальными
        lcm_den = denominators_N[0]
        for i in range(1, len(denominators_N)):
            lcm_den = lcm_den.LCM_NN_N(denominators_N[i])
        
        # Преобразуем натуральные числа обратно в целые для работы с рациональными числами
        gcd_num_Z = Integer.TRANS_N_Z(gcd_num)
        lcm_den_Z = Integer.TRANS_N_Z(lcm_den)
        
        # Проверяем, делится ли НОД числителей на НОК знаменателей
        # Это нужно для упрощения результирующей дроби
        remainder_N = gcd_num.MOD_NN_N(lcm_den)
        
        # Если остаток ≠ 0, т.е. НОД числителей не делится нацело на НОК знаменателей
        if remainder_N.NZER_N_B() == 'да':
            # Возвращаем дробь НОД числителей / НОК знаменателей
            return Rational(f"{gcd_num_Z}/{lcm_den_Z}")
        else:
            # Иначе делится нацело, возвращаем целое число
            quotient_Z = gcd_num_Z.DIV_ZZ_Z(lcm_den_Z)
            return Rational(f"{quotient_Z}/1")
    
    # P-8: Умножение многочленов
    def MUL_PP_P(self, other: Polynomial) -> Polynomial:
        # Используем стратегию: умножаем каждый член первого многочлена на второй многочлен и складываем
        # Это соответствует математическому определению умножения многочленов "в столбик"
        result = Polynomial('0')
        
        # Проходим по всем членам первого многочлена
        for power1, coeff1 in self.terms.items():
            # Умножаем второй многочлен на коэффициент текущего члена первого многочлена
            # Это дает многочлен с теми же степенями, но с измененными коэффициентами
            temp_poly = other.MUL_PQ_P(coeff1)
            
            # Умножаем полученный многочлен на x^power1 (где power1 - степень текущего члена первого многочлена)
            # Это сдвигает все степени на power1, что соответствует умножению на моном x^power1
            temp_poly = temp_poly.MUL_Pxk_P(Natural(str(power1)))
            
            # Добавляем полученный многочлен к накапливаемому результату
            # Это соответствует сложению частичных произведений
            result = result.ADD_PP_P(temp_poly)
        
        # Возвращаем результирующий многочлен
        # Все нулевые коэффициенты автоматически удаляются методом ADD_PP_P
        return result
    
    # P-9: Частное от деления многочлена на многочлен при делении с остатком
    def DIV_PP_P(self, other: Polynomial) -> Polynomial:
        # Проверяем, что делитель не является нулевым многочленом
        # Деление на нулевой многочлен математически не определено
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
        # Создаем копии делимого и делителя для безопасного изменения
        # Это предотвращает модификацию исходных объектов
        A = self._poly_clone()  # Делимое (будет уменьшаться в процессе деления)
        B = other._poly_clone()  # Делитель (остается неизменным)
        
        # Если степень делимого меньше степени делителя, частное равно 0
        # Это соответствует математическому определению целочисленного деления
        if A.DEG_P_N().COM_NN_D(B.DEG_P_N()) == 1:
            return Polynomial('0')
        
        Q = Polynomial('0')  # Частное (накапливаем результат деления)
        
        # Основной цикл алгоритма деления в столбик
        # Продолжаем, пока делимое не станет нулевым или его степень не станет меньше степени делителя
        while not A.is_zero():
            deg_A = A.DEG_P_N()  # Текущая степень делимого
            deg_B = B.DEG_P_N()  # Степень делителя
            
            # Если текущая степень делимого меньше степени делителя, деление завершено
            if deg_A.COM_NN_D(deg_B) == 1:
                break
                
            # Вычисляем разность степеней для определения степени следующего члена частного
            deg_diff = deg_A.SUB_NN_N(deg_B)
            
            # Получаем старшие коэффициенты делимого и делителя
            lead_A = A.LED_P_Q()  # Старший коэффициент делимого
            lead_B = B.LED_P_Q()  # Старший коэффициент делителя
            
            # Делим старшие коэффициенты для получения коэффициента следующего члена частного
            q_coeff = Rational.DIV_QQ_Q(lead_A, lead_B)
            
            # Создаем моном: коэффициент × x^разность_степеней
            # Это следующий член частного, который нужно добавить
            term_poly = Polynomial(str(q_coeff)).MUL_Pxk_P(deg_diff)
            
            # Добавляем вычисленный моном к частному
            Q = Q.ADD_PP_P(term_poly)
            
            # Вычитаем из делимого произведение делителя на добавленный член частного
            # Это соответствует шагу вычитания в алгоритме деления в столбик
            product = B.MUL_PP_P(term_poly)
            A = A.SUB_PP_P(product)
            
            # Удаляем нулевые старшие коэффициенты для поддержания канонической формы
            # Это важно для корректного определения степени на следующей итерации
            A._remove_leading_zeros()
        
        # Возвращаем найденное частное
        return Q

    # P-10: Остаток от деления многочлена на многочлен при делении с остатком
    def MOD_PP_P(self, other: Polynomial) -> Polynomial:
        # Проверяем, что делитель не является нулевым многочленом
        # Остаток от деления на нулевой многочлен математически не определен
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
        # Вычисляем частное от деления текущего многочлена на другой многочлен
        # Используем уже реализованный метод DIV_PP_P для нахождения целой части
        quotient = self.DIV_PP_P(other)
        
        # Вычисляем произведение делителя на найденное частное
        # Это дает ту часть делимого, которая делится на делитель без остатка
        product = other.MUL_PP_P(quotient)
        
        # Вычисляем остаток по формуле: остаток = делимое - (делитель × частное)
        # Это соответствует математическому определению остатка от деления
        remainder = self.SUB_PP_P(product)
        
        # Удаляем нулевые старшие коэффициенты для обеспечения канонического представления
        # Гарантируем, что остаток представлен в нормализованной форме
        remainder._remove_leading_zeros()
        return remainder
    
    # P-11: НОД многочленов
    def GCF_PP_P(self, other: Polynomial) -> Polynomial:
        # Создаем копии многочленов для безопасного изменения
        # Это предотвращает модификацию исходных объектов в процессе вычислений
        a = self._poly_clone()
        b = other._poly_clone()
        
        # Обрабатываем краевые случаи с нулевыми многочленами
        # Математически строго НОД(0, 0) не определен, но для удобства возвращаем 0
        if a.is_zero() and b.is_zero():
            return Polynomial('0')
        
        # Если первый многочлен нулевой, НОД равен второму многочлену
        # НОД(0, B) = B (с точностью до постоянного множителя)
        if a.is_zero():
            return b
        
        # Если второй многочлен нулевой, НОД равен первому многочлену
        # НОД(A, 0) = A (с точностью до постоянного множителя)
        if b.is_zero():
            return a
        
        # Алгоритм Евклида для многочленов
        # Продолжаем, пока второй многочлен не станет нулевым
        while not b.is_zero():
            # Вычисляем остаток от деления первого многочлена на второй
            remainder = a.MOD_PP_P(b)
            
            # Обновляем значения: a становится b, b становится остатком
            # Это соответствует шагу НОД(a, b) = НОД(b, a mod b)
            a, b = b, remainder
        
        # На этом этапе a содержит ненулевой НОД многочленов
        # (поскольку оба исходных многочлена были ненулевыми)
        
        # Нормализация результата - делаем старший коэффициент равным 1
        # Это стандартное представление НОД многочленов (унитарная форма)
        
        # Получаем старший коэффициент найденного НОД
        lead_coeff = a.LED_P_Q()
        
        # Делим все коэффициенты на старший коэффициент
        # Это обеспечивает унитарность многочлена (старший коэффициент = 1)
        normalized_terms = {}
        for power, coeff in a.terms.items():
            normalized_terms[power] = coeff.DIV_QQ_Q(lead_coeff)
        
        # Создаем нормализованный многочлен-результат
        result = Polynomial('0')
        result.terms = normalized_terms
        return result
    
    # P-12: Производная многочлена
    def DER_P_P(self) -> Polynomial:
        # Создаем словарь для хранения коэффициентов производной
        result_terms = {}
        
        # Проходим по всем членам (мономам) исходного многочлена
        for power, coeff in self.terms.items():
            # Если степень монома больше 0, т.е. моном не константа
            # (производная от константы равна 0, поэтому пропускаем)
            if power > 0:
                # Умножаем коэффициент на степень по правилу дифференцирования:
                # d/dx(a*x^n) = n*a*x^(n-1)
                multiplier = Rational(f"{power}/1")
                new_coeff = coeff.MUL_QQ_Q(multiplier)
                # Уменьшаем степень на 1 согласно правилу дифференцирования степенной функции
                result_terms[power - 1] = new_coeff
        
        # Создаем многочлен-результат на основе вычисленных коэффициентов
        result_poly = Polynomial('0')
        result_poly.terms = result_terms
        
        # Удаляем нулевые старшие коэффициенты для канонического представления
        # Особенно важно для случаев, когда производная оказывается нулевым многочленом
        result_poly._remove_leading_zeros()
        return result_poly
    
    # P-13: Преобразование многочлена - кратные корни в простые
    def NMR_P_P(self) -> Polynomial:
        # Находим производную исходного многочлена
        # (производная используется для определения наличия кратных корней)
        derivative = self.DER_P_P()
        
        # Находим НОД исходного многочлена и его производной
        # (если многочлен имеет кратные корни, они будут общими корнями с производной)
        gcd_poly = self.GCF_PP_P(derivative)
        
        # Проверяем, является ли НОД константой (многочленом степени 0)
        # Если НОД - константа, это означает, что у исходного многочлена нет кратных корней
        if gcd_poly.DEG_P_N().COM_NN_D(Natural('0')) == 0:
            # Возвращаем копию исходного многочлена, так как преобразование не требуется
            return self._poly_clone()
        
        # Если НОД не является константой, делим исходный многочлен на НОД
        # Это удаляет кратные корни, оставляя только простые корни
        # Результат - многочлен с теми же простыми корнями, но без кратностей
        return self.DIV_PP_P(gcd_poly)

# Тестирование
def tests_for_polynomials():
    # Создаем тестовые полиномы
    poly1 = Polynomial("x^2 + 2*x + 1")           # (x+1)^2
    poly2 = Polynomial("x + 1")                   # x+1
    poly3 = Polynomial("2*x^3 + 3*x^2 + x + 5")   # 2x^3 + 3x^2 + x + 5
    poly4 = Polynomial("x^2 - 1")                 # (x-1)(x+1)
    poly5 = Polynomial("0")                       # нулевой полином
    poly6 = Polynomial("3*x^4 + 2*x^2 + 1")       # 3x^4 + 2x^2 + 1
    poly7 = Polynomial("1/2*x^2 + 1/3*x + 1/4")   # дробные коэффициенты

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА POLYNOMIAL")
    print("=" * 60)

    # Тест 1: ADD_PP_P - сложение полиномов
    print("\n1. ТЕСТИРОВАНИЕ СЛОЖЕНИЯ ПОЛИНОМОВ (ADD_PP_P):")
    print(f"   ({poly1}) + ({poly2}) = {poly1.ADD_PP_P(poly2)}")  # x^2 + 3x + 2
    print(f"   ({poly3}) + ({poly4}) = {poly3.ADD_PP_P(poly4)}")  # 2x^3 + 4x^2 + x + 4
    print(f"   ({poly6}) + ({poly5}) = {poly6.ADD_PP_P(poly5)}")  # 3x^4 + 2x^2 + 1

    # Тест 2: SUB_PP_P - вычитание полиномов
    print("\n2. ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ ПОЛИНОМОВ (SUB_PP_P):")
    print(f"   ({poly1}) - ({poly2}) = {poly1.SUB_PP_P(poly2)}")  # x^2 + x
    print(f"   ({poly3}) - ({poly4}) = {poly3.SUB_PP_P(poly4)}")  # 2x^3 + 2x^2 + x + 6
    print(f"   ({poly6}) - ({poly5}) = {poly6.SUB_PP_P(poly5)}")  # 3x^4 + 2x^2 + 1

    # Тест 3: MUL_PQ_P - умножение полинома на рациональное число
    print("\n3. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ ПОЛИНОМА НА ЧИСЛО (MUL_PQ_P):")
    rational1 = Rational("2/1")
    rational2 = Rational("1/2")
    print(f"   ({poly1}) * {rational1} = {poly1.MUL_PQ_P(rational1)}")  # 2x^2 + 4x + 2
    print(f"   ({poly3}) * {rational2} = {poly3.MUL_PQ_P(rational2)}")  # x^3 + 3/2*x^2 + 1/2*x + 5/2

    # Тест 4: MUL_Pxk_P - умножение полинома на x^k
    print("\n4. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ ПОЛИНОМА НА x^k (MUL_Pxk_P):")
    k1 = Natural("2")
    k2 = Natural("1")
    print(f"   ({poly2}) * x^{k1} = {poly2.MUL_Pxk_P(k1)}")  # x^3 + x^2
    print(f"   ({poly4}) * x^{k2} = {poly4.MUL_Pxk_P(k2)}")  # x^3 - x

    # Тест 5: LED_P_Q - старший коэффициент
    print("\n5. ТЕСТИРОВАНИЕ СТАРШЕГО КОЭФФИЦИЕНТА (LED_P_Q):")
    print(f"   Старший коэффициент ({poly1}) = {poly1.LED_P_Q()}")  # 1
    print(f"   Старший коэффициент ({poly3}) = {poly3.LED_P_Q()}")  # 2
    print(f"   Старший коэффициент ({poly7}) = {poly7.LED_P_Q()}")  # 1/2

    # Тест 6: DEG_P_N - степень полинома
    print("\n6. ТЕСТИРОВАНИЕ СТЕПЕНИ ПОЛИНОМА (DEG_P_N):")
    print(f"   Степень ({poly1}) = {poly1.DEG_P_N()}")  # 2
    print(f"   Степень ({poly3}) = {poly3.DEG_P_N()}")  # 3
    print(f"   Степень ({poly5}) = {poly5.DEG_P_N()}")  # 0

    # Тест 7: FAC_P_Q - вынесение НОК знаменателей и НОД числителей
    print("\n7. ТЕСТИРОВАНИЕ ВЫНЕСЕНИЯ НОК/НОД (FAC_P_Q):")
    print(f"   FAC({poly7}) = {poly7.FAC_P_Q()}")  # НОК(2,3,4)=12 / НОД(1,1,1)=1 = 12
    print(f"   FAC({poly1}) = {poly1.FAC_P_Q()}")  # 1

    # Тест 8: MUL_PP_P - умножение полиномов
    print("\n8. ТЕСТИРОВАНИЕ УМНОЖЕНИЯ ПОЛИНОМОВ (MUL_PP_P):")
    print(f"   ({poly1}) * ({poly2}) = {poly1.MUL_PP_P(poly2)}")  # x^3 + 3x^2 + 3x + 1
    print(f"   ({poly2}) * ({poly4}) = {poly2.MUL_PP_P(poly4)}")  # x^3 + x^2 - x - 1

    # Тест 9: DIV_PP_P - деление полиномов
    print("\n9. ТЕСТИРОВАНИЕ ДЕЛЕНИЯ ПОЛИНОМОВ (DIV_PP_P):")
    print(f"   ({poly1}) / ({poly2}) = {poly1.DIV_PP_P(poly2)}")  # x + 1
    print(f"   ({poly3}) / ({poly2}) = {poly3.DIV_PP_P(poly2)}")  # 2x^2 + x + 0 (остаток 5)

    # Тест 10: MOD_PP_P - остаток от деления полиномов
    print("\n10. ТЕСТИРОВАНИЕ ОСТАТКА ОТ ДЕЛЕНИЯ (MOD_PP_P):")
    print(f"   ({poly1}) % ({poly2}) = {poly1.MOD_PP_P(poly2)}")  # 0
    print(f"   ({poly3}) % ({poly2}) = {poly3.MOD_PP_P(poly2)}")  # 5

    # Тест 11: GCF_PP_P - НОД полиномов
    print("\n11. ТЕСТИРОВАНИЕ НОД ПОЛИНОМОВ (GCF_PP_P):")
    print(f"   НОД({poly1}, {poly2}) = {poly1.GCF_PP_P(poly2)}")  # x + 1
    print(f"   НОД({poly4}, {poly2}) = {poly4.GCF_PP_P(poly2)}")  # x + 1

    # Тест 12: DER_P_P - производная полинома
    print("\n12. ТЕСТИРОВАНИЕ ПРОИЗВОДНОЙ ПОЛИНОМА (DER_P_P):")
    print(f"   d/dx({poly1}) = {poly1.DER_P_P()}")  # 2x + 2
    print(f"   d/dx({poly3}) = {poly3.DER_P_P()}")  # 6x^2 + 6x + 1
    print(f"   d/dx({poly7}) = {poly7.DER_P_P()}")  # x + 1/3

    # Тест 13: NMR_P_P - преобразование кратных корней в простые
    print("\n13. ТЕСТИРОВАНИЕ ПРЕОБРАЗОВАНИЯ КРАТНЫХ КОРНЕЙ (NMR_P_P):")
    poly_multiple = Polynomial("x^3 - 3*x^2 + 3*x - 1")  # (x-1)^3
    print(f"   NMR({poly_multiple}) = {poly_multiple.NMR_P_P()}")  # x - 1
    print(f"   NMR({poly4}) = {poly4.NMR_P_P()}")  # x^2 - 1 (без изменений)

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ПОЛИНОМОВ ЗАВЕРШЕНО!")
    print("=" * 60)

tests_for_polynomials()

