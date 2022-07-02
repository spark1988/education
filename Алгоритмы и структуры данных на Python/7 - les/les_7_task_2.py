import sys


def show_size(x, level=0):
    ''' Добавил в функцию сложение всех затрат памяти
        и возврат общей суммы затраченной памяти '''
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par

# Урок 1, задача № 1. Найти сумму и произведение цифр трехзначного
# числа, которое вводит пользователь.

a = input('Введите трехзначное число: ')

x = int(a[0])
y = int(a[1])
z = int(a[2])

sum_l = x + y + z
mult = x * y * z

sum_member = sys.getsizeof(a) + sys.getsizeof(x) + sys.getsizeof(y) + sys.getsizeof(z) + sys.getsizeof(
    sum_l) + sys.getsizeof(mult)
print('В программе задействовано байт памяти: {}'.format(sum_member))