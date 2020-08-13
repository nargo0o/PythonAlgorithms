'''
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
'''
# https://drive.google.com/file/d/1UoEQ2g8S6EgtHPjezz5z_GIRseVXMthB/view?usp=sharing


n = int(input('Количество элементов: '))

a = 1
s = 0
while n > 0:
    s = s + a
    a = a / -2
    n = n - 1

print(s)
