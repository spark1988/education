# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
ask = int(input('введите кол-во элементов для ряда 1, -0.5, 0.25, -0.125,…'))
s = 0
num = 1
while s < ask:
    print(num)
    num /= -2
    s += 1