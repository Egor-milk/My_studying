from autotest import basedir
import json


with open(basedir + '\\data1.json', 'r', encoding='utf-8') as f:
    data_1 = json.load(f)
with open(basedir + '\\data2.json', 'r', encoding='utf-8') as f:
    data_2 = json.load(f)

data_1.update(data_2)
with open(basedir + '\\data_merge.json', 'w', encoding='utf-8') as f:
    json.dump(data_1, f, indent=4, ensure_ascii=False)

