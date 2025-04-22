from datetime import date


from functools import reduce

from autotest import take_input_output_values, take_all_files

def convert_to_bytes(size, v):
    size = int(size)
    if v == 'GB':
        size, v = size * 1024, 'MB'
    if v == 'MB':
        size, v = size * 1024, 'KB'
    if v == 'KB':
        size, v = size * 1024, 'B'
    return size

def convert_to_bigger_bytes(size):
    size = int(size)
    v = 'B'
    if size / 1024 >= 1:
        size /= 1024
        v = 'KB'
        if size / 1024 >= 1:
            size /= 1024
            v = 'MB'
            if size / 1024 >= 1:
                size /= 1024
                v = 'GB'
    return str(round(size)), v


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