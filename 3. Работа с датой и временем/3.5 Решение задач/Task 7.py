from time import strftime

from autotest import take_all_files, take_input_output_values
from datetime import datetime, time, timedelta

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(nearest_birth(inp_value))
        print(*out_value)
        print()

def nearest_birth(lst):
    today_date = datetime.strptime(lst[0], '%d.%m.%Y')
    nearest_date = []
    answer = []
    for i in range(1, 8):
        nearest_date.append(today_date.replace(year = 1970) + timedelta(days=i)) # Присвоено 1970, так как год не важен
    lst = lst[2:]
    for i, item in enumerate(lst):
        temp = [f'{item.split()[0]} {item.split()[1]}', datetime.strptime(item.split()[2], '%d.%m.%Y')]
        if temp[1].replace(year=1970) in nearest_date:
            answer.append(temp)
    if len(answer) != 0:
        return max(answer, key=lambda x: x[1])
    else:
        return 'Дни рождения не планируются'

inp, out = (take_input_output_values(take_all_files()))
main(inp, out)