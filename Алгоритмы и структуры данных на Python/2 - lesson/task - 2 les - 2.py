# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = input('введите число чтобы узнать в нем четные и нечетные числа')
result = list(map(int, number))
b = 0
c = 0

for i in result:
    if i % 2 == 0:
        b += 1
        print( i , 'четная' + '\n')

    if i % 2 !=0:
        c += 1
        print(i, 'нечетная цифра' + '\n')

print(b, 'итого четных цифр')
print(c, 'итого нечетных цифр')