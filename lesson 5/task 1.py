# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна
# определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

company = namedtuple('Company', ['name', 'avg_profit'])
all_companies = set()

n = int(input("Количество компаний:  "))
s = 0
for i in range(n):
    name = input(str(i+1) + "-ая компания: ")
    pr_1_qv = int(input("прибыль за 1 квартал:  "))
    pr_2_qv = int(input("прибыль за 2 квартал:  "))
    pr_3_qv = int(input("прибыль за 3 квартал:  "))
    pr_4_qv = int(input("прибыль за 4 квартал:  "))
    avg_profit = (pr_1_qv+pr_2_qv+pr_3_qv+pr_4_qv)   # средняя прибыль компании за год

    comp = company(name=name, avg_profit=avg_profit)

    all_companies.add(comp)
    s += avg_profit

avg_common = s / n
print(f'Средняя прибыль всех предприятий: {avg_common}')

for comp in all_companies:
    if comp.avg_profit > avg_common:
        print(f'Прибыль выше среднего у компании: {comp.name} ')

for comp in all_companies:
    if comp.avg_profit < avg_common:
        print(f'Прибыль выше среднего у компании: {comp.name} ')

