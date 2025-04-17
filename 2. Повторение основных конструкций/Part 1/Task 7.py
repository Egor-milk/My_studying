from autotest import take_input_output_values, take_all_files

def test(input_values, output_values):
    for inp, out in zip(input_values, output_values):
        exec(inp)
        print(*out)
        print()

def likes(names):
    l_names = len(names)
    if l_names == 0:
        answer = 'Никто не оценил данную запись'
    elif l_names == 1:
        answer = f'{names[0]} оценил(а) данную запись'
    elif l_names == 2:
        answer = f'{names[0]} и {names[1]} оценили данную запись'
    elif l_names == 3:
        answer = f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        answer = f'{names[0]}, {names[1]} и {len(names[2:])} других оценили данную запись'
    return answer


input_values, output_values = take_input_output_values(take_all_files())
#вывод содержимого файлов
test(input_values, output_values)