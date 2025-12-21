from collections import OrderedDict
from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print()
        print(*out, sep='\n')
        print()


def custom_sort(ordered_dict, by_values=False):
    globals()[ordered_dict] = sorted(ordered_dict.items(), key= lambda x: x[0])

#input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
#test(input_values, output_values)

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)