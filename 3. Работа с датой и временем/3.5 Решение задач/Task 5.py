from time import strftime

from autotest import take_all_files, take_input_output_values
from datetime import datetime, time, timedelta

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(oldest(inp_value))
        print(*out_value)
        print()

def oldest(lst):
    lst = lst[1:]
    lst = [[f'{i.split()[0]} {i.split()[1]}', datetime.strptime(i.split()[2], '%d.%m.%Y')] for i in lst]
    mini = min(lst, key=lambda x: x[1])[1]
    answer = []
    for i in lst:
        if i[1] == mini:
            answer.append(i[0])
    if len(answer) > 1:
        return f'{datetime.strftime(mini, "%d.%m.%Y")} {len(answer)}'
    elif len(answer) == 1:
        return f'{datetime.strftime(mini, "%d.%m.%Y")} {answer[0]}'
    else:
        return None


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)