print("Введите три разных числа")
a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))

if b < a < c or b > a > c:
    print(f'{a} является средним числом')
elif a < b < c or a > b > c:
    print(f'{b} является средним числом')
else:
    print(f'{c} является средним числом')
