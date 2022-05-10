# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import cProfile
import timeit

import math


def even_odd(x, odd=0, even=0):
    while x > 0:
        x = math.floor(x / 10)
        digit = x % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

#print(even_odd(1234))

print(timeit.timeit('even_odd(123)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(1234)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(12345)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(123456)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(1234567)', number=1000, globals=globals()))

#0.0006389999762177467
#0.0001227000029757619
#0.001401199959218502
#0.00012780004180967808
#0.0031356000108644366

cProfile.run('even_odd(1123456789988765430)')

''' 23 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task 1_1.py:9(even_odd)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       19    0.000    0.000    0.000    0.000 {built-in method math.floor}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} '''