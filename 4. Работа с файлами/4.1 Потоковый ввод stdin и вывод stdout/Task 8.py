from autotest import take_all_files, take_input_output_values
import sys
from datetime import datetime

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        sys.stdin = inp_value
        print(type_of_progression(sys.stdin), sep='\n')
        print(*out_value, sep='\n')
        print('\n')

def type_of_progression(stding):
    sequence = [int(i) for i in stding.split()]
    different = sequence[1] - sequence[0]
    answer = 'Не прогрессия'

    for index in range(1, len(sequence[1:]) + 1):
        if sequence[index] - sequence[index - 1] != different:
            break
    else:
        answer = 'Арифметическая прогрессия'

    divider = sequence[1] / sequence[0]
    for index in range(1, len(sequence[1:]) + 1):
        if sequence[index] / sequence[index - 1] != divider:
            break
    else:
        answer = 'Геометрическая прогрессия'
    return answer


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)
#print(game(sys.stdin.read()))