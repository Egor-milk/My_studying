from autotest import take_all_files, take_input_output_values
import sys
from datetime import datetime

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        sys.stdin = inp_value
        print(*comment(sys.stdin), sep='\n')
        print()
        print(*out_value, sep='\n')
        print('\n')

def comment(stding):
    return list(filter(lambda x: not x.strip().startswith('#'), stding.splitlines()))



inp, out = (take_input_output_values(take_all_files()))
main(inp, out)
#print(game(sys.stdin.read()))