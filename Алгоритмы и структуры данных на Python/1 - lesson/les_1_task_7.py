# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
# номер которого кратен четырём, но исключение делалось для тех, которые были кратны 100.
# Такие годы были високосными только тогда, когда делились ещё и на 400.
year = int(input('Введите год для проверки високосный ли он'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#проверяем введеный пользователем год на кратность 4 или 400 , но не должно быть кратным 100 и выводим результат Да или Нет
    print('Да этот год високосный')
else:
    print('год не является високосным')