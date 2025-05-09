from autotest import basedir
import csv

with open(basedir + '\\salary_data.csv', 'rt', encoding='utf-8') as csvfile:
    #rows = sorted(csv.DictReader(csvfile, delimiter=';'), key=lambda row: (int(row['salary']), row['company_name']))
    #print(*rows, sep='\n')
    rows = list(csv.reader(csvfile, delimiter=';'))
    head, rows = rows[0], rows[1:]
    comp_dict = {}
    for row in rows:
        comp_dict[row[0]] = comp_dict.get(row[0], [0, 0])[0] + int(row[1]), comp_dict.get(row[0], [0, 0])[1] + 1
    comp_dict = [i[0] for i in sorted({key:value[0] / value[1] for key, value in comp_dict.items()}.items(), key=lambda x: (x[1], x[0]))]
    print(*comp_dict, sep='\n')