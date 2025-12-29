from collections import ChainMap
import json


summary = 0
with open('zoo.json', 'r', encoding='utf-8') as f:
    file = json.load(f)
    a = ChainMap(*file)
print(a)
for k in a:
    summary += a[k]
print(summary)