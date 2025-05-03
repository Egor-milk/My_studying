from autotest import take_all_files, take_input_output_values
import calendar
from datetime import datetime, date


def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        exec(inp_value)
        print(*out_value)
        print()


def get_all_mondays(year):
    return [date(year, i, j) for i in range(1, 13) for j in range(1, calendar.monthrange(year, i)[1] + 1) if date(year, i, j).weekday() == 0]


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)