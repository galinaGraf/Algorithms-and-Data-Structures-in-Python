#В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
num1 = 2
num2 = 99

rang1 = 2
rang2 = 9
for b in range(rang1, rang2+1):
    a = 0
    for i in range(num1, num2+1):
        if i % b == 0:
            a += 1
    print(f'Числу {b} кратно {a}')


