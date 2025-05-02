from time import perf_counter, sleep

def for_and_append(iterable): # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable): # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable): # с использованием встроенной функции list()
    return list(iterable)


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

print(get_the_fastest_func([for_and_append, list_function, list_comprehension], range(100_000)))

print(f'{for_and_append.__name__} : {calc_time_to_run(for_and_append, range(100_000))}')
print(f'{list_function.__name__} : {calc_time_to_run(list_function, range(100_000))}')
print(f'{list_comprehension.__name__} : {calc_time_to_run(list_comprehension, range(100_000))}')