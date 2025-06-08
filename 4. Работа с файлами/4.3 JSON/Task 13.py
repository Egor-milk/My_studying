from autotest import basedir
import json, csv
from collections import defaultdict

best_scores = {}
with open(basedir + '\\exam_results.csv', 'r', encoding='utf-8') as file_to_read:
    d_reader = csv.DictReader(file_to_read, delimiter=',')
    for line in d_reader:
        full_name = line['name'] + ' ' + line['surname']
        best_scores[full_name] = best_scores.get(full_name, {}) #ЕЩЕ НЕ РАБОТАЕТ
