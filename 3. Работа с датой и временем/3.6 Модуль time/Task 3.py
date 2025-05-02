from math import factorial # функция из модуля math
from time import perf_counter, sleep

def factorial_recurrent(n): # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n): # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def get_the_fastest_func(funcs_lst, arg):
    fastest_func = [funcs_lst[0], calc_time_to_run(funcs_lst[0], arg)] #func: time to run
    for i, item in enumerate(funcs_lst[1:]):
        time_to_run = calc_time_to_run(item, arg)
        if time_to_run < fastest_func[1]:
            fastest_func = [item, time_to_run]
    return str(fastest_func[0].__name__), fastest_func[1]

def calc_time_to_run(func, arg):
    start_time = perf_counter()
    func(arg)
    end_time = perf_counter() - start_time
    return end_time

print(get_the_fastest_func([factorial_recurrent, factorial_classic, factorial], 900))