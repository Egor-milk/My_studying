import json
from autotest import basedir


with open(basedir + '\\countries.json', 'r', encoding='utf-8') as f:
    countries = json.load(f)

religion = {}
for i in countries:
    religion[i['religion']] = religion.get(i['religion'], []) + [i['country']]

with open(basedir + '\\religion.json', 'w', encoding='utf-8') as f:
    json.dump(religion, f, indent=4)