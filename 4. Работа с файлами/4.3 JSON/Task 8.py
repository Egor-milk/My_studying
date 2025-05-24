import json
from autotest import basedir

#сделал немного по другому, но так даже прикольнее
with open(basedir + '\\people.json', 'r', encoding='utf-8') as f:
    people = json.load(f)

maximum_keys = max(people, key=lambda x: len(x.keys())).keys()

for index in range(len(people)):
    if len(people[index].keys()) < len(maximum_keys):
        temp_dict = dict.fromkeys(maximum_keys, None)
        for key in temp_dict.keys():
            if key in people[index]:
                temp_dict[key] = people[index][key]
        people[index] = temp_dict

with open(basedir + '\\updated_people.json', 'w', encoding='utf-8') as f:
    json.dump(people, f, indent=4)