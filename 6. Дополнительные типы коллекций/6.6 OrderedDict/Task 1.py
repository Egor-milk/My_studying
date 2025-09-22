from collections import OrderedDict
cloth = OrderedDict({'name': 'pants', 'size': 'm', 'color': 'grey'})
cloth['name'] = 'shirt'
cloth.update(size='s')
for key, value in cloth.items():
        print(f'{key}: {value}')