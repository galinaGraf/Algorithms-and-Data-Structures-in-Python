company = {}
n = int(input("Количество компаний:  "))
s = 0
for i in range(n):
    name = input(str(i+1) + "-ая компания: ")
    pr_1_qv = int(input("прибыль за 1 квартал:  "))
    pr_2_qv = int(input("прибыль за 2 квартал:  "))
    pr_3_qv = int(input("прибыль за 3 квартал:  "))
    pr_4_qv = int(input("прибыль за 4 квартал:  "))
    avg_profit = (pr_1_qv+pr_2_qv+pr_3_qv+pr_4_qv)   #  прибыль компании за год
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