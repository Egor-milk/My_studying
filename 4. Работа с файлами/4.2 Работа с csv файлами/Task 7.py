from autotest import basedir
import csv

with open(basedir + '\\titanic.csv', 'rt', encoding='utf-8') as file:
    mans, womans = [], []
    d_reader = csv.DictReader(file, delimiter=';')
    for row in d_reader:
        if row['survived'] == '1' and float(row['age']) < 18:
            if row['sex'] == 'male':
                mans.append(row['name'])
            else:
                womans.append(row['name'])
    print(*mans, sep='\n')
    print(*womans, sep='\n')