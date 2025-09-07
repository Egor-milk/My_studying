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
            # Пропускаем директории и файлы не json
            if zip_info.is_dir() or not zip_info.filename.endswith('.json'):
                continue

            # Берем только имя файла (игнорируем путь)
            filename = os.path.basename(zip_info.filename)

            # Устанавливаем новое имя (только файл)
            zip_info.filename = filename

            # Извлекаем
            zip_file.extract(zip_info, path_to_unzip) #Окзаывется экстракт можно использовать и так, с объектом infolist
            print(f"Извлечен: {filename}")

def delete_invalid_json(path):


    for i in os.listdir(path):
        if not is_json(i):
            os.remove(os.path.join(path, i))


def is_json(file):
    try:
        json_object = json.loads(file)
    except:
        return False
    return True

answer = []
with ZipFile(path_to_zip, 'r') as zip_file:
    for file_name in zip_file.namelist():
        if file_name.endswith('.json'):
            with zip_file.open(file_name) as f:
                if is_json(file_name):
                    answer.append(file_name)

print(answer)

