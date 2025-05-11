from autotest import basedir
import csv

newest_names = {}
with open(basedir + '\\name_log.csv', 'rt', encoding='utf-8') as file:
     d_reader = csv.DictReader(file)
     for row in d_reader:
         newest_names[row['email']] = newest_names.get(row['email'], 0) + 1