from autotest import take_all_files, take_input_output_values
import sys
from datetime import datetime

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        sys.stdin = inp_value
        print(comment(sys.stdin))
        print(*out_value, sep='\n')
        print()

def comment(stding):
    return sum(map(lambda x: True if x.startswith('#') else False, [i.strip() for i in stding.splitlines()]))



inp, out = (take_input_output_values(take_all_files()))
main(inp, out)
#print(game(sys.stdin.read()))