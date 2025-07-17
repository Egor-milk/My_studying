from zipfile import ZipFile
from autotest import basedir
from datetime import datetime, timedelta


with ZipFile(basedir / 'workbook.zip', 'r') as zip:
    files = zip.infolist()
    for file in files:
        if not file.is_dir():#не доделано
            print(file.date_time)