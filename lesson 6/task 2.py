import sys


company = {}
n = int(input("Количество компаний:  "))
s = 0
quarters = []
PERIOD = 4
avg_profit = 0
for i in range(n):
    name = input(str(i+1) + "-ая компания: ")
    for j in range(PERIOD):
        quarters.append(float(input(f'Прибыль за {j + 1}-й квартал: ')))
        avg_profit += quarters[j]   #  прибыль компании за год
        company[name] = avg_profit
        s += avg_profit

avg_common = s / n
print(f'Средняя прибыль всех предприятий: {avg_common}')

for i in company:
    if company[i] > avg_common:
        print(f'Прибыль выше среднего у компании: {i} ')

for i in company:
    if company[i] < avg_common:
        print(f'Прибыль выше среднего у компании: {i} ')


print(sys.getsizeof(quarters)) #120
print(sys.getsizeof(PERIOD)) #28
print(sys.getsizeof(n)) #28
print(sys.getsizeof(s)) #24
print(sys.getsizeof(i)) #51
print(sys.getsizeof(name)) #51
print(sys.getsizeof(company)) #232
print(sys.getsizeof(j)) #28
print(sys.getsizeof(avg_common)) #24
print(sys.getsizeof(avg_profit)) #24
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