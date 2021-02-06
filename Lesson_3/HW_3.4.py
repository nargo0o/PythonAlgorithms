# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random

SIZE = 10
MIN_ITEM = - 20
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = 0
for i in range(SIZE):
    if array[i] < array[min_]:
        min_ = i

if array[min_] < 0:
    min_max = min_
    for j in range(SIZE):
        if array[min_max] < array[j] < 0:
            max_min = j
    print(f"Макс мин число: {array[min_max]}")
