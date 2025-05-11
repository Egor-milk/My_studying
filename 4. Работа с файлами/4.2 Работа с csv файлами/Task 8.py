from autotest import basedir
import csv
from datetime import datetime, date

newest_names = {}
with open(basedir + '\\name_log.csv', 'rt', encoding='utf-8') as file:
    d_reader = csv.DictReader(file)
    for row in d_reader:
        mail = row['email']
        date1 = datetime.strptime(row['dtime'], '%d/%m/%Y %H:%M')
        if mail in newest_names:
            date2 = datetime.strptime(newest_names[mail], '%d/%m/%Y %H:%M')
        else:
            date2 = datetime(1, 1, 1)
        if date1 > date2:
            newest_names[mail] = [row['username'], row['dtime']]

with open(basedir + '\\new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    d_writer = csv.writer(file)
    d_writer.writerow(['username','email', 'dtime'])
    for key, value in sorted(newest_names.items(), key = lambda x: x[0]):# разобраться как сортировать
        d_writer.writerow([value[0], key, value[1]])