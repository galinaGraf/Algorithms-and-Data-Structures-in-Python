#1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

li = []
for i in (range(0, 10)):
    li.append(random.randint(-100, 100))
#print(li)
#n = 1
def sort(li):
    n = 1
    while n < len(li):
        for i in range(len(li) - n):
            if li[i] < li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        n += 1
    return li
print(li)
print(sort(li))
