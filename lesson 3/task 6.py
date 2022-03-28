#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_num = 0
max_num = 0
for i in range(len(array)):
    if array[i] < array[min_num]:
        min_num = i
    elif array[i] > array[max_num]:
        max_num = i

if min_num > max_num:
    min_num, max_num = max_num, min_num

sum_ = 0
for i in range(min_num+1, max_num):
    sum_+= array[i]
print(f'минимальное значение: {array[min_num]} ,максимальное значение: {array[max_num]} , сумма между ними: {sum_}')