from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def choose_plural(amount, declension):
    amount = str(amount)
    if int(amount[-2:]) in range(11, 15) or int(amount[-1:]) in list(range(5, 11)) + [0]:
        form = declension[2]
    elif int(amount[-1:]) == 1:
        form = declension[0]
    else:
        form = declension[1]
    return f'{amount} {form}'


input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)