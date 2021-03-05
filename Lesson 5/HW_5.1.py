# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.


import collections


total_comp = int(input("Введите количество предприятий: "))
comp_list = collections.defaultdict(list)
for i in range(total_comp):
    name = input('Введите название предприятия №{}: '.format(i+1))
    for j in range(4):
        income = int(input('Введите прибыль за квартал №{}: '.format(j+1)))
        comp_list[name].append(income)
    avg_income = [sum(comp_list[x])/4 for x in comp_list]
    avg = sum(avg_income) / total_comp
print("Средняя прибыль (за год для всех предприятий): ", avg)
print("Прибыль выше среднего: ")
print([i for i in comp_list if sum(comp_list[i]) / 4 > avg])
print("Прибыль ниже среднего: ")
print([i for i in comp_list if sum(comp_list[i]) / 4 < avg])
