from autotest import take_all_files, take_input_output_values
import sys
from datetime import datetime

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        sys.stdin = inp_value
        print(max_min_average_height(sys.stdin))
        print(*out_value, sep='\n')
        print()

def max_min_average_height(stding):
    lst = [int(i) for i in stding.splitlines()]
    if len(lst) > 0:
        return f'''Рост самого низкого ученика: {min(lst)}
Рост самого высокого ученика: {max(lst)}
Средний рост: {sum(lst) / len(lst)}'''
    else:
        return 'нет учеников'



inp, out = (take_input_output_values(take_all_files()))
main(inp, out)
#print(game(sys.stdin.read()))