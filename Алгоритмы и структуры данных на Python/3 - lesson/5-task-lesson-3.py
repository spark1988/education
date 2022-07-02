# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
List = [random.randint(-100,10) for _ in range(10)]
min_table = [i for i in List if i < 0]
print(max(min_table))
print(List)
