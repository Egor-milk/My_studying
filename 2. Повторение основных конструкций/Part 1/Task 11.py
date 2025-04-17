import itertools

from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def get_biggest(numbers):
    numbers = map(lambda x: str(x), numbers)
    numb = max(map(lambda x: int(''.join(x)), itertools.permutations(numbers)))
    return numb




input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)