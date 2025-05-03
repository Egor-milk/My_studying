from time import strftime

from autotest import take_all_files, take_input_output_values
import calendar
from datetime import datetime


def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(eng_weekday(inp_value[0]))
        print(out_value[0])
        print()


def eng_weekday(our_date):
    our_date = datetime.strptime(our_date, '%Y-%m-%d')
    return calendar.day_name[our_date.weekday()]

inp, out = (take_input_output_values(take_all_files()))
main(inp, out)