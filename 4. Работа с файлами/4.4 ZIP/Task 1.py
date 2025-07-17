from zipfile import ZipFile
from autotest import basedir

with ZipFile(basedir + '\\' + 'workbook.zip', 'r') as zipObj:
    list_of_files = zipObj.infolist()
    answer = 0
    for file in list_of_files:
        if not file.is_dir():
            answer += 1
    print(answer)
