# 3. По введенным п ользователем координатам
# двух точек вывести уравнение
# прямой вида y = kx + b,
# проходящей через эти точки.

print('Ведите координаты 2-х точек:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

a = x1 - x2
b = y1 - y2
if a == 0 and b == 0:
    print('точки совадают')
else:
    k = b / a
    b = y2 - k * x2

print(f'y = {k}x + {b}')
