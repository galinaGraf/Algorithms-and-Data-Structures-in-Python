# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import cProfile
import timeit

def even_odd(number, even_=0, odd_=0):
    if number == 0:
        return even_, odd_
    if number % 2 == 0:
        even_ += 1
    else:
        odd_ += 1
    number = number // 10
    return even_odd(number, even_, odd_)

#print(even_odd(123))

print(timeit.timeit('even_odd(123)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(1234)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(12345)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(123456)', number=1000, globals=globals()))
print(timeit.timeit('even_odd(1234567)', number=1000, globals=globals()))

#0.0005212000105530024
#0.0006852999795228243
#0.0009483998874202371
#0.0009951000101864338
#0.0010860000038519502

cProfile.run('even_odd(12345678923456789)')

''' 21 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     18/1    0.000    0.000    0.000    0.000 task 1_2.py:6(even_odd)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} '''