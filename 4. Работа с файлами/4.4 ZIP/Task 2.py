from zipfile import ZipFile
from autotest import basedir


with ZipFile(basedir + '\\' + 'workbook.zip') as zip:
    files = zip.infolist()
    summary, summary_zipped = 0, 0
    for file in files:
        summary += file.file_size
        summary_zipped += file.compress_size

print(f'Объем исходных файлов: {summary} байт(а) \nОбъем сжатых файлов {summary_zipped} байт(а)')