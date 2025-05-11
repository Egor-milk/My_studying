from autotest import basedir
import csv

newest_names = {}
with open(basedir + '\\name_log.csv', 'rt', encoding='utf-8') as file:
     d_reader = csv.DictReader(file)
     for row in d_reader:
         mail = row['email']
         newest_names[mail] = [row['username'], row['dtime']]

with open(basedir + '\\new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    d_writer = csv.writer(file)
    d_writer.writerow(['username','email', 'dtime'])
    for key, value in sorted(newest_names.items(), key = lambda x: x[1]):# разобраться как сортировать
        d_writer.writerow([key, value[0], value[1]])
        d_writer.writerow([value[0], key, value[1]])