# 8. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('1 число'))
b = int(input('2 число'))
c = int(input('3 число'))
#логически проверяем 2 возможных варианта при котором A - 1 ое число может быть средним
if a > b and a < c:
    print(f'1 число {a} является средним среди {b} {c}')

if a < b and a > c:
    print(f'1 число {a} является средним среди {b} {c}')
#логически проверяем 2 возможных варианта при котором B - 2 ое число может быть средним
elif b > a and b < c:
    print(f'2 число {b} является средним среди {a} {c}')
elif b < a and b > c:
    print(f'2 число {b} является средним среди {a} {c}')
#логически проверяем 2 возможных варианта при котором C - 3 ое число может быть средним
elif c > a and c < b:
    print(f'3 число {c} является средним среди {a} {b}')
elif c < a and c > b:
    print(f'3 число {c} является средним среди {a} {b}')
#выводим при равных числах
else:
    print('вы ввели одинаковые числа')
