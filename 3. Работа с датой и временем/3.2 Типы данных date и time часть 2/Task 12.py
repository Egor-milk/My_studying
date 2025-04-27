from datetime import date
from autotest import take_input_output_values, take_all_files


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(sort_by_date(inp))
        print('\n'.join(out))
        print()


def sort_by_date(lst):
    lst = map(lambda x: date.fromisoformat(x), lst)
    return min(lst).strftime('%d-%m (%Y)')

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)