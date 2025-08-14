#Вам доступен набор различных файлов, названия которых представлены в списке file_names.
# Дополните приведенный ниже код, чтобы он создал архив files.zip и добавил в него все файлы из данного списка.

#Примечание. Считайте, что файлы из списка file_names находятся в папке с программой.

from zipfile import ZipFile
from autotest import basedir


file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf']

with ZipFile(basedir + '\\' + 'file_names.zip', 'w') as file_names_zip:
    for file_name in file_names:
        file_names_zip.write(basedir + '\\' + file_name)
    print(file_names_zip.namelist())