import shutil

from autotest import basedir
from zipfile import ZipFile
import json

path_to_zip = basedir + '\\' + 'data.zip'

def is_json(file):
    try:
        json_object = json.loads(file.read().decode('utf-8'))
    except:
        return False, []
    return True, json_object

arsenal_football_player = set()
valid_json = []
with ZipFile(path_to_zip, 'r') as zip_file:
    for file_name in zip_file.namelist():
        if file_name.endswith('.json'):
            with zip_file.open(file_name) as f:
                is_js, json_object = is_json(f)
                if is_js:
                    if json_object['team'] == 'Arsenal':
                        arsenal_football_player.add(f'{json_object['first_name']} {json_object['last_name']}')
print(*sorted(arsenal_football_player), sep='\n')


