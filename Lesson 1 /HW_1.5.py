# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1l-u9ttCgetXABY2gdzPbvcZeoXVbu08g/view?usp=sharing


a = int(input('Введите первое уникальное число: '))
b = int(input('Введите второе уникальное число: '))
c = int(input('Введите третье уникальное число: '))

if c > a > b or b > a > c:
    print(f'Среднее число: {a}')
elif a > c > b or b > c > a:
    print(f'Среднее число: {c}')
else:
    print(f'Среднее число: {b}')
