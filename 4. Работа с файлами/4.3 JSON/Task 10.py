import json, csv
from autotest import basedir

addresses = {}
with open(basedir + '\\playgrounds.csv', 'r', encoding='utf-8') as file_to_read:
    d_reader = list(csv.DictReader(file_to_read, delimiter=';'))
    with open(basedir + '\\addresses.json', 'w', encoding='utf-8') as file_to_write:
        for i in d_reader:
            addresses[i['AdmArea']] = addresses.get(i['AdmArea'], {})
            #addresses[i['AdmArea']][] НЕ ДОДЕЛАНО
print(addresses)
