from autotest import basedir
from zipfile import ZipFile
import json
import os

def is_json(file):
    try:
        json_object = json.loads(file)
    except ValueError:
        return False
    return True

with ZipFile(basedir + '\\' + 'data.zip', 'r') as myzip:
    for i in myzip.namelist():
        myzip.extract(i, basedir + '\\' + 'temp')
        if not is_json(basedir + '\\' + 'temp'+ '\\' + i):
            os.remove(basedir + '\\' + 'temp'+ '\\' + i)
