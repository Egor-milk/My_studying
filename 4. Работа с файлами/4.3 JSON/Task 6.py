from autotest import basedir
import json
from datetime import datetime
import sys

def update_json(file_name):
    new_list = []
    with open(basedir + '\\' + file_name, 'r', encoding='utf-8') as f:
        j_load = json.load(f)
    for i in range(len(j_load)):
        if type(j_load[i]) == str:
            new_list.append(j_load[i] + '!')
        elif type(j_load[i]) == int:
            new_list.append(j_load[i] + 1)
        elif type(j_load[i]) == bool:
            new_list.append(not j_load[i])
        elif type(j_load[i]) == list:
            new_list.append(j_load[i] * 2)
        elif type(j_load[i]) == dict:
            j_load[i]["newkey"] = None
            new_list.append(j_load[i])
    with open(basedir + '\\updated_data.json', 'w', encoding='utf-8') as f:
        json.dump(new_list, f, ensure_ascii=False, indent=4)

update_json('data.json')