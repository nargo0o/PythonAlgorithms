'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, надо вывести 6843.
'''
# https://drive.google.com/file/d/1UoEQ2g8S6EgtHPjezz5z_GIRseVXMthB/view?usp=sharing


def rev_num(a, b = 0):   # a-само число, которое // 10 каждый раз, b-преобразованное число, которое * 10
    if a == 0:
        return b
    if a // 10 == 0:
        return b * 10 + a
    else:
        return rev_num(a // 10, (10 * b) + (a % 10))

num = int(input('Введи число: '))
z = rev_num(num)
print(z)