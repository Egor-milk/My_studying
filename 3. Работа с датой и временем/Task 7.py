from datetime import date
from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def saturdays_between_two_dates(start, end):
    saturdays = 0
    start, end = sorted([start.toordinal(), end.toordinal()])
    for i in range(start, end + 1):
        if date.fromordinal(i).weekday() == 5:
            saturdays += 1
    return saturdays

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)