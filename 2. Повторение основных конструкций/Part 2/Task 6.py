from functools import reduce

from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(multilanguage_film(inp))
        print(*out)
        print()

def multilanguage_film(data):
    data = [i.split(', ') for i in data[1:]]
    language = set(data[0])
    for i in data[1:]:
        language.intersection_update(set(i))
    if len(language) > 0:
        return ', '.join(sorted(language))
    else:
        return 'Сериал снять не удастся'

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)