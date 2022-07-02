# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).

array_test = [i for i in range(32)]
random.shuffle(array_test) #изначальный массив неотсортированный
print(array_test)
def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):

        key_item = array[i]

        j = i - 1

        while j >= left and array[j] > key_item:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array

def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:

        for start in range(0, n, size * 2):

            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            array[start:start + len(merged_array)] = merged_array

        size *= 2

    return array

print(timsort(array_test))