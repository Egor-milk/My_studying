import pytest
from task_3 import add_to_list_in_dict

def test_task_3_1():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    add_to_list_in_dict(data, 'b', 7)
    assert data == {'a': [1, 2, 3], 'b': [4, 5, 6, 7]}

def test_task_3_2():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    add_to_list_in_dict(data, 'c', 7)
    assert data == {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7]}

def test_task_3_3():
    data = {}
    add_to_list_in_dict(data, 'c', 7)
    assert data == {'c': [7]}

def test_task_3_4():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': []}
    add_to_list_in_dict(data, 'c', 7)
    assert data == {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7]}

def test_task_3_5():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [4, 5, 6]}
    add_to_list_in_dict(data, 'b', 'stepik')
    assert data == {'a': [1, 2, 3], 'b': [4, 5, 6, 'stepik'], 'c': [4, 5, 6]}

def test_task_3_6():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [4, 5, 6]}
    add_to_list_in_dict(data, 'a', True)
    add_to_list_in_dict(data, 'a', -90)
    add_to_list_in_dict(data, 'b', False)
    add_to_list_in_dict(data, 'b', 'beegeek')
    add_to_list_in_dict(data, 'b', None)
    add_to_list_in_dict(data, 'c', [])
    assert data == {'a': [1, 2, 3, True, -90], 'b': [4, 5, 6, False, 'beegeek', None], 'c': [4, 5, 6, []]}

def test_task_3_7():
    data = {'a': [1, 2, 3]}
    add_to_list_in_dict(data, 'a', 1)
    add_to_list_in_dict(data, 'a', 3)
    add_to_list_in_dict(data, 'b', False)
    assert data == {'a': [1, 2, 3, 1, 3], 'b': [False]}