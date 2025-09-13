from autotest import basedir
import pickle, os


def filter_dump(filename, objects, typename):
    '''Функция должна создавать pickle файл с названием filename, который содержит
    сериализованный список только тех объектов из списка objects, тип которых равен typename'''
    right_objects = []
    for i in objects:
        if type(i) == typename:
            right_objects.append(i)
    with open(os.path.join(basedir, filename), 'wb') as f:
        pickle.dump(right_objects, f)

#filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)


#Проверка
with open(os.path.join(basedir, 'numbers.pkl'), 'rb') as f:
    numbers = pickle.load(f)
    print(numbers)