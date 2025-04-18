from functools import reduce

from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(new_mail(inp))
        print(*out)
        print()

def new_mail(data):
    existing = data[1:int(data[0]) + 1]
    new = data[int(data[0]) + 2:]
    answer = []
    for i in new:
        if i + '@beegeek.bzz' not in existing:
            answer.append(i + '@beegeek.bzz')
            existing.append(i + '@beegeek.bzz')
        else:
            counter = 1
            insert = False
            while not insert:
                if (i + str(counter) + '@beegeek.bzz') not in existing:
                    answer.append(i + str(counter) + '@beegeek.bzz')
                    existing.append(i + str(counter) + '@beegeek.bzz')
                    insert = True
                else:
                    counter += 1
    return ' '.join(answer)


input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)