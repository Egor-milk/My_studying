from autotest import basedir
from zipfile import ZipFile
import os

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f'{round(size)} {power_labels[n]}B'


with ZipFile(os.path.join(basedir, 'desktop.zip')) as zipfile:
    inf_list = zipfile.infolist()
    for file in inf_list:
        if file.filename.endswith('/'): #Проверка папка ли
            fullname = '/' + file.filename[:-1] #Удаление последнего разделителя файла у папки
        else:
            fullname = '/' + file.filename
        basename = fullname[fullname.rfind('/') + 1:]
        file_dir = fullname[:fullname.rfind('/')]
        print(f'{'  ' * file_dir.count('/')}{basename}', end=' ')
        if file.file_size != 0:
            print(f'{format_bytes(file.file_size)}')
        else:
            print()