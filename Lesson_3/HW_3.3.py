# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = 0
max_ = 0
for i in range(SIZE):
    if array[i] < array[min_]:
        min_ = i
    elif array[i] > array[max_]:
        max_ = i

a = array[min_]
array[min_], array[max_] = array[max_], array[min_]
b = array[max_]

print(array)
