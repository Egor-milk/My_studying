from autotest import take_all_files, take_input_output_values
import sys
import csv
from datetime import datetime

def main(inp_values):
    for inp_value in inp_values:
        test(inp_value)

def test(stding):
    pass


inp, out = (take_input_output_values(take_all_files()))
main(inp)
#print(game(sys.stdin.read()))