from time import strftime

from autotest import take_all_files, take_input_output_values
from datetime import datetime, time, timedelta

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(*max_num_of_births(inp_value))
        print(*out_value)
        print()

def max_num_of_births(lst):
    lst = lst[1:]
    dct = {}
    for i in lst:
        i_spl = i.split()
        dct[datetime.strptime(i_spl[2], '%d.%m.%Y')] = (dct.get(datetime.strptime(i_spl[2], '%d.%m.%Y'), [])
                                                        + [f'{i_spl[0]} {i_spl[1]}'])
    answer = []
    maxi_len = len(max(dct.values(), key=lambda x: len(x)))
    for key, value in dct.items():
        if len(value) == maxi_len:
            answer.append(key)
    return [datetime.strftime(i, '%d.%m.%Y') for i in sorted(answer)]

inp, out = (take_input_output_values(take_all_files()))
main(inp, out)