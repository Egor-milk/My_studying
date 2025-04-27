from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        exec (inp)
        print(*out)
        print()

def num_of_sundays(year):
    our_date = datetime(year=year, month=1, day=1)
    count_of_sundays = 0
    while our_date != datetime(year=year + 1, month=1, day=1):
        if our_date.weekday() == 6:
            count_of_sundays += 1
        our_date = our_date + timedelta(days=1)
    return count_of_sundays


input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


