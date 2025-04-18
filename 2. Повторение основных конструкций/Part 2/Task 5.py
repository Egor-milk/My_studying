from functools import reduce

from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(max_group(inp[0]))
        print(*out)
        print()

def max_group(our_len):
    our_range = [str(i) for i in range(1, int(our_len) + 1)]
    dictionary = dict()
    for i in our_range:
        summary = int(reduce(lambda x, y: int(x) + int(y), i))
        dictionary[summary] = dictionary.get(summary, 0) + 1
    return max(dictionary.values())

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)