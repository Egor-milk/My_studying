from autotest import basedir
from zipfile import ZipFile
import json

def is_json(file):
    try:
        json_object = json.loads(file)
    except ValueError:
        return False
    return True

with ZipFile(basedir + '\\' + 'data.zip', 'r') as myzip:
    pass