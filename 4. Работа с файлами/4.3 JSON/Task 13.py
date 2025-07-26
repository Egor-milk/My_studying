from autotest import basedir
import json, csv
from collections import defaultdict
from datetime import datetime

all_scores = defaultdict(list) #при обращении к all_scores[key1] создает key1:[]
with open(basedir + '\\exam_results.csv', 'r', encoding='utf-8') as file_to_read:
    d_reader = csv.DictReader(file_to_read, delimiter=',')
    for line in d_reader:
        full_name = line['name'] + ' ' + line['surname']
        all_scores[full_name].append(line)
best_value = []
for value in all_scores.values():
    best_value.append(max(sorted(value, key= lambda y: datetime.strptime(y['date_and_time'], '%Y-%m-%d %H:%M:%S'),
                                 reverse= True), key=lambda x: x['score']))
best_value.sort(key=lambda x: x['email'])
with open(basedir + '\\best_scores.json', 'w', encoding='utf-8') as file_to_write:
    json.dump(best_value, file_to_write, ensure_ascii=False, indent=4)