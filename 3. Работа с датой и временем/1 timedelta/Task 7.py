from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        print(neighboring_dates(inp))
        print(*out)
        print()

def neighboring_dates(lst):
    lst = [datetime.strptime(i,'%d.%m.%Y') for i in lst]
    start = lst[0]
    answer = []
    for i in lst[1:]:
        answer.append(abs(start - i).days)
        start = i
    return answer



input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


