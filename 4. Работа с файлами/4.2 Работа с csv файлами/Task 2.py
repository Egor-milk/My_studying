import csv
from autotest import basedir

with open(basedir + '\\sales.csv', 'r', encoding='utf-8') as file:
    d_reader = csv.DictReader(file, delimiter=';')
    real_sales = [i['name'] for i in d_reader if int(i['old_price']) > int(i['new_price'])]
    print(*real_sales, sep='\n')
