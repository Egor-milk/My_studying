from autotest import basedir
from collections import namedtuple
import pickle, os

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open(os.path.join(basedir, 'data.pkl'), 'rb') as f:
    data = pickle.load(f)

for i in data:
    dict_i = i._asdict()
    for key, value in dict_i.items():
        print(f'{key}: {value}')
    print()
