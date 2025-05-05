from autotest import take_all_files, take_input_output_values
import sys
from datetime import datetime

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        sys.stdin = inp_value
        print(game(sys.stdin))
        print(*out_value)
        print()

def game(stding):
    lst = [int(i) for i in stding.splitlines()]
    gamers = ['Дима', 'Анри']
    if len(lst) % 2: #Нечетное?
        gamers.reverse()
    return gamers[lst[-1] % 2]


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)
#print(game(sys.stdin.read()))