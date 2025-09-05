import shutil

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

with ZipFile(basedir + '\\' + 'data.zip', 'r') as myzip: #НИХУЯ НЕ РАБОТАЕТ БЛЯТЬ
    path_to_temp = (basedir + '\\' + 'temp').replace('/', '\\')
    for i in myzip.namelist():
        myzip.extract(i, path_to_temp)
        path_to_file = path_to_temp + '\\' + i
        if os.path.isfile(path_to_file) and is_json(path_to_file):
            os.remove(path_to_file)

#print(is_json('D://programm//pyc
#harm//My_studying//autotest//player2.json'))
