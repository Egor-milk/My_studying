import pytest
from task_5 import get_value
from collections import ChainMap


def test_task_5_1():
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    assert (get_value(chainmap, 'name')) == 'Arthur'

def test_task_5_2():
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    assert (get_value(chainmap, 'name', False)) == 'Timur'

def test_task_5_3():
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    assert (get_value(chainmap, 'age')) == None

def test_task_5_4():
    chainmap = ChainMap({'name': 'Arthur'})
    assert (get_value(chainmap, 'name', False)) == 'Arthur'

def test_task_5_5():
    chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})
    assert (get_value(chainmap, 'name')) == 'Anri'

def test_task_5_6():
    chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})
    assert (get_value(chainmap, 'age', False)) == 29