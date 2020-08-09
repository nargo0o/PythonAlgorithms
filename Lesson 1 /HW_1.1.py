# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1l-u9ttCgetXABY2gdzPbvcZeoXVbu08g/view?usp=sharing


abc = int(input('Введите целое трехзначное число (100-999): '))

a = abc // 100
c = abc % 10
b = abc % 100 // 10

print(f'Сумма чисел равна {a + b + c}')
print(f'Произведение чисел равно {a * b * c}')
