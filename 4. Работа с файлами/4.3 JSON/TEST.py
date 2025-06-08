import json, csv
from autotest import basedir
from collections import defaultdict #defaultdict имба оказывается, буду использовать

addresses = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
print(addresses['hello']['poop']['sex'])
