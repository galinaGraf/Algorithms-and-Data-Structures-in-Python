#По длинам трех отрезков, введенных пользователем,
#определить возможность существования треугольника,
#составленного из этих отрезков. Если такой треугольник существует,
#то определить, является ли он разносторонним,
#равнобедренным или равносторонним.

print("Введите длины трех отрезков")
a = int(input('а = '))
b = int(input('b = '))
c = int(input('c = '))

if a + b <= c or a + c <= b:
    print("Треугольник не существует")
elif a == b and b == c:
    print("Треугольник равносторонний")
elif a != b and a!=c and c != b:
    print("Треугольник разносторонний")
elif a == c or b == c or a == b:
    print("Треугольник равнобедренный")





