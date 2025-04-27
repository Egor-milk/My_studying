from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        exec(inp)
        print(*out)
        print()

def fill_up_missing_dates(lst):
    dates_range = [datetime.strptime(i, '%d.%m.%Y') for i in lst]
    current_date = min(dates_range)
    while current_date != max(dates_range):
        current_date += timedelta(days=1)
        if current_date not in dates_range:
            dates_range.append(current_date)
    return sorted([datetime.strftime(i, '%d.%m.%Y') for i in dates_range])


input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


