from datetime import date
from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def get_date_range(start, end):
    start, end = start.toordinal(), end.toordinal()
    result = []
    if start <= end:
        for i in range(start, end + 1):
            result.append(date.fromordinal(i))
    return result

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)