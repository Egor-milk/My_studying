from autotest import basedir
import csv

with open(basedir + '\\data.csv', 'rt', encoding='utf-8') as file:
    domain_usage = {}
    data = csv.DictReader(file)
    for row in data:
        email = row['email'][row['email'].find('@') + 1:]
        domain_usage[email] = domain_usage.get(email, 0) + 1

with open(basedir + '\\domain_usage.csv ', 'w', encoding='utf-8', newline='') as file:
    d_writer = csv.writer(file)
    d_writer.writerow(['domain', 'count'])
    for key, value in sorted(domain_usage.items(), key=lambda item: (item[1], item[0])):
        d_writer.writerow([key, value])