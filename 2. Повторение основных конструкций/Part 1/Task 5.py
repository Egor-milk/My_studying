from autotest import take_all_files, take_input_output_values


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()


def convert(our_string):
    lst = list(filter(lambda x: x.isalpha(), our_string))
    count_lower = sum(map(lambda x: x == x.lower(), lst))
    count_upper = sum(map(lambda x: x == x.upper(), lst))
    if count_upper > count_lower:
        our_string = our_string.upper()
    else:
        our_string = our_string.lower()
    return our_string

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)