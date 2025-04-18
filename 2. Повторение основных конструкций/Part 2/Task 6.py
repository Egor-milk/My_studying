from functools import reduce

from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(same_word(inp))
        print(*out)
        print()

def same_word(data):
    def isvowel(value):
        to_return = []
        vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
        for index, item in enumerate(value):
            if item in vowels:
                to_return.append(index)
        return to_return

    answer = []
    main_word = isvowel(data[0])
    for i in data[2:]:
        if isvowel(i) == main_word:
            answer.append(i)
    return ' '.join(answer)

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)