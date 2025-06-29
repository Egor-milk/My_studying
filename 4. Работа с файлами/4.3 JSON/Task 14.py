from autotest import basedir
import json

objects_in_districts = {}
objects_in_net = {}
with open(basedir + '\\food_services.json', 'r', encoding='utf-8') as file_to_read:
    data = json.load(file_to_read)
    for line in data:
        objects_in_districts[line['District']] = objects_in_districts.get(line['District'], 0) + 1
        if line['IsNetObject'] == 'да':
            objects_in_net[line['OperatingCompany']] = objects_in_net.get(line['OperatingCompany'], 0) + 1
max_obj_in_dist = max(objects_in_districts.items(),key=lambda x: x[1])
max_obj_in_net = max(objects_in_net.items(),key=lambda x: x[1])
print(f'''{max_obj_in_dist[0]}: {max_obj_in_dist[1]}\n{max_obj_in_net[0]}: {max_obj_in_net[1]}''')
