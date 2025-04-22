from functools import reduce
from datetime import date
from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def get_min_max(dates):
    if len(dates) == 0:
        return ()
    return min(dates), max(dates)

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)