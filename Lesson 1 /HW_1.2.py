# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.
# https://drive.google.com/file/d/1l-u9ttCgetXABY2gdzPbvcZeoXVbu08g/view?usp=sharing


x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'y = {k}x + {b}')
