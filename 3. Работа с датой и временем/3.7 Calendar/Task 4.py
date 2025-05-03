from time import strftime

from autotest import take_all_files, take_input_output_values
import calendar
from datetime import datetime


def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(func_monthrange(inp_value))
        print(*out_value)
        print()


def func_monthrange(year_and_month):
    year, month = [int(i) for i in year_and_month]
    return calendar.monthrange(year, month)[1]

inp, out = (take_input_output_values(take_all_files()))
main(inp, out)