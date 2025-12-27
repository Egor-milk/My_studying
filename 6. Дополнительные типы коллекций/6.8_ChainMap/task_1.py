from collections import ChainMap
import json

with open('zoo.json', 'r', encoding='utf-8') as f:
    file = json.load(f)
    a = ChainMap(file)
print(a)