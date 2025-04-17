import itertools

from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        print(flip_rotate(inp[0]))
        print(*out)
        print()

def flip_rotate(lst):
    n, x, y, a, b = [int(i) for i in lst.split()]
    our_range = [str(i) for i in range(0, n + 1)]
    our_range = our_range[0:x] + our_range[x:y + 1][::-1] + our_range[y+1:]
    our_range = our_range[1:a] + our_range[a:b + 1][::-1] + our_range[b+1:]
    return ' '.join(our_range)




input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)