from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        print(*previous_and_next_date(inp[0]), sep=' ')
        print(*out)
        print()

def previous_and_next_date(our_date):
    our_date = datetime.strptime(our_date, '%d.%m.%Y')
    return datetime.strftime(our_date - timedelta(days=1), '%d.%m.%Y'), datetime.strftime(our_date + timedelta(days=1), '%d.%m.%Y')
input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


