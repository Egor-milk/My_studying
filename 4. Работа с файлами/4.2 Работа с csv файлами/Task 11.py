import csv
from collections import OrderedDict
from autotest import basedir


with open(basedir + '\\student_counts.csv', 'rt', encoding='utf-8') as csvfile:
    reader = [list(i.items()) for i in list(csv.DictReader(csvfile))]
    reader = [OrderedDict([i[0]] + sorted(i[1:], key=lambda x: (int(x[0][0:x[0].find('-')]), x[0][x[0].find('-') + 1:]))) for i in reader]

with open(basedir + '\\sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader[0].keys())
    writer.writeheader()
    writer.writerows(reader)
