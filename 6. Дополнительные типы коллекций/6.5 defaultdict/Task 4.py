from autotest import take_input_output_values, take_all_files
from collections import defaultdict


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print()
        print(*out, sep='\n')
        print()

def wins(pairs):
    result = defaultdict(set)
    for winner, loser in pairs:
        result[winner].add(loser)
    return result

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)