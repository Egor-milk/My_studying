from autotest import take_all_files, take_input_output_values
import sys


def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        sys.stdin = inp_value
        print([line[::-1] for line in sys.stdin.splitlines()])
        print(out_value)
        print()



inp, out = (take_input_output_values(take_all_files()))
main(inp, out)