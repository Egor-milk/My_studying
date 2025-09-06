import shutil

from autotest import basedir
from zipfile import ZipFile
import json, os, sys

path_to_zip = basedir + '\\' + 'data.zip'
path_to_unzip = basedir + '\\' + 'temp'

def extract_flattened():
    """
    Извлекает все файлы из архива в одну директорию
    """
    # Создаем целевую директорию
    os.makedirs(path_to_unzip, exist_ok=True)

    with ZipFile(path_to_zip, 'r') as zip_file:
        for zip_info in zip_file.infolist():
            # Пропускаем директории
            if zip_info.is_dir() or not zip_info.filename.endswith('.json'):
                continue

            # Берем только имя файла (игнорируем путь)
            filename = os.path.basename(zip_info.filename)

            # Устанавливаем новое имя (только файл)
            zip_info.filename = filename

            # Извлекаем
            zip_file.extract(zip_info, path_to_unzip)
            print(f"Извлечен: {filename}")



def is_json(file):
    try:
        with open(file) as json_data:
            json_object = json.load(json_data)
    except:
        return False
    return True

for i in os.listdir(path_to_unzip):
    if not is_json(i):
        os.remove(os.path.join(path_to_unzip, i))

extract_flattened()

#print(is_json('D://programm//pyc
#harm//My_studying//autotest//player2.json'))
