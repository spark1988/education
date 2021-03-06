# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные
# (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять
# поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
from itertools import zip_longest

class Matrix():

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return self.matrix
# return f'{self.matrix[0]}\n{self.matrix[1]}'


    def __add__(self, other):
        s = []
        for i in range(len(self.matrix)):  # если в range() задан только один аргумент, отсчёт будет от 0

            # s.append(self.matrix[i] + other[i + 2])
            result = [sum(n) for n in zip_longest(self.matrix[i], other[i + 2], fillvalue=0)]
            s.append(result)
        return s


        # a = self.matrix[0]
        # b = self.matrix[1]
        # c = other[2]
        # d = other[3]
        # c.extend([0, ] * (len(d) - len(c)))
        # d.extend([0, ] * (len(c) - len(d)))
        # a.extend([0, ] * (len(b) - len(a)))
        # b.extend([0, ] * (len(a) - len(b)))
        # data = []
        # data.append(list(map(sum, zip(a, c))))
        # data.append(list(map(sum, zip(b, d))))
        # return data

matrica = [[1, 2, 4, 5], [7, 4, 5, 7]]
matrica2 =[[4, 33, 22, 6], [6, 4, 7, 9]]
matrica3 =[[4, 20, 11], [2, 3, 6]]
matrica4 =[[4, 20, 11], [2, 3, 6]]



m = Matrix(matrica)

print(matrica , matrica2)
print(m.__add__(matrica + matrica2))

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
class Clothes():
    def __init__(self, name):
        self.name = name

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    @property
    def consumption(self):
        result_coat = (self.size/6.5 + 0.5)
        return result_coat

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        result_suit = (2 * self.height + 0.3)
        return result_suit

c = Coat(23)
b = Suit(45)

print(c.consumption)
print(b.consumption)

# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell():
    def __init__(self,num):
        self.num = num

    def __add__(self, other):

        result = self.num + other
        return round(result)

    def __sub__(self, other):
        result = self.num - other
        if result > 0:

            return result
        else:
            print('Клеток не может быть < 0')

    def __mul__(self, other):
        result = self.num * other
        return round(result)

    def __truediv__(self, other):
        result = self.num // other
        if result > 0:

            return result
        else:
            print(f'нет целых: {result}')

    def make_order(self, lenght_line):
        result = self.num // lenght_line
        left_of_line = self.num % lenght_line
        print ((('*' * lenght_line) + '\n') * result + ('*' * left_of_line))

c = Cell(12)

print(c / 3)
print(c * 3)
print(c - 3)
print(c + 3)
print(12//5)
c.make_order(5)
