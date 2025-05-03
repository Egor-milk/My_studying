from time import strftime

from autotest import take_all_files, take_input_output_values
import calendar
from datetime import datetime, date


def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        exec(inp_value)
        print(*out_value)
        print()


def get_days_in_month(year, month):
    year, month = int(year), list(calendar.month_name).index(month)
    month_length = calendar.monthrange(year, month)[1]
    result = [date(year, month, i) for i in range(1, month_length + 1)]
    return result


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)