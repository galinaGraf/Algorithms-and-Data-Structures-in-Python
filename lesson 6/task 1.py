# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна
# определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
import sys

company = namedtuple('Company', ['name', 'avg_profit'])
all_companies = set()
quarters = []
PERIOD = 4
avg_profit = 0
n = int(input("Количество компаний:  "))
s = 0
for i in range(n):
    name = input(str(i+1) + "-ая компания: ")
    for j in range(PERIOD):
        quarters.append(float(input(f'Прибыль за {j + 1}-й квартал: ')))
        avg_profit += quarters[j]

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

print(sys.getsizeof(comp)) #56
print(sys.getsizeof(all_companies)) #216
print(sys.getsizeof(quarters)) #120
print(sys.getsizeof(PERIOD)) #28
print(sys.getsizeof(n)) #28
print(sys.getsizeof(s)) #24
print(sys.getsizeof(i)) #28
print(sys.getsizeof(name)) #51
print(sys.getsizeof(company)) #904
print(sys.getsizeof(j)) #28
print(sys.getsizeof(avg_common)) #24
print(sys.getsizeof(avg_profit)) #24
# версия Python 3.10.2
# 64-разрядная операционная система, процессор x64
#Количество компаний:  2
#1-ая компания: sd
#Прибыль за 1-й квартал: 1
#Прибыль за 2-й квартал: 2
#Прибыль за 3-й квартал: 3
#Прибыль за 4-й квартал: 4
#2-ая компания: ds
#Прибыль за 1-й квартал: 4
#Прибыль за 2-й квартал: 5
#Прибыль за 3-й квартал: 6
#Прибыль за 4-й квартал: 7
#Средняя прибыль всех предприятий: 15.0
#Прибыль выше среднего у компании: ds
#Прибыль выше среднего у компании: sd
