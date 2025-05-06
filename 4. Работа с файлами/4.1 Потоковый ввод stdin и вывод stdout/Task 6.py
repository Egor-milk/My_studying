from autotest import take_all_files, take_input_output_values
import sys
from datetime import datetime

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        sys.stdin = inp_value
        print(filtr(sys.stdin), sep='\n')
        print()
        print(*out_value, sep='\n')
        print('\n')

def filtr(stding):
    stding = [line.split(' / ') for line in stding.split('\n')]
    all_news, required_category = sorted(stding[:-1], key=lambda x: (x[2], x[0])), *stding[-1]
    filtered_news = map(lambda x: x[0], filter(lambda x: x[1] == required_category, all_news))
    return '\n'.join(filtered_news)



inp, out = (take_input_output_values(take_all_files()))
main(inp, out)
#print(game(sys.stdin.read()))