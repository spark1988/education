import cProfile
import timeit
def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve
#
# cProfile.run('eratosthenes(1000000)')
#
#          9596 function calls in 0.028 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.028    0.028 <string>:1(<module>)
#         1    0.026    0.026    0.027    0.027 main.py:2(eratosthenes)
#         1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
#      9592    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#


def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1
#
# cProfile.run('eratosthenes(1000000)') #где n - любое число
# 9597 function calls in 0.029 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.029    0.029 <string>:1(<module>)
#         1    0.024    0.024    0.029    0.029 main.py:27(eratosthenes)
#         1    0.003    0.003    0.003    0.003 main.py:34(<listcomp>)
#         1    0.000    0.000    0.029    0.029 {built-in method builtins.exec}
#      9592    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# В итоге 2 функции выше работают примерно с одной скоростью первая чуть быстрее, но совсем несущественно, на доли секунд.

n = int(input())
s = [x for x in range(2, n+1) if x not in [i for sub in [list(range(2 * j, n+1, j)) for j in range(2, n // 2)] for i in sub]]
cProfile.run('s')

# 1000 отрабатывает только до тысячи дальше зависает
#          3 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}