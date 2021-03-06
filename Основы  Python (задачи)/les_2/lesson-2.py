# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
list_var = ['data', 2021, 3.14, False, None]

for i in list_var:
    print(type(i))
	
	

# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
user_input = input('Введите любые значения через символ , ')

a_list =  list(map(str,user_input.split(',')))

for i in range(1, len(a_list), 2):

    a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]

print(' '.join([str(i) for i in a_list]))




# # 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# # Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# # Напишите решения через list и через dict.

 seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input('Укажи месяц в виде числа и узнай какое это время года: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(f'на дворе {key}')

m = int(input('Выберите месяц числом от 1 - 12: '))
a = [None,'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
if m > 0 and m <=2 or m == 12:

    print(a[m], ' - это Зима')

elif m > 2 and m <= 4:
    print(a[m], ' - это Весна')

elif m > 4 and m <= 7:
    print(a[m], ' - это Лето')

elif m > 7 and m <= 11:
    print(a[m], ' - это Осень')

elif m == 0:
    print('нет месяца 0')

else:
    print('Вы выбрали неправильный месяц, выберите числа от 1 - 12!')
	
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
#
# Если в слово длинное, выводить только первые 10 букв в слове.

user_input = input('Введите любые слова через пробел: ')

user_list = user_input.split()

for count, value in enumerate(user_list):

    print(f'Строка № {count} - {value[0:10]}')
	
	
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. #
# У пользователя необходимо запрашивать новый элемент рейтинга. #
# Если в рейтинге существуют элементы с одинаковыми значениями, #
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

number = int(input("введите число: "))
my_list = [7, 4, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

# 6.

products, order = [], 1

while True:

    name = input('Введите name товара: ')

    price = input('Введите стоимость товара: ')

    quantity = input('Введите quantity: ')

    units = input('Введите units измерения: ')

    products.append((
        order,
        {
            'name': name,
            'price': price,
            'quantity': quantity,
            'units': units
        }
    ))

    order += 1

    question_to_continue = input('Формирование списка завершено? (Да/Нет)) ')
    if question_to_continue == 'Да':
        break

print(products)

analitics = {
    'name': [],
    'price': [],
    'quantity': [],
    'units': []
}

for number, description in products:
    analitics['name'].append(description['name'])
    analitics['price'].append(description['price'])
    analitics['quantity'].append(description['quantity'])
    analitics['units'].append(description['units'])


print(analitics)
