# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# https://drive.google.com/file/d/1l-u9ttCgetXABY2gdzPbvcZeoXVbu08g/view?usp=sharing


n = int(input('Введите номер буквы в алфавите от 1 до 26: '))
if n > 0:
    n = ord('a') + n - 1
    print(chr(n))
else:
    print('Нет такой буквы')










