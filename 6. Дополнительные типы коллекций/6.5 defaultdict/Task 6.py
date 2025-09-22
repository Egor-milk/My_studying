from autotest import take_input_output_values, take_all_files
from collections import defaultdict


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print()
        print(*out, sep='\n')
        print()

def best_sender(messages, senders):
    results = defaultdict(int)
    for message, sender in zip(messages, senders):
        results[sender] += len(message.split())
    results = [list(reversed(i)) for i in results.items()]
    return max(results)[1]

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)