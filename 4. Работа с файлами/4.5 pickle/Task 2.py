import os, pickle, sys
from autotest import basedir
import inspect
import types

def func(*args):
    """Тестовая функция"""
    return ' '.join(args)



# Способ 1: Сохранение исходного кода
def save_function_source(func, filename):
    """Сохраняет исходный код функции"""
    source_code = inspect.getsource(func)
    function_info = {
        'source_code': source_code,
        'name': func.__name__,
        'docstring': func.__doc__
    }

    with open(filename, 'wb') as f:
        pickle.dump(function_info, f)


def load_function_source(filename):
    """Загружает и восстанавливает функцию безопасно"""
    with open(filename, 'rb') as f:
        function_info = pickle.load(f)

    # Создаем отдельное пространство имен для выполнения
    local_namespace = {}
    exec(function_info['source_code'], {}, local_namespace)

    # Берем функцию из созданного пространства имен
    loaded_func = local_namespace[function_info['name']]
    return loaded_func


# Использование
save_function_source(func, os.path.join(basedir, 'func.pkl'))
data = [i.rstrip() for i in sys.stdin.readlines()]
loaded_func = load_function_source(os.path.join(basedir, data[0]))
print(loaded_func(*data[1:]))