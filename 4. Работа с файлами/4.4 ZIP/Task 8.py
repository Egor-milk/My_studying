from autotest import basedir
from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(basedir + '\\' + zip_name, 'r') as myzip:
        if len(args) > 0:
            for i in args:
                myzip.extract(i, basedir)
        else:
            myzip.extractall(basedir)

extract_this('test.zip', 'test/Картинки/1.jpg')