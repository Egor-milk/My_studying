import itertools

from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(ru_or_eng(inp))
        print(*out)
        print()

def ru_or_eng(lst):
    lst = map(lambda x: True if x in 'AaBCcEeHKMOoPpTXxy' else False, lst) # английские буквы
    return ['ru', 'mix', 'mix', 'en'][sum(lst)]




input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)