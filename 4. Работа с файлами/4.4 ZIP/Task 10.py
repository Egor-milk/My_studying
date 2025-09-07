from autotest import basedir
from zipfile import ZipFile
import os


with ZipFile(os.path.join(basedir, 'desktop.zip')) as zipfile:
    inf_list = zipfile.infolist()
    for file in inf_list:
        if os.path.isdir(file.filename):
            print(os.path.basename(file.filename))
