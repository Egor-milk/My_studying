from autotest import basedir
import csv

with open(basedir + '\\prices.csv', 'rt', encoding='utf-8') as file:
    reader = [list(i.items()) for i in csv.DictReader(file, delimiter=';')]
    minimal_in_every_store = [[i[0], min(i[1:], key=lambda x:int(x[1]))] for i in reader]
    absolute_minimal = min(minimal_in_every_store, key=lambda x: (int(x[1][1]), x[1][0], x[0][1]))
    print(f'{absolute_minimal[1][0]}: {absolute_minimal[0][1]}')