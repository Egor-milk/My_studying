import json, csv
from autotest import basedir
from collections import defaultdict #defaultdict имба оказывается, буду использовать

addresses = defaultdict(lambda: defaultdict(list))
with open(basedir + '\\playgrounds.csv', 'r', encoding='utf-8') as file_to_read:
    d_reader = list(csv.DictReader(file_to_read, delimiter=';'))
    for item in d_reader:
        addresses[item['AdmArea']][item['District']].append(item['Address'])
    with open(basedir + '\\addresses.json', 'w', encoding='utf-8') as file_to_write:
        json.dump(addresses, file_to_write, ensure_ascii=False, indent=4)

print(addresses)
