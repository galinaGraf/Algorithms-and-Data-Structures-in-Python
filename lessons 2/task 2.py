# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import math



odd = 0
even = 0


def odd_or_even(x):
  global odd, even
  digit = x % 10
  if digit % 2 == 0:
    even += 1
  else:
    odd += 1


cProfile.run('odd_or_even(11234567890)')