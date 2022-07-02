# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# import random
#
List = [1,2,3,4,5,6,7,8,9]

random.shuffle(List)
print(List)
for i in List:

    if i == max(List):

        b = List.index(i)
        print(List.index(i))

    if i == min(List):

        a = List.index(i)
        print(List.index(i))

List[b], List[a] = List[a], List[b]

print(List)