from zipfile import ZipFile
from autotest import basedir

compress_ratio = {}
with ZipFile(basedir + '\\' + 'workbook.zip', 'r') as zipObj:
    list_of_files = zipObj.infolist()
    for file in list_of_files:
        if not file.is_dir():
            compress_ratio[file.filename] = (file.compress_size / file.file_size) * 100
answer = (min(compress_ratio.items(), key= lambda x:x[1]))
print(f'{answer[0][answer[0].rfind('/') + 1:]}: {answer[1]}%' )
