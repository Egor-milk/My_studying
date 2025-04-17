from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()


def filter_anagrams(word, anagrams):
    answer = []
    for i in anagrams:
        if sorted(list(i)) == sorted(list(word)):
            answer.append(i)
    return answer

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)