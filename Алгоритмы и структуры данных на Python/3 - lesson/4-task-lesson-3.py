# 4. Определить, какое число в массиве встречается чаще всего.
List = [1,2,3,4,5,6,7,8,9,1,2,2, 2]
frequency = max(map(List.count, List))
print(f'{max(a for a in List if List.count(a) == frequency)} то самое число')

print(f'{frequency} количество повторений этого числа в списке')