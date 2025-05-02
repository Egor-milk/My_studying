from time import perf_counter, sleep

def get_the_fastest_func(funcs_lst, arg):
    fastest_func = [funcs_lst[0], calc_time_to_run(funcs_lst[0], arg)] #func: time to run
    for i, item in enumerate(funcs_lst[1:]):
        time_to_run = calc_time_to_run(item, arg)
        if time_to_run < fastest_func[1]:
            fastest_func = [item, time_to_run]
    return str(fastest_func[0].__name__)

def calc_time_to_run(func, arg):
    start_time = perf_counter()
    func(arg)
    end_time = perf_counter() - start_time
    return end_time

def func5(arg):
    sleep(5)
    return arg

def func3(arg):
    sleep(3)
    return arg

def func2(arg):
    sleep(2)
    return arg

def func4(arg):
    sleep(4)
    return arg

print(get_the_fastest_func([func2, func3, func4, func5], 5))
