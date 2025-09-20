import csv, os
from autotest import basedir
from collections import namedtuple
from datetime import datetime


with open(os.path.join(basedir, 'meetings.csv'), newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    timeline = sorted(reader, key=lambda row: datetime.strptime(str(f'{row['meeting_date']} {row['meeting_time']}'),
                                                                '%d.%m.%Y %H:%M'))
for row in timeline:
    print(f'{row['surname']} {row['name']}')