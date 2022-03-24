# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import math

x = int(input('Input number: '))

odd = 0
even = 0


def odd_or_even(x):
  global odd, even
  digit = x % 10
  if digit % 2 == 0:
    even += 1
  else:
    odd += 1


odd_or_even(x)

while x >= 10:
  x = math.floor(x / 10)
  odd_or_even(x)

print('Odd:', odd)
print('Even:', even)