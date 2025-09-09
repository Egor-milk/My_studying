#Найдите и исправьте ошибки, допущенные в приведенной ниже программе,
# чтобы она сериализовала словарь dogs и записала результат в файл dogs.pkl.

import pickle, os
from autotest import basedir

dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}

with open(os.path.join(basedir, 'dogs.pkl'), mode='wb') as file:
    pickle.dump(dogs, file)

#Проверка
with open(os.path.join(basedir, 'dogs.pkl'), mode='rb') as file:
    print(pickle.load(file))