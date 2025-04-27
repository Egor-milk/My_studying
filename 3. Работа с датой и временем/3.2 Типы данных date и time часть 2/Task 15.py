from datetime import date
from autotest import take_input_output_values, take_all_files


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()


def is_correct(day, month, year):
    try:
        date.fromisoformat('-'.join([str(year), str(month), str(day)]))
    except:
        return False
    return True

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)