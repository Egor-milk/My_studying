from autotest import basedir
from collections import namedtuple

#Дополните приведенный ниже код, чтобы он создал именованный кортеж Fruit с полями name, color и vitamins.

#Примечание. Программа ничего не должна выводить.

Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])

print(Fruit('banana', color='yellow', vitamins=2))
