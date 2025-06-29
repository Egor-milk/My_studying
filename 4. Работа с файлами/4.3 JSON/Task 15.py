from collections import defaultdict

from autotest import basedir
import json

sotred_by_TypeObject = defaultdict(list)
with open(basedir + '\\food_services.json', 'r', encoding='utf-8') as file_to_read:
    data = json.load(file_to_read)
    for line in data:
        sotred_by_TypeObject[line['TypeObject']].append([line['Name'], line['SeatsCount']])
for key, value in sorted(sotred_by_TypeObject.items()):
    maximum_el = max(value, key=lambda x: x[1])
    print(f'{key}: {maximum_el[0]}, {maximum_el[1]}')