from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def spell(*args):
    args = [i.lower() for i in args]
    dictionary = dict()
    for key in args:
        dictionary[key[0]] = max(dictionary.get(key[0], 0), len(key))
    return dictionary



input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)