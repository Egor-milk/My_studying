from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def index_of_nearest(numbers, number):
    try:
        return numbers.index(min(numbers, key=lambda x: abs(x - number)))
    except:
        return -1


input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)