from autotest import basedir
from zipfile import ZipFile


zip_info = []
with ZipFile(basedir + '\\' + 'workbook.zip', 'r') as zipFile:
    infolist = zipFile.infolist()
    for info in infolist:
        if not info.is_dir():
            zip_info.append([info.filename[info.filename.rfind('/') + 1:], info.date_time, info.file_size, info.compress_size])

for i in sorted(zip_info, key=lambda x:x[0]):
    print(f'''  {i[0]}
        Дата модификации файла: {i[1]}
        Объем исходного файла: {i[2]} байт(а)
        Объем сжатого файла: {i[3]} байт(а)
    ''')