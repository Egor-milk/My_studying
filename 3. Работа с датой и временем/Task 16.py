from datetime import date
from autotest import take_input_output_values, take_all_files


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        counter = 0
        for i in inp:
            if 'end' in i:
                break
            else:
                if is_correct(i):
                    counter += 1
                    print('Корректная', end= ' ')
                else:
                    print('Некорректная', end=' ')
        print(counter)
        print(*out)
        print()


def is_correct(dat):
    day, month, year = dat.split('.')
    try:
        date.fromisoformat('-'.join([str(year), str(month), str(day)]))
    except:
        return False
    return True

input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)