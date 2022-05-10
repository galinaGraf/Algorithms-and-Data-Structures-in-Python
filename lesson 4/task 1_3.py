# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import cProfile
import timeit

def even_odd(a, even = 0, odd = 0):
    while a > 0:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
        a = a // 10
    return f'четные: {even}', f'нечетные: {odd}'

#print(even_odd(123))

print(timeit.timeit('even_odd(123)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(1234)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(12345)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(123456)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(1234567)', number=1000, globals=globals()))

#0.0006032999372109771
#0.0006506999488919973
#0.0007322999881580472
#0.0008141999132931232
#0.0008929000468924642

cProfile.run('even_odd(23456789876545634567878)')

''' 4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task 1_3.py:6(even_odd)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} '''

