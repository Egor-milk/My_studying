from autotest import basedir
from zipfile import ZipFile
import json
import os

def is_json(file):
    try:
        with open(file) as json_data:
            json_object = json.load(json_data)
    except:
        return False
    return True

with ZipFile(basedir + '\\' + 'data.zip', 'r') as myzip:
    for i in myzip.namelist():
        path = (basedir + '\\' + i).replace('/', '\\')
        print(is_json(path))

