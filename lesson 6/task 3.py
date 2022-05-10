from collections import namedtuple, deque
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

sort_comp = deque([None])
for comp in all_companies:
    if comp.avg_profit > avg_common:
        sort_comp.append(comp)
    elif comp.avg_profit < avg_common:
        sort_comp.appendleft(comp)

text = 'меньше'
for comp in sort_comp:
    if comp is None:
        text = 'больше'
    else:
        print(f'Компания {comp.name} заработала {text}, чем средняя прибыль - {comp.avg_profit}')

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
print(sys.getsizeof(text)) #86
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

#вывод: код написанный в task2 весит меньше, так как в первом и
# третьем случае использовались множества, которые занимают большую часть свободной памяти