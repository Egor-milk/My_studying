from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        print(total_sec(inp[0]), sep=' ')
        print(*out)
        print()

def total_sec(our_date):
    our_date = datetime.strptime(our_date, '%H:%M:%S') #- datetime(year=1900, month=1, day=1)
    our_date = timedelta(hours=our_date.hour, minutes=our_date.minute, seconds=our_date.second)
    return our_date.seconds

input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


