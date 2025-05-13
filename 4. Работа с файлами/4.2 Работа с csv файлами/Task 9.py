from autotest import basedir
import csv

with open(basedir + '\\deniro.csv', 'rt', encoding='utf-8') as file:
    column_to_sort = int(input()) - 1 #нумерация начинается с 1
    reader = csv.reader(file, delimiter=',')
    for i in sorted(reader, key=lambda x: int(x[column_to_sort]) if x[column_to_sort].isdigit() else x[column_to_sort]):
        print(','.join(i))