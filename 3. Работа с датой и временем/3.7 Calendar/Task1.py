from autotest import take_all_files, take_input_output_values
import calendar


def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(*isleaps(inp_value))
        print(*out_value)
        print()


def isleaps(lst):
    lst = lst[1:]
    return [calendar.isleap(int(i)) for i in lst]


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)