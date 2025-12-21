from collections import OrderedDict
from Task_4 import custom_sort

def test_Task_4():
    data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
    custom_sort(data, by_values=True)
    assert [*data.items()]== [('Mercury', 1), ('Venus', 2), ('Earth', 3), ('Mars', 4)]

def test_Task_4_1():
    data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
    custom_sort(data)
    assert data == OrderedDict([('Anabel', 17), ('Brian', 40), ('Carol', 16), ('Dustin', 29)])


