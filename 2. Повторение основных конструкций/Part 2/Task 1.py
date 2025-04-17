import itertools

from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(do_u_know_the_way(inp))
        print(*out)
        print()

def do_u_know_the_way(lst):
    one, two, three = int(lst[0]), int(lst[1]), int(lst[2])
    optimal_way = min(one + three + two, one + one + two + two, one + three + three + one, two + three + three + two)
    return optimal_way




input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)