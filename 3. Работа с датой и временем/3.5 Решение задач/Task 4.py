from autotest import take_all_files, take_input_output_values
from datetime import datetime, time, timedelta

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(*omg(inp_value))
        print(*out_value)
        print()

def omg(lst):
    start, end = [datetime.strptime(i, '%d.%m.%Y') for i in lst]
    while start <= end:
        if (start.day + start.month) % 2 == 1:
            break
        else:
            start += timedelta(days=1)
    answer = []
    while start <= end:
        if start.weekday() not in [0, 3]:
            answer.append(datetime.strftime(start, '%d.%m.%Y'))
        start = start + timedelta(days=3)
    return answer


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)