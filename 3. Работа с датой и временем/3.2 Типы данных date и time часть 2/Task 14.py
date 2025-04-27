from datetime import date
from autotest import take_input_output_values, take_all_files


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()


def print_good_dates(dates):
    birthday = 1992
    age = 29
    #dates = map(lambda x : date.fromisoformat(x), dates)
    dates = sorted(filter(lambda x: x.year == birthday and x.month + x.day == age, dates))
    dates = map(lambda x: x.strftime('%B %d, %Y'), dates)
    print(*dates)

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)