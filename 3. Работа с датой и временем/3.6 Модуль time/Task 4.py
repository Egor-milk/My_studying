from time import perf_counter, sleep

def get_the_fastest_func(funcs_lst):
    fastest_func = [funcs_lst[0], calc_time_to_run(funcs_lst[0])] #func: time to run
    for i, item in enumerate(funcs_lst[1:]):
        time_to_run = calc_time_to_run(item)
        if time_to_run < fastest_func[1]:
            fastest_func = [item, time_to_run]
    return str(fastest_func[0].__name__), fastest_func[1]

def calc_time_to_run(func):
    start_time = perf_counter()
    func()
    end_time = perf_counter() - start_time
    return end_time

def for_and_append(): # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension(): # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


print(get_the_fastest_func([for_and_append, list_comprehension]))