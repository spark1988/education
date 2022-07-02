# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

List = [1, 2, 3, 9, 5, 6, 7, 8, 1, 2, 2, -2]

min_num = min(map(int, List))

max_num = max(map(int, List))

for i in List:
    j = List.index(max_num)
    k = List.index(min_num)
print(List[j + 1:k - 1])
print(sum(List[j + 1:k - 1]))