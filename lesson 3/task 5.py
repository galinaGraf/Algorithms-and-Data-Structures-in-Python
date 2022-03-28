# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

a = 0
b = []
max_num = 0
for i, item in enumerate(array):
    if item < a:
        b.append(item)
        for j in range(len(b)):
            if b[j] > b[max_num]:
                max_num = j
print(f'максимальный отрицательный элемент {b[max_num]}, его позиция {max_num} в массиве {b}')
