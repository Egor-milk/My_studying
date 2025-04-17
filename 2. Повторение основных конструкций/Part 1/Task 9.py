from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def spell(*args):
    dictionary = dict()
    for i in args:
        dictionary[i] = max(dictionary.get(i, 0), len(i))



input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)