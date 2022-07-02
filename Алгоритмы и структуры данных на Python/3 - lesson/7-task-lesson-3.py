# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

List = [1, 2, 3, 9, 5, 6, 7, 8, 2, -2]
result = []

min_num_1 = min(map(int, List))
List.remove(min_num_1)
result.append(min_num_1)
min_num_2 = min(map(int, List))
result.append(min_num_2)

print(List)
print(result)