from zipfile import ZipFile
from autotest import basedir
from datetime import datetime, timedelta

filtered_files = []
with ZipFile(basedir + '\\' +  'workbook.zip', 'r') as zip:
    files = zip.infolist()
    for file in files:
        if not file.is_dir():#не доделано
            if datetime.strptime('.'.join(map( lambda x:str(x), file.date_time)), '%Y.%m.%d.%H.%M.%S') > \
                    datetime(2021, 11, 30, 14, 22):
                filtered_files.append(file.filename[file.filename.rfind('/') + 1:])
filtered_files.sort()
print(*filtered_files, sep='\n')
