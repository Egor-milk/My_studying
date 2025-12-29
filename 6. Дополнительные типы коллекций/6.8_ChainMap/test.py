import pytest
from task_4 import deep_update
from collections import ChainMap


def test_task_4_1():
    chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
    deep_update(chainmap, 'name', 'Dima')
    assert chainmap == ChainMap({'city': 'Moscow'}, {'name': 'Dima'}, {'name': 'Dima'})

def test_task_4_2():
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    deep_update(chainmap, 'age', 20)
    assert chainmap == ChainMap({'name': 'Arthur', 'age': 20}, {'name': 'Timur'})

def test_task_4_3():
    chainmap = ChainMap({})
    deep_update(chainmap, 'city', 'Moscow')
    assert chainmap == ChainMap({'city': 'Moscow'})

def test_task_4_4():
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur', 'age': 29}, {'name': 'Anri', 'age': 20},
                        {'name': 'Dima', 'age': 20})
    deep_update(chainmap, 'age', 29)
    assert chainmap == ChainMap({'name': 'Arthur'}, {'name': 'Timur', 'age': 29},
                                {'name': 'Anri', 'age': 29}, {'name': 'Dima', 'age': 29})

def test_task_4_5():
    chainmap = ChainMap({})
    assert deep_update(chainmap, 'city', 'Moscow') == None

def test_task_4_6():
    chainmap = ChainMap({'name': 'Tanya'}, {'name': 'Arthur'}, {'name': 'Timur'})
    deep_update(chainmap, 'name', 'Dima')
    assert chainmap == ChainMap({'name': 'Dima'}, {'name': 'Dima'}, {'name': 'Dima'})