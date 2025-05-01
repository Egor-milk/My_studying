import time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


def calculate_it(func, *args):
    time_start = time.perf_counter()
    result = func(*args)
    time_spend = time.perf_counter() - time_start
    return result, time_spend

print(calculate_it(add, 1, 2, 3))