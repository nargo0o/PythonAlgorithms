'''
 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
'''
# https://drive.google.com/file/d/1UoEQ2g8S6EgtHPjezz5z_GIRseVXMthB/view?usp=sharing


n = int(input('Введите натуральное число: '))

a = 1
s_1 = 0
while n > 0:
    s_1 = s_1 + a
    a = a + 1
    n = n - 1

s_2 = n * (n + 1) / 2
if s_1 == s_2:
    print('Равенство выполняется')
else:
    print('Равенство не выполняется')
