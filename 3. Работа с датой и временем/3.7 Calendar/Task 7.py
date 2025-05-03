from autotest import take_all_files, take_input_output_values
import calendar
from datetime import datetime, date


def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(*TTM(inp_value[0]))
        print(*out_value)
        print()


def TTM(year):
    year = int(year)
    result = []
    for i in range(1, 13):
        day = 1
        while date(year, i, day).weekday() != 3:
            day += 1
        else:
            day += 14
        result.append(date(year, i, day).strftime('%d.%m.%Y'))
    return result


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)