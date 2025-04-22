from datetime import date
from autotest import take_input_output_values, take_all_files


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(sort_date(inp))
        print(out)
        print()


def sort_date(lst):
    lst = lst[1:]
    lst = sorted(map(lambda x: date.fromisoformat(x), lst))
    lst = map(lambda x: x.strftime('%d/%m/%Y'), lst)
    return list(lst)

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)