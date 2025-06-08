from autotest import basedir
import json
from datetime import datetime, time


with open(basedir + '\\pools.json', 'r', encoding='utf-8') as file_to_read:
    pools_lst = json.load(file_to_read)

right_pool = {}
for pool in pools_lst:
    w_start, w_end = [datetime.strptime(i, '%H:%M').time() for i in pool["WorkingHoursSummer"]["Понедельник"].split('-')]
    if w_start <= time(10) and w_end >= time(12):
        len_pool, width_pool = pool["DimensionsSummer"]["Length"], pool["DimensionsSummer"]["Width"]
        if [len_pool, width_pool] > [right_pool.get('Length', 0), right_pool.get('Width', 0)]:
            right_pool = {'Address': pool['Address'], 'Length': len_pool, 'Width': width_pool}
print(f'{right_pool['Length']}x{right_pool['Width']} \n{right_pool['Address']}')