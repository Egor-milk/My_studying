from functools import reduce

from autotest import take_input_output_values, take_all_files

def convert_to_bytes(size, v):
    size = int(size)
    if v == 'GB':
        size, v = size * 1024, 'MB'
    if v == 'MB':
        size, v = size * 1024, 'KB'
    if v == 'KB':
        size, v = size * 1024, 'B'
    return size

def convert_to_bigger_bytes(size):
    size = int(size)
    v = 'B'
    if size / 1024 >= 1:
        size /= 1024
        v = 'KB'
        if size / 1024 >= 1:
            size /= 1024
            v = 'MB'
            if size / 1024 >= 1:
                size /= 1024
                v = 'GB'
    return str(round(size)), v


def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(sort_by_extension(inp))
        #print('\n'.join(out))
        print()

def sort_by_extension(data):
    extension = {}
    data = list(map(lambda x: x.split(), data))
    for i in data:
        ext = i[0][i[0].find('.'):]
        if ext not in extension:
            extension[ext] = [[i[0], convert_to_bytes(i[1], i[2])]]
        else:
            extension[ext].append([i[0], convert_to_bytes(i[1], i[2])])
    result = []
    for key, value in sorted(extension.items()):
        summary = 0
        temp = []
        for i in value:
            temp.append(i[0])
            summary += int(i[1])
        result += [f'{"\n".join(sorted(temp))}\n----------\nSummary: {" ".join(convert_to_bigger_bytes(summary))}']
    return '\n\n'.join(result)


input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)