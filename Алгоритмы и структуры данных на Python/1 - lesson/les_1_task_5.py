# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter = int(input('введите букву числом '))
#запрашиваем числовое значение буквы алфавита от 1 до 26 

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#получаем из словаря по отработанной схеме значение вычитая - 1 тк отчет в словаре от 0 а не от 1 цы.
print(alphabet[letter-1])