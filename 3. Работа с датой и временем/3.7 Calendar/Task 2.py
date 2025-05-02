from autotest import take_all_files, take_input_output_values
import calendar


def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(month_calendar(inp_value))
        print(out_value)
        print()


def month_calendar(lst):
    cal = calendar.month(int(lst[0]), list(calendar.month_abbr).index(lst[1]))
    return cal

inp, out = (take_input_output_values(take_all_files()))
main(inp, out)