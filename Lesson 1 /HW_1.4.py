# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# https://drive.google.com/file/d/1l-u9ttCgetXABY2gdzPbvcZeoXVbu08g/view?usp=sharing


y = int(input('Введите год: '))

if y % 400 == 0:
    print(f'Високосный год {y}')
elif y % 100 == 0:
    print(f'Не високосный год {y}')
elif y % 4 == 0:
    print(f'Високосный год {y}')
else:
    print(f'Не високосный год - {y}')
