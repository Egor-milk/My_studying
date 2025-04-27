from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        print(time_after_the_timer(inp))
        print(*out)
        print()

def time_after_the_timer(lst):
    time = datetime.strptime(lst[0], '%H:%M:%S') + timedelta(seconds=int(lst[1]))
    return time.strftime('%H:%M:%S')



input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


