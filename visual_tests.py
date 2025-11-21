# Визуальные тесты для всех модулей с анализом лучших/средних/худших случаев
import time
from MODULES.Natural import Natural
from MODULES.Integer import Integer
from MODULES.Rational import Rational
from MODULES.Polynomial import Polynomial

def format_polynomial_output(poly_str):
    """Форматирует строку полинома для вывода от старшей степени к младшей"""
    # Это упрощенная функция для демонстрации
    # В реальной реализации нужно парсить и переупорядочивать полином
    return poly_str

def test_natural():
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА NATURAL")
    print("=" * 60)

    start_time = time.time()
    
    # Лучшие/средние/худшие случаи
    small1, small2 = Natural("2"), Natural("3")
    medium1, medium2 = Natural("123"), Natural("456") 
    large1, large2 = Natural("999999"), Natural("1000000")
    zero = Natural("0")
    one = Natural("1")

    print("\n1. СРАВНЕНИЕ (COM_NN_D):")
    print("   Лучший случай (малые числа):")
    print(f"     {small1} сравнить с {small2}: {small1.COM_NN_D(small2)}")
    print("   Средний случай (случайные числа):")
    random_med1, random_med2 = Natural("847"), Natural("236")
    print(f"     {random_med1} сравнить с {random_med2}: {random_med1.COM_NN_D(random_med2)}")
    print("   Худший случай (большие числа):")
    print(f"     {large1} сравнить с {large2}: {large1.COM_NN_D(large2)}")

    print("\n2. ПРОВЕРКА НА НОЛЬ (NZER_N_B):")
    print("   Лучший случай (не ноль):")
    print(f"     {small1} не равно нулю? {small1.NZER_N_B()}")
    print("   Средний случай (случайное число):")
    random_med = Natural("729")
    print(f"     {random_med} не равно нулю? {random_med.NZER_N_B()}")
    print("   Худший случай (ноль):")
    print(f"     {zero} не равно нулю? {zero.NZER_N_B()}")

    print("\n3. ДОБАВЛЕНИЕ 1 (ADD_1N_N):")
    print("   Лучший случай (без переноса):")
    print(f"     {small1} + 1 = {small1.ADD_1N_N()}")
    print("   Средний случай (случайное число):")
    random_med = Natural("458")
    print(f"     {random_med} + 1 = {random_med.ADD_1N_N()}")
    print("   Худший случай (цепочка переносов):")
    print(f"     {Natural('999')} + 1 = {Natural('999').ADD_1N_N()}")

    print("\n4. СЛОЖЕНИЕ (ADD_NN_N):")
    print("   Лучший случай (малые числа):")
    print(f"     {small1} + {small2} = {small1.ADD_NN_N(small2)}")
    print("   Средний случай (случайные числа):")
    random_med1, random_med2 = Natural("345"), Natural("678")
    print(f"     {random_med1} + {random_med2} = {random_med1.ADD_NN_N(random_med2)}")
    print("   Худший случай (большие числа с переносом):")
    print(f"     {large1} + {large2} = {large1.ADD_NN_N(large2)}")

    print("\n5. ВЫЧИТАНИЕ (SUB_NN_N):")
    print("   Лучший случай (результат малое число):")
    print(f"     {Natural('5')} - {Natural('2')} = {Natural('5').SUB_NN_N(Natural('2'))}")
    print("   Средний случай (случайные числа):")
    print(f"     {random_med1} - {Natural('100')} = {random_med1.SUB_NN_N(Natural('100'))}")
    print("   Худший случай (заём через много разрядов):")
    print(f"     {Natural('1000')} - {Natural('1')} = {Natural('1000').SUB_NN_N(Natural('1'))}")

    print("\n6. УМНОЖЕНИЕ НА ЦИФРУ (MUL_ND_N):")
    print("   Лучший случай (умножение на 1):")
    print(f"     {small1} * 1 = {small1.MUL_ND_N(1)}")
    print("   Средний случай (умножение на 5):")
    print(f"     {random_med} * 5 = {random_med.MUL_ND_N(5)}")
    print("   Худший случай (умножение на 9 с переносом):")
    print(f"     {Natural('999')} * 9 = {Natural('999').MUL_ND_N(9)}")

    print("\n7. УМНОЖЕНИЕ НА 10^k (MUL_Nk_N):")
    print("   Лучший случай (k=0):")
    print(f"     {small1} * 10^0 = {small1.MUL_Nk_N(0)}")
    print("   Средний случай (k=2):")
    print(f"     {random_med} * 10^2 = {random_med.MUL_Nk_N(2)}")
    print("   Худший случай (k=5):")
    print(f"     {Natural('12')} * 10^5 = {Natural('12').MUL_Nk_N(5)}")

    print("\n8. УМНОЖЕНИЕ НАТУРАЛЬНЫХ ЧИСЕЛ (MUL_NN_N):")
    print("   Лучший случай (малые числа):")
    print(f"     {small1} * {small2} = {small1.MUL_NN_N(small2)}")
    print("   Средний случай (средние числа):")
    print(f"     {Natural('12')} * {Natural('34')} = {Natural('12').MUL_NN_N(Natural('34'))}")
    print("   Худший случай (большие числа):")
    print(f"     {Natural('999')} * {Natural('999')} = {Natural('999').MUL_NN_N(Natural('999'))}")

    print("\n9. ВЫЧИТАНИЕ УМНОЖЕННОГО ЧИСЛА (SUB_NDN_N):")
    print("   Лучший случай (малые числа):")
    print(f"     {Natural('10')} - ({Natural('2')} * 3) = {Natural('10').SUB_NDN_N(Natural('2'), 3)}")
    print("   Средний случай (случайные числа):")
    print(f"     {Natural('100')} - ({Natural('15')} * 4) = {Natural('100').SUB_NDN_N(Natural('15'), 4)}")
    print("   Худший случай (большие числа):")
    print(f"     {Natural('1000')} - ({Natural('99')} * 9) = {Natural('1000').SUB_NDN_N(Natural('99'), 9)}")

    print("\n10. НАХОЖДЕНИЕ ЦИФРЫ ЧАСТНОГО (DIV_NN_Dk):")
    print("   Лучший случай (делится нацело):")
    print(f"     {Natural('100')} / {Natural('10')}, позиция 0: {Natural('100').DIV_NN_Dk(Natural('10'), 0)}")
    print("   Средний случай (обычное деление):")
    print(f"     {Natural('256')} / {Natural('16')}, позиция 0: {Natural('256').DIV_NN_Dk(Natural('16'), 0)}")
    print("   Худший случай (сложное деление):")
    print(f"     {Natural('1000')} / {Natural('33')}, позиция 0: {Natural('1000').DIV_NN_Dk(Natural('33'), 0)}")

    print("\n11. ДЕЛЕНИЕ НАТУРАЛЬНЫХ ЧИСЕЛ (DIV_NN_N):")
    print("   Лучший случай (делится нацело):")
    print(f"     {Natural('100')} / {Natural('10')} = {Natural('100').DIV_NN_N(Natural('10'))}")
    print("   Средний случай (обычное деление):")
    print(f"     {Natural('256')} / {Natural('16')} = {Natural('256').DIV_NN_N(Natural('16'))}")
    print("   Худший случай (с остатком):")
    print(f"     {Natural('1000')} / {Natural('33')} = {Natural('1000').DIV_NN_N(Natural('33'))}")

    print("\n12. ОСТАТОК ОТ ДЕЛЕНИЯ (MOD_NN_N):")
    print("   Лучший случай (делится нацело):")
    print(f"     {Natural('100')} % {Natural('10')} = {Natural('100').MOD_NN_N(Natural('10'))}")
    print("   Средний случай (обычное деление):")
    print(f"     {Natural('256')} % {Natural('16')} = {Natural('256').MOD_NN_N(Natural('16'))}")
    print("   Худший случай (максимальный остаток):")
    print(f"     {Natural('1000')} % {Natural('33')} = {Natural('1000').MOD_NN_N(Natural('33'))}")

    print("\n13. НОД НАТУРАЛЬНЫХ ЧИСЕЛ (GCF_NN_N):")
    print("   Лучший случай (одно число делит другое):")
    print(f"     НОД({Natural('100')}, {Natural('10')}) = {Natural('100').GCF_NN_N(Natural('10'))}")
    print("   Средний случай (взаимно простые):")
    print(f"     НОД({Natural('17')}, {Natural('13')}) = {Natural('17').GCF_NN_N(Natural('13'))}")
    print("   Худший случай (сложный НОД):")
    print(f"     НОД({Natural('1071')}, {Natural('462')}) = {Natural('1071').GCF_NN_N(Natural('462'))}")

    print("\n14. НОК НАТУРАЛЬНЫХ ЧИСЕЛ (LCM_NN_N):")
    print("   Лучший случай (одно число кратно другому):")
    print(f"     НОК({Natural('5')}, {Natural('10')}) = {Natural('5').LCM_NN_N(Natural('10'))}")
    print("   Средний случай (соприостальные числа):")
    print(f"     НОК({Natural('12')}, {Natural('18')}) = {Natural('12').LCM_NN_N(Natural('18'))}")
    print("   Худший случай (взаимно простые):")
    print(f"     НОК({Natural('17')}, {Natural('13')}) = {Natural('17').LCM_NN_N(Natural('13'))}")

    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1000
    print(f"\n✓ Тестирование класса Natural завершено")
    print(f"  Время выполнения: {elapsed_ms:.2f} мс\n")


def test_integer():
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА INTEGER")
    print("=" * 60)
    
    start_time = time.time()

    # Лучшие/средние/худшие случаи
    pos_small = Integer("123")
    neg_small = Integer("-123")
    pos_large = Integer("999999")
    neg_large = Integer("-999999")
    zero = Integer("0")

    print("\n1. АБСОЛЮТНОЕ ЗНАЧЕНИЕ (ABS_Z_N):")
    print("   Лучший случай (положительное):")
    print(f"     |{pos_small}| = {pos_small.ABS_Z_N()}")
    print("   Средний случай (случайное число):")
    random_med = Integer("-456")
    print(f"     |{random_med}| = {random_med.ABS_Z_N()}")
    print("   Худший случай (отрицательное):")
    print(f"     |{neg_large}| = {neg_large.ABS_Z_N()}")

    print("\n2. ЗНАК ЧИСЛА (POZ_Z_D):")
    print("   Лучший случай (положительное):")
    print(f"     знак({pos_small}) = {pos_small.POZ_Z_D()}")
    print("   Средний случай (случайное число):")
    random_med = Integer("-789")
    print(f"     знак({random_med}) = {random_med.POZ_Z_D()}")
    print("   Худший случай (ноль):")
    print(f"     знак({zero}) = {zero.POZ_Z_D()}")

    print("\n3. СМЕНА ЗНАКА (MUL_ZM_Z):")
    print("   Лучший случай (положительное):")
    print(f"     -{pos_small} = {pos_small.MUL_ZM_Z()}")
    print("   Средний случай (случайное число):")
    random_med = Integer("321")
    print(f"     -{random_med} = {random_med.MUL_ZM_Z()}")
    print("   Худший случай (отрицательное):")
    print(f"     -{neg_large} = {neg_large.MUL_ZM_Z()}")

    print("\n4. ПРЕОБРАЗОВАНИЕ NATURAL -> INTEGER (TRANS_N_Z):")
    print("   Лучший случай (малое натуральное число):")
    nat_small = Natural("5")
    print(f"     Natural('{nat_small}') -> Integer: {Integer.TRANS_N_Z(nat_small)}")
    print("   Средний случай (среднее натуральное число):")
    nat_med = Natural("456")
    print(f"     Natural('{nat_med}') -> Integer: {Integer.TRANS_N_Z(nat_med)}")
    print("   Худший случай (ноль):")
    nat_zero = Natural("0")
    print(f"     Natural('{nat_zero}') -> Integer: {Integer.TRANS_N_Z(nat_zero)}")

    print("\n5. ПРЕОБРАЗОВАНИЕ INTEGER -> NATURAL (TRANS_Z_N):")
    print("   Лучший случай (положительное число):")
    int_pos = Integer("123")
    print(f"     Integer('{int_pos}') -> Natural: {int_pos.TRANS_Z_N()}")
    print("   Средний случай (ноль):")
    int_zero = Integer("0")
    print(f"     Integer('{int_zero}') -> Natural: {int_zero.TRANS_Z_N()}")
    print("   Худший случай (отрицательное число):")
    int_neg = Integer("-123")
    try:
        result = int_neg.TRANS_Z_N()
        print(f"     Integer('{int_neg}') -> Natural: {result}")
    except ValueError as e:
        print(f"     Integer('{int_neg}') -> Natural: ошибка (ожидаемо) - {e}")

    print("\n6. СЛОЖЕНИЕ ЦЕЛЫХ ЧИСЕЛ (ADD_ZZ_Z):")
    print("   Лучший случай (оба положительные):")
    print(f"     {pos_small} + {Integer('50')} = {pos_small.ADD_ZZ_Z(Integer('50'))}")
    print("   Средний случай (смешанные знаки):")
    print(f"     {pos_small} + {neg_small} = {pos_small.ADD_ZZ_Z(neg_small)}")
    print("   Худший случай (оба отрицательные):")
    print(f"     {Integer('-100')} + {Integer('-50')} = {Integer('-100').ADD_ZZ_Z(Integer('-50'))}")

    print("\n7. ВЫЧИТАНИЕ ЦЕЛЫХ ЧИСЕЛ (SUB_ZZ_Z):")
    print("   Лучший случай (положительные числа):")
    print(f"     {Integer('100')} - {Integer('30')} = {Integer('100').SUB_ZZ_Z(Integer('30'))}")
    print("   Средний случай (смешанные знаки):")
    print(f"     {pos_small} - {neg_small} = {pos_small.SUB_ZZ_Z(neg_small)}")
    print("   Худший случай (результат отрицательный):")
    print(f"     {Integer('10')} - {Integer('50')} = {Integer('10').SUB_ZZ_Z(Integer('50'))}")

    print("\n8. УМНОЖЕНИЕ ЦЕЛЫХ ЧИСЕЛ (MUL_ZZ_Z):")
    print("   Лучший случай (оба положительные):")
    print(f"     {Integer('12')} * {Integer('5')} = {Integer('12').MUL_ZZ_Z(Integer('5'))}")
    print("   Средний случай (разные знаки):")
    print(f"     {Integer('12')} * {Integer('-5')} = {Integer('12').MUL_ZZ_Z(Integer('-5'))}")
    print("   Худший случай (большие отрицательные):")
    print(f"     {Integer('-123')} * {Integer('-45')} = {Integer('-123').MUL_ZZ_Z(Integer('-45'))}")

    print("\n9. ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ (DIV_ZZ_Z):")
    print("   Лучший случай (делится нацело):")
    print(f"     {Integer('100')} / {Integer('10')} = {Integer('100').DIV_ZZ_Z(Integer('10'))}")
    print("   Средний случай (не делится нацело):")
    print(f"     {Integer('25')} / {Integer('7')} = {Integer('25').DIV_ZZ_Z(Integer('7'))}")
    print("   Худший случай (отрицательные числа):")
    print(f"     {Integer('-25')} / {Integer('-7')} = {Integer('-25').DIV_ZZ_Z(Integer('-7'))}")

    print("\n10. ОСТАТОК ОТ ДЕЛЕНИЯ (MOD_ZZ_Z):")
    print("   Лучший случай (делится нацело):")
    print(f"     {Integer('100')} % {Integer('10')} = {Integer('100').MOD_ZZ_Z(Integer('10'))}")
    print("   Средний случай (обычный остаток):")
    print(f"     {Integer('25')} % {Integer('7')} = {Integer('25').MOD_ZZ_Z(Integer('7'))}")
    print("   Худший случай (отрицательное делимое):")
    print(f"     {Integer('-25')} % {Integer('7')} = {Integer('-25').MOD_ZZ_Z(Integer('7'))}")

    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1000
    print(f"\n✓ Тестирование класса Integer завершено")
    print(f"  Время выполнения: {elapsed_ms:.2f} мс\n")


def test_rational():
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА RATIONAL")
    print("=" * 60)
    
    start_time = time.time()

    # Лучшие/средние/худшие случаи
    simple = Rational("1/2")
    complex_frac = Rational("123456/789012")
    integer = Rational("5/1")
    zero = Rational("0/1")
    negative = Rational("-3/4")

    print("\n1. СОКРАЩЕНИЕ (RED_Q_Q):")
    print("   Лучший случай (уже сокращена):")
    print(f"     {simple} → {simple.RED_Q_Q()}")
    print("   Средний случай (случайная дробь):")
    random_med = Rational("36/48")
    print(f"     {random_med} → {random_med.RED_Q_Q()}")
    print("   Худший случай (сложное сокращение):")
    print(f"     {Rational('123456/246912')} → {Rational('123456/246912').RED_Q_Q()}")

    print("\n2. ПРОВЕРКА НА ЦЕЛОЕ ЧИСЛО (INT_Q_B):")
    print("   Лучший случай (целое):")
    print(f"     {integer} целое число? {integer.INT_Q_B()}")
    print("   Средний случай (случайная дробь):")
    random_med = Rational("7/3")
    print(f"     {random_med} целое число? {random_med.INT_Q_B()}")
    print("   Худший случай (дробь):")
    print(f"     {complex_frac} целое число? {complex_frac.INT_Q_B()}")

    print("\n3. СЛОЖЕНИЕ (ADD_QQ_Q):")
    print("   Лучший случай (одинаковые знаменатели):")
    print(f"     {simple} + {Rational('1/4')} = {simple.ADD_QQ_Q(Rational('1/4'))}")
    print("   Средний случай (случайные дроби):")
    random_med1, random_med2 = Rational("2/5"), Rational("3/7")
    print(f"     {random_med1} + {random_med2} = {random_med1.ADD_QQ_Q(random_med2)}")
    print("   Худший случай (большие взаимно простые знаменатели):")
    print(f"     {Rational('1/123')} + {Rational('1/456')} = {Rational('1/123').ADD_QQ_Q(Rational('1/456'))}")

    print("\n4. ПРЕОБРАЗОВАНИЕ INTEGER -> RATIONAL (TRANS_Z_Q):")
    print("   Лучший случай (положительное целое):")
    int_num = Integer("5")
    print(f"     Integer('{int_num}') -> Rational: {Rational.TRANS_Z_Q(int_num)}")
    print("   Средний случай (большое целое число):")
    int_med = Integer("789")
    print(f"     Integer('{int_med}') -> Rational: {Rational.TRANS_Z_Q(int_med)}")
    print("   Худший случай (отрицательное целое):")
    int_neg = Integer("-123")
    print(f"     Integer('{int_neg}') -> Rational: {Rational.TRANS_Z_Q(int_neg)}")

    print("\n5. ПРЕОБРАЗОВАНИЕ RATIONAL -> INTEGER (TRANS_Q_Z):")
    print("   Лучший случай (целое число):")
    frac_whole = Rational("5/1")
    print(f"     Rational('{frac_whole}') -> Integer: {frac_whole.TRANS_Q_Z()}")
    print("   Средний случай (целое число со сложным представлением):")
    frac_whole2 = Rational("100/10").RED_Q_Q()
    print(f"     Rational('100/10').RED_Q_Q() -> Integer: {frac_whole2.TRANS_Q_Z()}")
    print("   Худший случай (дробь, не являющаяся целым):")
    frac_non_whole = Rational("5/3")
    try:
        print(f"     Rational('{frac_non_whole}') -> Integer: {frac_non_whole.TRANS_Q_Z()}")
    except ValueError as e:
        print(f"     Rational('{frac_non_whole}') -> Integer: ошибка (ожидаемо) - {e}")

    print("\n6. ВЫЧИТАНИЕ (SUB_QQ_Q):")
    print("   Лучший случай (одинаковые знаменатели):")
    print(f"     {Rational('5/4')} - {simple} = {Rational('5/4').SUB_QQ_Q(simple)}")
    print("   Средний случай (случайные дроби):")
    print(f"     {Rational('7/5')} - {Rational('2/3')} = {Rational('7/5').SUB_QQ_Q(Rational('2/3'))}")
    print("   Худший случай (результат может быть отрицательным):")
    print(f"     {Rational('1/10')} - {Rational('1/5')} = {Rational('1/10').SUB_QQ_Q(Rational('1/5'))}")

    print("\n7. УМНОЖЕНИЕ (MUL_QQ_Q):")
    print("   Лучший случай (простые дроби):")
    print(f"     {simple} * {Rational('2/3')} = {simple.MUL_QQ_Q(Rational('2/3'))}")
    print("   Средний случай (случайные дроби):")
    print(f"     {Rational('3/4')} * {Rational('4/5')} = {Rational('3/4').MUL_QQ_Q(Rational('4/5'))}")
    print("   Худший случай (результат требует сокращения):")
    print(f"     {Rational('6/8')} * {Rational('4/9')} = {Rational('6/8').MUL_QQ_Q(Rational('4/9'))}")

    print("\n8. ДЕЛЕНИЕ (DIV_QQ_Q):")
    print("   Лучший случай (простые дроби):")
    print(f"     {simple} / {Rational('1/4')} = {simple.DIV_QQ_Q(Rational('1/4'))}")
    print("   Средний случай (случайные дроби):")
    print(f"     {Rational('3/4')} / {Rational('4/5')} = {Rational('3/4').DIV_QQ_Q(Rational('4/5'))}")
    print("   Худший случай (отрицательные дроби):")
    print(f"     {Rational('-1/2')} / {Rational('3/4')} = {Rational('-1/2').DIV_QQ_Q(Rational('3/4'))}")

    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1000
    print(f"\n✓ Тестирование класса Rational завершено")
    print(f"  Время выполнения: {elapsed_ms:.2f} мс\n")


def test_polynomial():
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ КЛАССА POLYNOMIAL")
    print("=" * 60)
    
    start_time = time.time()

    print("\nИНИЦИАЛИЗАЦИЯ ПОЛИНОМОВ (от старшей степени к младшей):")
    
    # Лучшие случаи - простые полиномы
    p_simple1 = Polynomial("x^2 + 2*x + 1")
    p_simple2 = Polynomial("x + 1")
    
    # Средние случаи
    p_medium1 = Polynomial("3*x^3 + 2*x^2 + 5/2*x + 1/3")
    p_medium2 = Polynomial("2*x^2 + 3/4*x + 5")
    
    # Худшие случаи
    p_complex1 = Polynomial("x^5 + 123/456*x^4 + 789/101*x^3 + 2/3*x^2 + 1/2*x + 1")
    p_sparse = Polynomial("x^100 + 1")

    print("   Лучший случай (простой полином):")
    print(f"     'x^2 + 2*x + 1' → {p_simple1}")
    print("   Средний случай (случайный полином):")
    random_med = Polynomial("2*x^3 + 3/4*x^2 + 5*x + 7")
    print(f"     '2*x^3 + 3/4*x^2 + 5*x + 7' → {random_med}")
    print("   Худший случай (высокая степень):")
    print(f"     'x^100 + 1' → {p_sparse}")

    print("\n1. СЛОЖЕНИЕ (ADD_PP_P):")
    print("   Лучший случай (одинаковые степени):")
    result = p_simple1.ADD_PP_P(p_simple1)
    print(f"     {p_simple1} + {p_simple1} = {result}")
    print("   Средний случай (случайные полиномы):")
    random_med1 = Polynomial("x^2 + 3*x + 2")
    random_med2 = Polynomial("2*x^2 + x + 4")
    result = random_med1.ADD_PP_P(random_med2)
    print(f"     {random_med1} + {random_med2} = {result}")
    print("   Худший случай (разные степени):")
    result = p_complex1.ADD_PP_P(p_medium2)
    print(f"     {p_complex1} + {p_medium2} = {result}")

    print("\n2. ВЫЧИТАНИЕ (SUB_PP_P):")
    print("   Лучший случай (малые полиномы):")
    result = p_simple1.SUB_PP_P(p_simple2)
    print(f"     {p_simple1} - {p_simple2} = {result}")
    print("   Средний случай (случайные полиномы):")
    random_med1 = Polynomial("3*x^2 + 2*x + 1")
    random_med2 = Polynomial("x^2 + 4*x + 2")
    result = random_med1.SUB_PP_P(random_med2)
    print(f"     {random_med1} - {random_med2} = {result}")
    print("   Худший случай (аннулирование):")
    result = p_medium1.SUB_PP_P(p_medium1)
    print(f"     {p_medium1} - {p_medium1} = {result}")

    print("\n3. УМНОЖЕНИЕ НА РАЦИОНАЛЬНОЕ ЧИСЛО (MUL_PQ_P):")
    q_simple = Rational("2/1")
    print("   Лучший случай (умножение на 2):")
    result = p_simple1.MUL_PQ_P(q_simple)
    print(f"     {p_simple1} * {q_simple} = {result}")
    print("   Средний случай (случайный полином):")
    random_med = Polynomial("x^2 + 2*x + 3")
    random_q = Rational("3/2")
    result = random_med.MUL_PQ_P(random_q)
    print(f"     {random_med} * {random_q} = {result}")
    print("   Худший случай (сложная дробь):")
    result = p_complex1.MUL_PQ_P(Rational("123/456"))
    print(f"     {p_complex1} * 123/456 = {result}")

    print("\n4. УМНОЖЕНИЕ НА x^k (MUL_Pxk_P):")
    print("   Лучший случай (k=1):")
    result = p_simple1.MUL_Pxk_P(Natural("1"))
    print(f"     {p_simple1} * x^1 = {result}")
    print("   Средний случай (случайный полином):")
    random_med = Polynomial("2*x^2 + 3*x + 1")
    result = random_med.MUL_Pxk_P(Natural("2"))
    print(f"     {random_med} * x^2 = {result}")
    print("   Худший случай (большой k):")
    result = p_sparse.MUL_Pxk_P(Natural("10"))
    print(f"     {p_sparse} * x^10 = {result}")

    print("\n5. СТАРШИЙ КОЭФФИЦИЕНТ (LED_P_Q):")
    print("   Лучший случай (простой коэффициент):")
    print(f"     LED({p_simple1}) = {p_simple1.LED_P_Q()}")
    print("   Средний случай (случайный полином):")
    random_med = Polynomial("5/2*x^3 + 3*x^2 + 7/4*x + 2")
    print(f"     LED({random_med}) = {random_med.LED_P_Q()}")
    print("   Худший случай (сложная дробь):")
    print(f"     LED({p_complex1}) = {p_complex1.LED_P_Q()}")

    print("\n6. СТЕПЕНЬ МНОГОЧЛЕНА (DEG_P_N):")
    print("   Лучший случай (низкая степень):")
    print(f"     DEG({p_simple1}) = {p_simple1.DEG_P_N()}")
    print("   Средний случай (случайный полином):")
    random_med = Polynomial("x^4 + 2*x^3 + 3*x^2 + 4*x + 5")
    print(f"     DEG({random_med}) = {random_med.DEG_P_N()}")
    print("   Худший случай (высокая степень):")
    print(f"     DEG({p_sparse}) = {p_sparse.DEG_P_N()}")

    print("\n7. УМНОЖЕНИЕ МНОГОЧЛЕНОВ (MUL_PP_P):")
    print("   Лучший случай (малые полиномы):")
    result = p_simple1.MUL_PP_P(p_simple2)
    print(f"     {p_simple1} * {p_simple2} = {result}")
    print("   Средний случай (случайные полиномы):")
    random_med1 = Polynomial("x^2 + 2*x + 1")
    random_med2 = Polynomial("x + 3")
    result = random_med1.MUL_PP_P(random_med2)
    print(f"     {random_med1} * {random_med2} = {result}")
    print("   Худший случай (высокие степени):")
    result = p_medium1.MUL_PP_P(p_medium2)
    print(f"     {p_medium1} * {p_medium2} = {result}")

    print("\n8. ДЕЛЕНИЕ МНОГОЧЛЕНОВ (DIV_PP_P):")
    print("   Лучший случай (делится нацело):")
    p_divisible = Polynomial("x^2 + 2*x + 1")
    p_divisor = Polynomial("x + 1")
    try:
        result = p_divisible.DIV_PP_P(p_divisor)
        print(f"     {p_divisible} / {p_divisor} = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")
    print("   Средний случай (случайные полиномы):")
    random_med1 = Polynomial("2*x^3 + 3*x^2 + 4*x + 1")
    random_med2 = Polynomial("x + 1")
    try:
        result = random_med1.DIV_PP_P(random_med2)
        print(f"     {random_med1} / {random_med2} = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")
    print("   Худший случай (с остатком):")
    try:
        result = p_medium1.DIV_PP_P(p_medium2)
        print(f"     {p_medium1} / {p_medium2} = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")

    print("\n9. ОСТАТОК ОТ ДЕЛЕНИЯ (MOD_PP_P):")
    print("   Лучший случай (делится нацело):")
    try:
        result = p_divisible.MOD_PP_P(p_divisor)
        print(f"     {p_divisible} mod {p_divisor} = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")
    print("   Средний случай (случайные полиномы):")
    try:
        result = random_med1.MOD_PP_P(random_med2)
        print(f"     {random_med1} mod {random_med2} = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")
    print("   Худший случай (ненулевой остаток):")
    try:
        result = p_medium1.MOD_PP_P(p_medium2)
        print(f"     {p_medium1} mod {p_medium2} = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")

    print("\n10. НОД МНОГОЧЛЕНОВ (GCF_PP_P):")
    print("   Лучший случай (простые полиномы):")
    try:
        result = p_simple1.GCF_PP_P(p_simple2)
        print(f"     НОД({p_simple1}, {p_simple2}) = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")
    print("   Средний случай (случайные полиномы):")
    random_med1 = Polynomial("x^2 + 3*x + 2")
    random_med2 = Polynomial("x^2 + 4*x + 4")
    try:
        result = random_med1.GCF_PP_P(random_med2)
        print(f"     НОД({random_med1}, {random_med2}) = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")
    print("   Худший случай (сложные полиномы):")
    try:
        result = p_medium1.GCF_PP_P(p_medium2)
        print(f"     НОД({p_medium1}, {p_medium2}) = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")

    print("\n11. ПРОИЗВОДНАЯ (DER_P_P):")
    print("   Лучший случай (простой полином):")
    result = p_simple1.DER_P_P()
    print(f"     D/dx({p_simple1}) = {result}")
    print("   Средний случай (случайный полином):")
    random_med = Polynomial("3*x^3 + 2*x^2 + x + 5")
    result = random_med.DER_P_P()
    print(f"     D/dx({random_med}) = {result}")
    print("   Худший случай (сложный полином):")
    result = p_complex1.DER_P_P()
    print(f"     D/dx({p_complex1}) = {result}")

    print("\n12. ПРЕОБРАЗОВАНИЕ - КРАТНЫЕ КОРНИ В ПРОСТЫЕ (NMR_P_P):")
    print("   Лучший случай (уже простые корни):")
    try:
        result = p_simple1.NMR_P_P()
        print(f"     NMR({p_simple1}) = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")
    print("   Средний случай (случайный полином):")
    random_med = Polynomial("x^2 + 2*x + 1")
    try:
        result = random_med.NMR_P_P()
        print(f"     NMR({random_med}) = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")
    print("   Худший случай (кратные корни):")
    p_multiple_roots = Polynomial("x^3 + 3*x^2 + 3*x + 1")  # (x+1)³
    try:
        result = p_multiple_roots.NMR_P_P()
        print(f"     NMR({p_multiple_roots}) = {result}")
    except Exception as e:
        print(f"     Ошибка: {e}")

    print("\n13. ВЫНЕСЕНИЕ НОК/НОД (FAC_P_Q):")
    print("   Лучший случай (целые коэффициенты):")
    print(f"     FAC({p_simple1}) = {p_simple1.FAC_P_Q()}")
    print("   Средний случай (случайный полином):")
    random_med = Polynomial("2*x^2 + 4*x + 6")
    print(f"     FAC({random_med}) = {random_med.FAC_P_Q()}")
    print("   Худший случай (дробные коэффициенты):")
    print(f"     FAC({p_complex1}) = {p_complex1.FAC_P_Q()}")

    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1000
    print(f"\n✓ Тестирование класса Polynomial завершено")
    print(f"  Время выполнения: {elapsed_ms:.2f} мс\n")


def main():
    print("\n" + "=" * 60)
    print("ВИЗУАЛЬНОЕ ТЕСТИРОВАНИЕ ВСЕХ МОДУЛЕЙ С АНАЛИЗОМ СЛУЧАЕВ")
    print("=" * 60 + "\n")
    
    total_start_time = time.time()

    try:
        test_natural()
    except Exception as e:
        print(f"Ошибка при тестировании Natural: {e}\n")

    try:
        test_integer()
    except Exception as e:
        print(f"Ошибка при тестировании Integer: {e}\n")

    try:
        test_rational()
    except Exception as e:
        print(f"Ошибка при тестировании Rational: {e}\n")

    try:
        test_polynomial()
    except Exception as e:
        print(f"Ошибка при тестировании Polynomial: {e}\n")

    total_end_time = time.time()
    total_elapsed_ms = (total_end_time - total_start_time) * 1000
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ С АНАЛИЗОМ СЛУЧАЕВ ЗАВЕРШЕНО!")
    print(f"Общее время выполнения: {total_elapsed_ms:.2f} мс")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()