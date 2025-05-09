import os
import csv
# функции для автотестов как на степике

basedir = os.path.abspath(os.getcwd())
basedir = basedir[:basedir.find('My_studying') + 11] + '\\autotest'


def take_all_files(directory=basedir):
    files = os.listdir(directory)
    return files


def take_input_output_values(all_files, directory=basedir, csv_in=False, csv_delimiter=';', csv_quotechar='"'):
    if csv_in:
        output_values = []
        for i in all_files:
            if i.isdigit():
                with open(directory + '\\' + i, 'r', encoding='utf-8') as file:
                    d_reader = csv.DictReader(file, delimiter=csv_delimiter, quotechar=csv_quotechar)
            elif i.endswith('.clue'):
                with open(directory + '\\' + i, 'rt', encoding='utf-8') as file:
                    output_values.append(list(map(lambda x: x, file.read().split('\n'))))
            return d_reader, output_values
    else:
        input_values = []
        output_values = []
        for i in all_files:
            if i.isdigit():
                with open(directory + '\\' + i, 'rt', encoding='utf-8') as file:
                    input_values.append(file.read())
            elif i.endswith('.clue'):
                with open(directory + '\\' + i, 'rt', encoding='utf-8') as file:
                    output_values.append(list(map(lambda x: x, file.read().split('\n'))))
        return input_values, output_values

