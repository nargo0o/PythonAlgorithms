# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Урок 2. Задача 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… . Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile

# Вариант 1. Пример c циклом while. O(n):


def sum_n(n):
    a = 1
    sum_ = 0
    while n > 0:
        sum_ = sum_ + a
        a = a / -2
        n = n - 1
    return sum_


print(timeit.timeit('sum_n(100)', number=1000, globals=globals()))   #0.021231849000000004
print(timeit.timeit('sum_n(200)', number=1000, globals=globals()))   #0.050700763
print(timeit.timeit('sum_n(400)', number=1000, globals=globals()))   #0.05211061099999999
print(timeit.timeit('sum_n(800)', number=1000, globals=globals()))   #0.12873314400000002
print(timeit.timeit('sum_n(1600)', number=1000, globals=globals()))  #0.228511415

cProfile.run('sum_n(10000)')
#  1    0.001    0.001    0.001    0.001 Task 1.py:9(sum_n)
cProfile.run('sum_n(40000)')
#  1    0.006    0.006    0.006    0.006 Task 1.py:9(sum_n)
cProfile.run('sum_n(160000)')
# 1    0.024    0.024    0.024    0.024 Task 1.py:9(sum_n)



# Вариант 2. Пример с циклом for. O(n):

def sum_loop(n):
    a = 1
    sum_ = 0
    for _ in range(n):
        sum_ += a
        a /= -2
        return sum_


print(timeit.timeit('sum_loop(100)', number=1000, globals=globals()))   #0.0007508189999999998
print(timeit.timeit('sum_loop(200)', number=1000, globals=globals()))   #0.001197567999999996
print(timeit.timeit('sum_loop(400)', number=1000, globals=globals()))   #0.0013287400000000019
print(timeit.timeit('sum_loop(800)', number=1000, globals=globals()))   #0.000620192999999998
print(timeit.timeit('sum_loop(1600)', number=1000, globals=globals()))  #0.0.0017683419999999991

cProfile.run('sum_loop(10000)')
#         1    0.000    0.000    0.000    0.000 Task 1.py:36(sum_loop)
cProfile.run('sum_loop(40000)')
#         1    0.000    0.000    0.000    0.000 Task 1.py:36(sum_loop)
cProfile.run('sum_loop(160000)')
#         1    0.000    0.000    0.000    0.000 Task 1.py:36(sum_loop)


# Вариант 3. Пример с рекурсией. O(n2):


def sum_rec(n):
    a = 1
    sum_ = 0
    if n > 0:
        sum_ += a
        a /= -2
        n -= 1
        return sum_rec(n)
    return sum_

print(timeit.timeit('sum_rec(100)', number=1000, globals=globals()))   #0.030864441
print(timeit.timeit('sum_rec(200)', number=1000, globals=globals()))   #0.05452980099999999
print(timeit.timeit('sum_rec(400)', number=1000, globals=globals()))   #0.122341753
print(timeit.timeit('sum_rec(800)', number=1000, globals=globals()))   #0.279075162


cProfile.run('sum_rec(100)')
#    101/1    0.000    0.000    0.000    0.000 Task 1.py:91(sum_rec)
cProfile.run('sum_rec(400)')
#    401/1    0.000    0.000    0.000    0.000 Task 1.py:91(sum_rec)
cProfile.run('sum_rec(800)')
#     801/1    0.001    0.000    0.001    0.001 Task 1.py:91(sum_rec)


# Вариант 4. Пример с рекурсией, словарем и мемоизации. O(n):


def sum_dict(n):
    sum_d = {0: 0, 1: 1, 2: -0.5}

    def _sum_dict(n):
        if n in sum_d:
            return sum_d[n]
        sum_d[n] = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
        return sum_d[n]

    return _sum_dict(n)


print(timeit.timeit('sum_dict(100)', number=1000, globals=globals()))   #0.0009272040000000009
print(timeit.timeit('sum_dict(200)', number=1000, globals=globals()))   #0.0008065780000000022
print(timeit.timeit('sum_dict(400)', number=1000, globals=globals()))   #0.0008054129999999979
print(timeit.timeit('sum_dict(800)', number=1000, globals=globals()))   #0.0008459700000000014
print(timeit.timeit('sum_dict(1600)', number=1000, globals=globals()))  #0.000997089999999999


cProfile.run('sum_dict(10000)')
#         1    0.000    0.000    0.000    0.000 Task 1.py:61(sum_dict)
cProfile.run('sum_dict(40000)')
#         1    0.000    0.000    0.000    0.000 Task 1.py:61(sum_dict)
cProfile.run('sum_dict(160000)')
#        1    0.000    0.000    0.000    0.000 Task 1.py:61(sum_dict)

'''
Вывод: 
Оптимальным вариантом решения задачи является вариант №4 с примением мемоизации, все запросы выполняются за короткое, одинаковое примерно время. Это связано 
с тем, что рузультат сохраняется в словаре и используется при следующем вызове.
Вариант с рекурсией оказался медленнее всех, потому что он вызывался каждый раз. При увеличении числа, время работы заметно замедлялось, так же возможна ошибка
RecursionError.
'''
