from autotest import basedir
import pickle, os

def create_pickle_list():
    with open(os.path.join(basedir, 'pickle.pickle'), 'wb') as f:
        pickle.dump([1, 2, 3, 6, 7, 8, 9, 13, 2134, 434, 1, 1, 1, 2432, 23], f)

def create_pickle_dict():
    with open(os.path.join(basedir, 'pickle.pickle'), 'wb') as f:
        pickle.dump({1: '1', 2: '2', 3:'3', 4321: '4321', 111: '111'}, f)


def checksum(filename, int1):
    with open(filename, 'rb') as f:
        file = pickle.load(f)
        answer = 0
        if type(file) is dict:
            for i in file.keys():
                if type(i) is int:
                    answer += i
        elif type(file) is list:
            answer = min(file) * max(file)
        else:
            print('Файл не список и не словарь')
    if answer == int1:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')

create_pickle_list()
checksum(os.path.join(basedir, 'pickle.pickle'), 2432)