from zipfile import ZipFile
from autotest import basedir

with ZipFile(basedir + '\\' + 'test2.zip', 'w') as zipObj:
    zipObj.write(basedir + '\\' + 'best_scores.json')

with ZipFile(basedir + '\\' + 'test2.zip', 'a') as zipObj:
    zipObj.write(basedir + '\\' + 'exam_results.csv')