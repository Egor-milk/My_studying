from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(more_than_one_times(inp[0]))
        print(*out)
        print()

def more_than_one_times(string):
    answer = []
    string = [int(i) for i in string.split()]
    for i in set(string):
        if string.count(i) > 1:
            answer.append(i)
    answer = [str(i) for i in sorted(answer)]
    return ' '.join(answer)


input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)