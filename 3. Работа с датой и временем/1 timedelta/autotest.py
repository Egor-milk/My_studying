import os
# функции для автотестов как на степике

def take_all_files(directory='D:/programm/PythonProjects/autotest'):
    files = os.listdir(directory)
    return files


def take_input_output_values(all_files, directory='D:/programm/PythonProjects/autotest'):
    input_values = []
    output_values = []
    for i in all_files:
        if i.isdigit():
            with open(directory + '\\' + i, 'rt', encoding='utf-8') as file:
                input_values.append(list(map(lambda x: x.strip(), file.read().split(' '))))
        elif i.endswith('.clue'):
            with open(directory + '\\' + i, 'rt', encoding='utf-8') as file:
                output_values.append(list(map(lambda x: x.strip(), file.read().split('\n'))))

    return input_values, output_values

