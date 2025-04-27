from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        print(rep_math(inp))
        print(*out)
        print()

def rep_math(lst):
    lst = [datetime.strptime(i, '%H:%M') for i in lst]
    start, end = lst[0], lst[1]
    answer = []
    while start <= end:
        start_plus_45 = start + timedelta(minutes=45)
        if start_plus_45 < end:
            answer.append(f'{start.hour}:{start.minute} - {start_plus_45.hour}:{start_plus_45.minute}')
        start = start_plus_45 + timedelta(minutes=10)
    return answer


input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


