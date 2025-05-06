from autotest import take_all_files, take_input_output_values
import sys
from datetime import datetime

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        sys.stdin = inp_value
        print(filtr(sys.stdin), sep='\n')
        print(*out_value, sep='\n')
        print('\n')

def filtr(stding):
    original_order = [datetime.strptime(i, '%d.%m.%Y') for i in stding.split()]
    if len(original_order) == len(set(original_order)): #Проверка на повторения
        if original_order == sorted(original_order):
            return 'ASC'
        elif original_order == sorted(original_order, reverse=True):
            return 'DESC'
    return 'MIX'


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)
#print(game(sys.stdin.read()))